# Importing necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the faculty directory page for the choosen university
university_url = 'https://www.law.uchicago.edu/directory?profile_type=103'

# Send an HTTP GET request to the URL
response = requests.get(university_url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find links to individual faculty homepages
faculty_links = soup.find_all( class_="profile-list")

# Extract faculty homepage URLs and store them in bio.txt
with open("bio.txt", "w") as file:
    for link in faculty_links:
        file.write(link.text)
        print(link.text)
