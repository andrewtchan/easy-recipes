import requests
from recipe_scrapers import scrape_html
from airium import Airium
import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://cooking.nytimes.com/recipes/1017303-roast-lamb'
    name = 'Andrew C.'
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

    html = str(a)
    return html

if __name__ == "__main__":
    app.run(debug=False)
