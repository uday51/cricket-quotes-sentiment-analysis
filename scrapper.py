import requests
from bs4 import BeautifulSoup
import csv

url = "url-of-page"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all li elements
li_elements = soup.find_all('li')

quotes_list = []

for li in li_elements:
    text = li.get_text(strip=True)
   
    # Split the text into quote and author
    if ' - ' in text:
        quote, author = text.split(' - ', 1)
    else:
        quote = text
        author = "Unknown"
   
    quotes_list.append({
        'quote': quote.strip('"').strip(),
        'author': author.strip()
    })

# Print the results
for i, item in enumerate(quotes_list, 1):
    print(f"{i}. Quote: {item['quote']}")
    print(f"   Author: {item['author']}\n")




with open('cricket_quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['quote', 'author']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   
    writer.writeheader()
    writer.writerows(quotes_list)

print("Quotes have been saved to cricket_quotes.csv")
