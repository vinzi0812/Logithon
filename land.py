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
    query = {
        "point": [[source_coords[1],source_coords[0]], [destination_coords[1],destination_coords[0]]],
        "vehicle": "car",
        "locale": "en",
        "key": api_key
    }

    response = requests.post(url, params=query)
    data = response.json()

    if data.get('paths'):
        routes = data['paths']
        return routes
    else:
        print("No routes found.")
        return None
    
    
# Replace 'YOUR_API_KEY_HERE' with your actual API key
api_key = '7bf48df5-2e24-433b-9690-49accd446cc4'

source = input("Enter the source location: ")
destination = input("Enter the destination location: ")

source_coords = get_coordinates(source, api_key)
destination_coords = get_coordinates(destination, api_key)

sc= list(source_coords.values())
dc = list(destination_coords.values())

print(f"Coordinates of the source ({source}): {source_coords}")
print(f"Coordinates of the destination ({destination}): {destination_coords}")

print(sc)

routes = get_routes(sc, dc, api_key)
print(routes)

