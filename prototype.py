import requests
from recipe_scrapers import scrape_html
from airium import Airium
import sys

url = input('Enter recipe url: ')
name = input('Enter agent name: ')
html = requests.get(url, headers={'User-Agent': f'Hungry person {name}'}).content
scraper = scrape_html(html, org_url=url)

a = Airium()

a('<!DOCTYPE html>')
with a.html():
    with a.head():
        a.meta(charset='utf-8')
        a.title(_t='Simply Recipes')
    
    with a.body():
        with a.h1():
            a(scraper.title())
        a.img(src=scraper.image(), alt='header image', width='50%', height='50%')
        with a.h3():
            a('Prep time: ' + str(scraper.prep_time()))
        with a.h3():
            a('Cook time: ' + str(scraper.cook_time()))
        with a.h3():
            a('Total time: ' + str(scraper.total_time()))
        with a.h3():
            a('Yields: ' + str(scraper.yields()))
        with a.h3():
            a('Ingredients')
        with a.ul():
            for ingr in scraper.ingredients():
                with a.li():
                    a(ingr)
        with a.h3():
            a('Instructions')
        with a.ol():
            for step in scraper.instructions_list():
                with a.li():
                    a(step)
        a(scraper.instructions())

html = str(a)

with open('recipetest.html', 'wb') as f:
    f.write(bytes(html, encoding='utf-8'))
