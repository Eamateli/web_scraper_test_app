import csv
import requests
from bs4 import BeautifulSoup

# Function to scrape data
def scrape_data(url, element):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request is successful
    if response.status_code == 200:
        # Parsing the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Finding the specified HTML element
        data = soup.find(element)
        
        # Cleaning the data by removing unnecessary spaces
        clean_data = data.text.strip()
        
        return clean_data

# Function to save the data to a CSV file
def save_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Writing the data to the CSV file
        writer.writerow(data)

# Get the URL from the user
url = input("Enter the URL: ")

# Get the HTML element from the user
element = input("Enter the HTML element to be scraped (e.g. p, h1, div): ")

# Scrape the data from the URL
data = scrape_data(url, element)

# Get the filename from the user
filename = input("Enter the filename for the CSV file: ")

# Save the data to a CSV file
save_to_csv(filename + '.csv', [data])

print("Data saved to", filename + '.csv')
