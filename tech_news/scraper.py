import requests
import time
from parsel import Selector
# from tech_news.database import create_news


def fetch(url):
    time.sleep(1)
    try:
        resp = requests.get(url, timeout=3)
        resp.raise_for_status()

    except requests.HTTPError:
        return None

    except requests.Timeout:
        return None

    return resp.text


def scrape_novidades(html_content):
    sel = Selector(html_content)
    return sel.css("div.tec--card__info > h3 > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
