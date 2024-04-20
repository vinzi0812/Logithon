import requests
import json
from bs4 import BeautifulSoup
import google.generativeai as genai
from sea import *
from base import *
from land import *

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

def get_routes(source, destination, api_key):
    prompt = f"I want to go from {source} to {destination}. Find me the best route with the least carbon emission and cost. Mode of transport can be land, air or sea. Include the duration of the journey as well. Provide the response in this format: [source, destination, mode_of_transport(Air, Sea or Road), cost(in rupeees without commas), carbon_emission, duration] and nothing else. You can use multiple modes of transport if needed. In such a case, provide the details for each mode of transport separately."
    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    paths = convo.last.text
    paths = paths.replace('[', '').replace(']', '').split("\n")
    arr = []
    for path in paths:
        arr.append(path.split(","))
        if path[2] == "sea":
            get_route_details(path[0], path[1])
        elif path[2] == "air":
            airmain(path[0], path[1])
        else:
            landmain(path[0], path[1])
        # elif path[2] == "sea":
            
        # else:
            #get land routes
        
    

get_routes("New York", "Mumbai", "7bf48df5-2e24-433b-9690-49accd446cc4")