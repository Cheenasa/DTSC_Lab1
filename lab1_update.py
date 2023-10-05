import requests
from lxml import etree

 

page = requests.get('https://www.law.uchicago.edu/directory?profile_type=103')

 

html_content = page.content
html_tree = etree.HTML(html_content)
xpath_expression = '//a/@href'
links = html_tree.xpath(xpath_expression)

 

bio_urls = []
substring = "/faculty/"
for link in links:
    if substring in link:
        bio_url = 'https://www.law.uchicago.edu' + link
        bio_urls.append(bio_url)
bio_urls = list(set(bio_urls))

 

from bs4 import BeautifulSoup

 

bios = []
for bio_url in bio_urls:
    print(bio_url)
    response = requests.get(bio_url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")
        # Find the element containing the bio based on the class name
        bio_element = soup.find("div", class_="profile__bio-copy")
        # Extract the text from the element
        if bio_element:
            bio = bio_element.get_text(strip=True)
            print(bio)
            bios.append(bio)
        else:
            print("Bio element not found on the webpage.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

import io

 

try:
    with io.open("bios.txt", "w", encoding="utf-8") as f:
        for index, bio in enumerate(bios):
            f.write(bio + "\n")
            print(bio)
except Exception as e:
    print("An error occurred: ", str(e))
