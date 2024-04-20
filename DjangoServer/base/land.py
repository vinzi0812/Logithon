# import requests

# def get_coordinates(location, api_key):
#     url = "https://graphhopper.com/api/1/geocode"
#     query = {
#         "q": location,
#         "locale": "en",
#         "limit": "1",
#         "provider": "default",
#         "key": api_key
#     }
#     response = requests.get(url, params=query)
#     data = response.json()
#     if data['hits']:
#         return data['hits'][0]['point']
#     else:
#         return None

# def get_routes(sc, dc, api_key):
#     url = "https://graphhopper.com/api/1/route"
#     headers = {"Content-Type": "application/json"}
#     body = {
#         "points": [sc[::-1], dc[::-1]],
#         "snap_preventions": ["motorway", "ferry", "tunnel"],
#         "details": ["road_class"],
#         "profile": "car",
#         "locale": "en",
#         "instructions": True,
#         "calc_points": True,
#         "points_encoded": False,
#         "limit": 5,
#     }

#     response = requests.post(url, headers=headers, json=body, params={"key": api_key})
#     data = response.json()

#     if data.get('paths'):
#         routes = data['paths']
#         return routes
#     else:
#         print("No routes found.")
#         return None
    
# # Replace 'YOUR_API_KEY_HERE' with your actual API key
# api_key = '7bf48df5-2e24-433b-9690-49accd446cc4'

# source = input("Enter the source location: ")
# destination = input("Enter the destination location: ")

# source_coords = get_coordinates(source, api_key)
# destination_coords = get_coordinates(destination, api_key)

# sc= list(source_coords.values())
# dc = list(destination_coords.values())

# print(f"Coordinates of the source ({source}): {sc}")
# print(f"Coordinates of the destination ({destination}): {dc}")

# print(sc)

# routes = get_routes(sc, dc, api_key)
# print(routes)

import requests
import csv
def print_routes(routes):
    print("Route ID, Distance (km), Duration (h), Fuel Consumption (l), Cost ($)")
    for i, route in enumerate(routes, 1):
        distance_km = route['distance'] / 1000
        duration_h = route['time'] / 3600000
        fuel_consumption = distance_km * 7 / 100  # assuming 7 liters per 100 km
        cost = fuel_consumption * 1.5  # assuming $1.5 per liter
        print(f"{i}, {distance_km}, {duration_h}, {fuel_consumption}, {cost}")

# def write_to_csv(routes, filename):
#     with open(filename, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Route ID", "Distance (m)", "Duration (s)", "Fuel Consumption (l)"])
#         for i, route in enumerate(routes, 1):
#             consumption = route['consumption'] if 'consumption' in route else 'N/A'
#             writer.writerow([i, route['distance'], route['time'] / 1000, consumption])


def get_coordinates(location, api_key):
    url = "https://graphhopper.com/api/1/geocode"
    query = {
        "q": location,
        "locale": "en",
        "limit": "1",
        "provider": "default",
        "key": api_key
    }
    response = requests.get(url, params=query)
    data = response.json()
    if data['hits']:
        return data['hits'][0]['point']
    else:
        return None

def get_routes(source_coords, destination_coords, api_key):
    url = "https://graphhopper.com/api/1/route"
    headers = {"Content-Type": "application/json"}
    body = {
        "points": [[source_coords["lng"], source_coords["lat"]], [destination_coords["lng"], destination_coords["lat"]]],
        "snap_preventions": ["motorway", "ferry", "tunnel"],
        "details": ["road_class"],
        "profile": "car",
        "locale": "en",
        "instructions": True,
        "calc_points": True,
        "points_encoded": False,
        "alternatives": 5
    }

    # Get time-optimized routes
    body["optimize"] = "time"
    response = requests.post(url, headers=headers, json=body, params={"key": api_key})
    time_optimized_routes = response.json()["paths"]

    # Get distance-optimized routes
    body["optimize"] = "distance"
    response = requests.post(url, headers=headers, json=body, params={"key": api_key})
    distance_optimized_routes = response.json()["paths"]

    # Get fuel consumption-optimized routes
    body["optimize"] = "consumption"
    response = requests.post(url, headers=headers, json=body, params={"key": api_key})
    consumption_optimized_routes = response.json()["paths"]

    return time_optimized_routes, distance_optimized_routes, consumption_optimized_routes

def main():
    # Replace 'YOUR_API_KEY_HERE' with your actual API key
    api_key = '7bf48df5-2e24-433b-9690-49accd446cc4'

    source = input("Enter the source location: ")
    destination = input("Enter the destination location: ")

    source_coords = get_coordinates(source, api_key)
    destination_coords = get_coordinates(destination, api_key)

    if source_coords and destination_coords:
        print(f"Coordinates of the source ({source}): {list(source_coords.values())}")
        print(f"Coordinates of the destination ({destination}): {list(destination_coords.values())}")

        time_optimized_routes, distance_optimized_routes, consumption_optimized_routes = get_routes(source_coords, destination_coords, api_key)
        
        print("Time optimized routes:")
        print_routes(time_optimized_routes)
        
        print("Distance optimized routes:")
        print_routes(distance_optimized_routes)
        
        print("Consumption optimized routes:")
        print_routes(consumption_optimized_routes)
    else:
        print("Could not find coordinates for one or both locations.")

if __name__ == "__main__":
    main()