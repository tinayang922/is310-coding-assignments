# api-getting-data assignment

import requests
import json
import os

# Type your EUROPEANA API key below:
EUROPEANA_API_KEY = "Your-API-keys"  # Use your API key

# Get data from the Star Wars API (SWAPI) for a specific character
def get_swapi_people():
    swapi_url = f"https://swapi.dev/api/people/"
    response = requests.get(swapi_url)
    if response.status_code == 200:
        people_data = response.json()
        return people_data
    else:
        print("Failed to fetch data from SWAPI.")
        return None

# Get related sports data from the Europeana API
def get_europeana_sports_data(query):
    europeana_url = "https://api.europeana.eu/record/v2/search.json"
    params = {
        "query": query, 
        "wskey": EUROPEANA_API_KEY,
        "rows": 1  
    }
    response = requests.get(europeana_url, params=params)
    if response.status_code == 200:
        europeana_data = response.json()
        # print("Europeana Response:", json.dumps(europeana_data, indent=2))
        return europeana_data
    else:
        # print(response)
        print("Failed to fetch data from Europeana.")
        return None

# combine data to a JSON file
def save_to_json(data, filename="swapi_europeana_sports_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)
    print(f"Data saved to {filename}")

def main():
    people_data = get_swapi_people()
    results = people_data['results']
    for i in range(len(results)):
        if i == 3:
            the_one_i_want = results[i].get('name')
        print(results[i].get('name'))
    print("This is the one I want:")
    print(the_one_i_want)

# Use the character's name to search Europeana for sports-related items
    if the_one_i_want:
        europeana_data = get_europeana_sports_data(the_one_i_want)

# Combine both datasets and save to a JSON file
        combined_data = {
            "Europeana Sports Data": europeana_data["items"]
        }
        save_to_json(combined_data)

if __name__ == "__main__":
    main()
