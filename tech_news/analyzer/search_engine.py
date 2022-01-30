from tech_news.database import find_news
# import datetime


def search_by_title(title):
    data = find_news()
    result = []

    for new in data:
        if new['title'].lower() == title.lower():
            result.append((new['title'], new['url']))

    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
