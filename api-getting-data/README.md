# API-Getting-Data Assignment

## Overview
This is my first time using API to retrieve data from two different APIs. **Europeana API** is the required API, and the 
people API (https://swapi.dev/api/people/)from **Star Wars API (SWAPI)** is my chosen API. The goal is to query a specific Star Wars character and find related sports data from Europeana using the character's name. You will get combined data in a JSON file in the end. 

## Requirements
- Python 3.x
- `requests` library 
- A Europeana API Key (Go to: https://pro.europeana.eu/pages/get-api) to get your own personal Europeana API Key. 

## Reminder
- Be sure to get your Europeana API Key before running my script. 
- Type your own Europeana API Key
- You can also change the Stars War characters from 0 to 9 under the for loop in the script
Ex.I have i==3 for Darth Vader

def main():
    people_data = get_swapi_people()
    results = people_data['results']
    for i in range(len(results)):
        if i == 3:
            the_one_i_want = results[i].get('name')
        print(results[i].get('name'))
    print("This is the one I want:")
    print(the_one_i_want)






