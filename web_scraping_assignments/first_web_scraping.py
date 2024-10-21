import requests
from bs4 import BeautifulSoup

# request to the webpage and use BeautifulSoup to parse the HTML
response = requests.get("https://www.gutenberg.org/browse/scores/top")
soup = BeautifulSoup(response.text, 'html.parser')

# Find the 'Top 100 EBooks yesterday' section
top_100_section = soup.find(id="books-last1")
top_100_section = top_100_section.find_next('ol')

# Extract and print the titles of the books
books = top_100_section.find_all('li')
print(books)

for book in books:
    title = book.get_text().strip()
    print(title)



