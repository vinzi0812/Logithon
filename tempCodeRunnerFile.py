import requests

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
        "points": [[source_coords["lon"], source_coords["lat"]], [destination_coords["lon"], destination_coords["lat"]]],
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
        print("Time-optimized routes:", time_optimized_routes)
        print("Distance-optimized routes:", distance_optimized_routes)
        print("Fuel consumption-optimized routes:", consumption_optimized_routes)
    else:
        print("Could not find coordinates for one or both locations.")

if __name__ == "__main__":
    main()