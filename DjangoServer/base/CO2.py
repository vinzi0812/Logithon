import requests

def get_co2(sc,dc, api_key):
    urls = ["https://api.searoutes.com/co2/v2/direct/air", "https://api.searoutes.com/co2/v2/direct/sea","https://api.searoutes.com/co2/v2/direct/road"]
    query = {
        "fromCoordinates" :sc[::-1],
        "toCoordinates" : dc[::-1],
        "weight" : 1000,
    }
    headers = {
    "accept": "application/json",
    "x-api-key": "Geb5fiIf743SUzpAjmRF88Z2Kn8z7SYV35DqjgHh"
    }
    answer = []
    for url in urls:
        response = requests.get(url, params=query, headers=headers)
        data = response.json()
        #print(data["co2e"])
        # if data["total"] != None:
        #     answer.append(data["total"])
            
    return data

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
    print(data)
    return data["hits"][0]["point"]

CO2_api_key = 'Geb5fiIf743SUzpAjmRF88Z2Kn8z7SYV35DqjgHh'
geocoods_api_key = '7bf48df5-2e24-433b-9690-49accd446cc4'

source = input("Enter the source location: ")
destination = input("Enter the destination location: ")

source_coords = get_coordinates(source, geocoods_api_key)
destination_coords = get_coordinates(destination, geocoods_api_key)

sc= list(source_coords.values())
dc = list(destination_coords.values())

print(f"Coordinates of the source ({source}): {source_coords}")
print(f"Coordinates of the destination ({destination}): {destination_coords}")

print(get_co2(sc, dc, CO2_api_key))
#print(routes)