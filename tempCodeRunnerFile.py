import requests

def get_coordinates(location):
    url = f"https://api.searoutes.com/geocoding/v2/all?query={location}"

    headers = {
        "accept": "application/json",
        "x-api-key": "p1u19OkokB4cTpiWyGtyd9aPziSvF1XS8BbXl2X5"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if data:
        return data[0]['geometry']['coordinates']
    else:
        return None

source = input("Enter source location: ")
destination = input("Enter destination location: ")

source_coords = get_coordinates(source)
destination_coords = get_coordinates(destination)

print(f"Source coordinates: {source_coords}")
print(f"Destination coordinates: {destination_coords}")