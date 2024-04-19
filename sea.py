# # # import requests

# # # url = "https://api.searoutes.com/co2/v2/direct/sea"

# # # headers = {
# # #     "accept": "application/json",
# # #     "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
# # # }

# # # response = requests.get(url, headers=headers)

# # # print(response.text)
# # # import requests

# # # url = "https://api.searoutes.com/geocoding/v2/all?query=Montreal"

# # # headers = {
# # #     "accept": "application/json",
# # #     "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
# # # }

# # # response = requests.get(url, headers=headers)

# # # print(response.text)

# # # import requests

# # # url = "https://api.searoutes.com/geocoding/v2/closest/9.965629577636719%2C53.53296196255539"

# # # headers = {
# # #     "accept": "application/json",
# # #     "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
# # # }

# # # response = requests.get(url, headers=headers)

# # # print(response.text)

# # # import requests

# # # url = "https://api.searoutes.com/geocoding/v2/zipcode?countryCodes=FR&query=Montreal"

# # # headers = {
# # #     "accept": "application/json",
# # #     "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
# # # }

# # # response = requests.get(url, headers=headers)

# # # print(response.text)

# # # import requests

# # # url = "https://api.searoutes.com/geocoding/v2/sea/14.27621841430664%2C40.84464176925914"

# # # headers = {
# # #     "accept": "application/json",
# # #     "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
# # # }

# # # response = requests.get(url, headers=headers)

# # # print(response.text)

# # # import requests

# # # url = "https://api.searoutes.com/route/v2/sea/9.965629577636719%2C53.53296196255539%3B0.45069694519042963%2C51.503039451809734?continuousCoordinates=true&allowIceAreas=false&avoidHRA=false&avoidSeca=false"

# # # headers = {
# # #     "accept": "application/json",
# # #     "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
# # # }

# # # response = requests.get(url, headers=headers)

# # # print(response.text)

# # # import requests

# # # url = "https://api.searoutes.com/route/v2/sea/9.965629577636719%2C53.53296196255539%3B0.45069694519042963%2C51.503039451809734/plan?continuousCoordinates=true&allowIceAreas=false&avoidHRA=false&avoidSeca=false"

# # # headers = {
# # #     "accept": "application/json",
# # #     "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
# # # }

# # # response = requests.get(url, headers=headers)

# # # print(response.text)

# # # import requests

# # # url = "https://api.searoutes.com/weather/v2/track"

# # # payload = { "type": "Feature" }
# # # headers = {
# # #     "accept": "application/json",
# # #     "content-type": "application/json",
# # #     "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
# # # }

# # # response = requests.post(url, json=payload, headers=headers)

# # # print(response.text)
# # # import requests

# # # url = "https://api.searoutes.com/weather/v2/forecast"

# # # headers = {
# # #     "accept": "application/json",
# # #     "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
# # # }

# # # response = requests.get(url, headers=headers)

# # # print(response.text)

# # # import requests

# # # url = "https://api.searoutes.com/itinerary/v2/execution?fromLocode=BRSSZ&toLocode=COCTG&carrierScac=CMDU&nContainers=1"

# # # headers = {
# # #     "accept": "application/json",
# # #     "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
# # # }

# # # response = requests.get(url, headers=headers)

# # # print(response.text)


# # import requests

# # def get_routes(mode, source, destination):
# #     base_url = "https://api.searoutes.com"
# #     headers = {
# #         "accept": "application/json",
# #         "x-api-key": "your_api_key_here"
# #     }

# #     # Get geocoding for source and destination
# #     source_response = requests.get(f"{base_url}/geocoding/v2/all?query={source}", headers=headers)
# #     destination_response = requests.get(f"{base_url}/geocoding/v2/all?query={destination}", headers=headers)

# #     source_json = source_response.json()
# #     destination_json = destination_response.json()

# #     if not source_json or not destination_json:
# #         print("No results found for source or destination.")
# #         return

# #     source_coords = source_json[0]['geometry']['coordinates']
# #     destination_coords = destination_json[0]['geometry']['coordinates']

# #     # Get routes
# #     routes_response = requests.get(f"{base_url}/route/v2/{mode}/{source_coords[0]}%2C{source_coords[1]}%3B{destination_coords[0]}%2C{destination_coords[1]}?continuousCoordinates=true&allowIceAreas=false&avoidHRA=false&avoidSeca=false", headers=headers)

# #     routes = routes_response.json()

# #     # Get weather conditions for each route
# #     for route in routes:
# #         weather_response = requests.post(f"{base_url}/weather/v2/track", json={"type": "Feature", "geometry": route['geometry']}, headers={**headers, "content-type": "application/json"})
# #         route['weather'] = weather_response.json()

# #     return routes

# # mode = input("Enter mode of travel (sea or air): ")
# # source = input("Enter source location: ")
# # destination = input("Enter destination location: ")

# # routes = get_routes(mode, source, destination)

# # for route in routes:
# #     print(f"Route: {route['geometry']}")
# #     print(f"Weather: {route['weather']}")


# import requests

# url = "https://api.searoutes.com/geocoding/v2/area/"

# headers = {
#     "accept": "application/json",
#     "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
# }

# response = requests.get(url, headers=headers)

# print(response.text)


# import requests

# def get_coordinates(location):
#     url = f"https://api.searoutes.com/geocoding/v2/all?query={location}"

#     headers = {
#         "accept": "application/json",
#         "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
#     }

#     response = requests.get(url, headers=headers)
#     data = response.json()
#     # print(response.json())


#     return data['features'][0]['geometry']['coordinates']

# source = input("Enter source location: ")
# destination = input("Enter destination location: ")

# source_coords = get_coordinates(source)
# destination_coords = get_coordinates(destination)

# print(f"Source coordinates: {source_coords}")
# print(f"Destination coordinates: {destination_coords}")

import requests
import time

def get_coordinates(location):
    url = f"https://api.searoutes.com/geocoding/v2/all?query={location}"
    headers = {
        "accept": "application/json",
        "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['features'][0]['geometry']['coordinates']

def get_route_details(source_coords, destination_coords):
    url = f"https://api.searoutes.com/route/v2/sea/{source_coords[0]},{source_coords[1]};{destination_coords[0]},{destination_coords[1]}/plan"
    headers = {
        "accept": "application/json",
        "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
    }
    
    # Retry the request up to 3 times with a 5-second delay
    for i in range(3):
        response = requests.get(url, headers=headers)
        if response.status_code == 202:
            # The route is being calculated, you can poll the API for the result
            route_url = response.json()['href']
            response = requests.get(route_url, headers=headers)
            return response.json()
        elif response.status_code == 429:
            # Too Many Requests error, wait for 5 seconds and retry
            print(f"Too Many Requests error, retrying in 5 seconds (attempt {i+1}/3)...")
            time.sleep(5)
            continue
        else:
            return response.json()
    
    # If all retries fail, raise an error
    raise Exception("Failed to get route details after 3 attempts.")

source = input("Enter source location: ")
destination = input("Enter destination location: ")

source_coords = get_coordinates(source)
destination_coords = get_coordinates(destination)

print(f"Source coordinates: {source_coords}")
print(f"Destination coordinates: {destination_coords}")

try:
    route_details = get_route_details(source_coords, destination_coords)
    print(route_details)
except Exception as e:
    print(f"Error: {e}")