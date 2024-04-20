import requests
import json
from bs4 import BeautifulSoup
import google.generativeai as genai

# API keys and credentials
WEATHER_API_KEY = "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
GEMINI_API_KEY = "AIzaSyA181AEFg-9i8m0I7QwcrGdA4dw7SlGvjo"

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]
model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config, safety_settings=safety_settings)

def get_coordinates(location):
    url = f"https://api.searoutes.com/geocoding/v2/all?query={location}"
    headers = {
        "accept": "application/json",
        "x-api-key": WEATHER_API_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['features'][0]['geometry']['coordinates']

# Function to get all possible airports along the flight route using Gemini API
def get_airports_along_route(source_city, destination_city):
    prompt = f"Find all possible airports and regions that a flight would pass over while traveling from {source_city} to {destination_city}. Include airports for direct flights as well as for flights with stopovers. Provide the response with just the names in a list format. The response should be in this format : [airport1, airport2, airport3, ...] and nothing else"
    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    airports_json = convo.last.text
    print(airports_json)
    return airports_json.replace("\\n", "").strip().split("-") if airports_json else []

# Function to scrape news and get weather for a location
def scrape_news_and_weather(location):
    news_url = f"https://www.google.com/search?q=news+{location}&tbm=nws"
    weather_url = f"https://api.searoutes.com/weather/v2/current?location={location}"
    headers = {"accept": "application/json", "x-api-key": WEATHER_API_KEY}

    news_response = requests.get(news_url)
    weather_response = requests.get(weather_url, headers=headers)

    news_soup = BeautifulSoup(news_response.text, "html.parser")
    weather_data = weather_response.json()

    news_headlines = [headline.text for headline in news_soup.find_all("div", class_="BNeawe")]
    weather_info = weather_data.get("weather", {}).get("condition", {}).get("overall", "")

    return news_headlines, weather_info

def check_safety(airports):
    unsafe_areas = []
    print(airports)
    for area in airports:
        location = area
        news_headlines, weather_info = scrape_news_and_weather(location)
        if not is_safe_to_fly(location, news_headlines, weather_info):
            unsafe_areas.append(location)
    return unsafe_areas

# Function to determine if a location is safe to fly based on news and weather
def is_safe_to_fly(location, news_headlines, weather_info):
    unsafe_keywords = ["storm", "hurricane", "tornado", "blizzard", "earthquake", "tsunami", "attack", "riot", "protest", "unrest"]
    news_text = " ".join(news_headlines).lower() if news_headlines else ""
    for keyword in unsafe_keywords:
        if keyword in news_text or (weather_info and keyword in weather_info.lower()):
            return False
    return True

def get_optimized_routes(source_city, destination_city, unsafe_areas):
    unsafe_areas_str = ", ".join(unsafe_areas)
    prompt = f"Considering that currently airports in {unsafe_areas_str} are unsafe to fly through, find the optimized flight routes from {source_city} to {destination_city}. Give the response in a JSON format with the following structure: [{{'source': '{source_city}', 'destination': '{destination_city}', 'stops': [{{'airport': 'stop_airport'}}]}}]."
    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    optimized_routes_json = convo.last.text
    optimized_routes_json = optimized_routes_json.replace("```", "").replace("json", "").strip()
    optimized_routes = []
    if optimized_routes_json:
        try:
            optimized_routes = json.loads(optimized_routes_json)
        except json.decoder.JSONDecodeError:
            print(f"Error decoding JSON: {optimized_routes_json}")
    return optimized_routes

# Main function
def main():
    source_city = input("Enter source city: ").strip()
    destination_city = input("Enter destination city: ").strip()
    airports = get_airports_along_route(source_city, destination_city)
    unsafe_areas = check_safety(airports)
    safe_areas = [area for area in airports if area not in unsafe_areas]

    optimized_routes = get_optimized_routes(source_city, destination_city, unsafe_areas)

    print("Direct flight options:")
    direct_flights = [{"source": source_city, "destination": destination_city, "stops": []}]  # Assume a direct flight is available
    if direct_flights:
        for flight in direct_flights:
            print(f"{flight['source']} -> {flight['destination']}")
    else:
        print("No direct flight options available.")

    print("\nLayover flight options:")
    layover_flights = [route for route in optimized_routes if route["stops"]]
    if layover_flights:
        for flight in layover_flights:
            stops = ", ".join([stop["airport"] for stop in flight["stops"]])
            print(f"{flight['source']} -> {flight['destination']}, Stops: {stops}")
    else:
        print("No layover flight options available.")

    print("\nUnsafe areas to avoid:")
    if unsafe_areas:
        print(", ".join(unsafe_areas))
        optimized_routes = get_optimized_routes(source_city, destination_city, unsafe_areas)
        print("\nOptimized routes:")
    else:
        print("No unsafe areas found.")

if __name__ == "__main__":
    main()