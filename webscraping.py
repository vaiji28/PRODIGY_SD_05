import requests
from bs4 import BeautifulSoup
import csv

# Define the URL for the e-commerce website (Amazon example)
url = 'https://www.amazon.com/s?k=laptops'

# Set up headers to mimic a browser visit (necessary for scraping)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

# Make the HTTP request to the website
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the product elements (specific to the site's HTML structure)
products = soup.find_all('div', {'data-component-type': 's-search-result'})

# Open the CSV file for writing
with open('product_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the headers
    writer.writerow(['Product Name', 'Price', 'Rating'])

    # Loop through the products and extract the necessary information
    for product in products:
        # Extract product name
        name = product.h2.text.strip()

        # Extract product price
        price = product.find('span', class_='a-price-whole')
        price = price.text if price else 'N/A'  # Handle missing price

        # Extract product rating
        rating = product.find('span', class_='a-icon-alt')
        rating = rating.text if rating else 'N/A'  # Handle missing rating

        # Write the data to the CSV file
        writer.writerow([name, price, rating])

print("Product data has been saved to product_data.csv")
