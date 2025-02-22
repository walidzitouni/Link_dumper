import requests
import scrapy
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import tldextract
import concurrent.futures
import os
import json

#::main::
file_links = []  # default links
file_js = []  # js_files

# Request and prettier
def request(Link):
    try:
        Request = requests.get(f'{Link}', verify=False)
        if Request.status_code == 200:
            soup = BeautifulSoup(Request.content, 'lxml')
            # Find all links within href
            links = soup.find_all('a', href=True)  # list of all <a href
            for link in links:
                href = link.get('href')  # take the value of href=

                if not href.startswith('http') and href.startswith('/'):
                    file_links.append(urljoin(Link, href))  # add Link + value of href
                else:
                    if href.startswith('http'):
                        file_links.append(href)

            links_js = soup.find_all('script', src=True)  # list of all <script src=
            for link in links_js:
                src = link.get('src')  # take the value of src=

                if not src.startswith('http') and src.startswith('/') and src.endswith('.js'):
                    file_js.append(urljoin(Link, src))  # add Link + value of src
                else:
                    if src.endswith('.js'):
                        file_js.append(src)
    except requests.exceptions.RequestException as e:
        print(f"Error while requesting {Link}: {e}")

# Load links from a text file
def load_links_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

#-------------------- Process links from text file --------------------
file_with_links = input("Enter the path to the text file containing links (eg :C://....) : ")

links_from_file = load_links_from_file(file_with_links)
for URL in links_from_file:
    request(URL)

#-------------------- Saving ------------------
with open('file_js.json', 'w') as json_file:
    json.dump(file_js, json_file, indent=4)
with open('file_links.json', 'w') as json_file:
    json.dump(file_links, json_file, indent=4)

# Load existing links from JSON files
def load_existing_links(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            return json.load(json_file)
    else:
        return []

# Save updated links to JSON files
def save_links_to_file(filename, links):
    with open(filename, 'w') as json_file:
        json.dump(links, json_file, indent=4)

#--------- Crawl all links from the current JSON ------------
def crawl_from_file():
    existing_links = load_existing_links('file_links.json')
    for link in existing_links:
        print(f"Crawling: {link}")  # for GUI interface
        request(link)  # Request again html
    # Save updated links
    save_links_to_file('file_js.json', file_js)
    save_links_to_file('file_links.json', file_links)

crawl_from_file()  # dumping links

#------ Delete duplicated links ----------
def duplicated_links(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    unique_links = []
    for link in data:
        if link not in unique_links:
            unique_links.append(link)
    with open(filename, 'w') as file:
        json.dump(unique_links, file, indent=4)

#--------------------------------------------
duplicated_links('file_links.json')
duplicated_links('file_js.json')
