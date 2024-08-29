import requests
from recipe_scrapers import scrape_html
from airium import Airium
import sys

url = input("Enter recipe url: ")
name = input("Enter agent name: ")
html = requests.get(url, headers={"User-Agent": f"Hungry person {name}"}).content
scraper = scrape_html(html, org_url=url)

print(scraper.to_json())