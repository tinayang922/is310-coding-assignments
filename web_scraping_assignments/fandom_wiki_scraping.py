import requests
from bs4 import BeautifulSoup
import csv

# Send a request to the webpage
response = requests.get("https://www.mariowiki.com/Characters")

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Scraping character names from the wiki
characters = []
character_list = soup.find_all('li')

for item in character_list:
    a_tag = item.find('a')
    italic_tag = item.find('i')
    
    if a_tag and italic_tag:
        name = a_tag.text.strip() 
        first_appearance = italic_tag.text.strip()
        characters.append([name, first_appearance])


# Save the data to a CSV file
with open('characters.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'First Appearance']) 
    writer.writerows(characters)
