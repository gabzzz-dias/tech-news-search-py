import requests
import time
from parsel import Selector
from tech_news.database import create_news


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


def scrape_next_page_link(html_content):
    sel = Selector(html_content)

    return sel.css(".tec--btn--lg::attr(href)").get()


def scrape_noticia(html_content):
    sel = Selector(html_content)

    url = sel.css("link[rel=canonical]::attr(href)").get()
    title = sel.css(".tec--article__header__title::text").get()
    date = sel.css("time::attr(datetime)").get()
    writer = sel.css(
        ".z--font-bold").css("*::text").get().strip() or ""
    comments = sel.css(".tec--btn::attr(data-count)").get()
    summary = "".join(sel.css(
        ".tec--article__body > p:nth-child(1) ::text"
    ).getall())
    sources = sel.css(
        ".z--mb-16 .tec--badge::text"
    ).getall()
    categories = sel.css(
        ".tec--badge--primary::text"
    ).getall()

    try:
        shares = sel.css(
            ".tec--toolbar__item::text"
        ).get().strip().split(" ")[0]
    except AttributeError:
        shares = 0

    return {
        "url": url,
        "title": title,
        "timestamp": date,
        "writer": writer,
        "shares_count": int(shares),
        "comments_count": int(comments),
        "summary": summary,
        "sources": [x.strip() for x in sources],
        "categories": [y.strip() for y in categories],
    }


def get_tech_news(amount):
    url = fetch("https://www.tecmundo.com.br/novidades")
    data = scrape_novidades(url)

    if len(data) < amount:
        next_page = fetch(scrape_next_page_link(url))
        data.extend(scrape_novidades(next_page))
    result = []

    for x in data:
        new = scrape_noticia(fetch(x))

        if len(result) < amount:
            result.append(new)
    create_news(result)

    return result
