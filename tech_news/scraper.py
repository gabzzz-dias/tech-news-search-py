import requests
import time
from parsel import Selector
from tech_news.database import create_news

def fetch(link):
    time.sleep(1)
    try:
        resp = requests.get(link, timeout=3)
        resp.raise_for_status()

    except requests.HTTPError:
        return None

    except requests.Timeout:
        return None

    return resp.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
