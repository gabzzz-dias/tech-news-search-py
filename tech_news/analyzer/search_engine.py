from tech_news.database import find_news
import datetime


def search_by_title(title):
    data = find_news()
    result = []

    for new in data:
        if new['title'].lower() == title.lower():
            result.append((new['title'], new['url']))

    return result


def search_by_date(date):
    data = find_news()
    result = []

    try:
        datetime.date.fromisoformat(date)

        for new in data:
            if new['timestamp'][0:10] == date:
                result.append((new['title'], new['url']))

        return result

    except ValueError:
        raise ValueError("Data inválida")


def search_by_source(source):
    data = find_news()
    result = []

    for new in data:
        for x in range(len(new['sources'])):
            new['sources'][x] = new['sources'][x].lower()

        if source.lower() in new['sources']:
            result.append((new['title'], new['url']))

    return result


def search_by_category(category):
    data = find_news()
    result = []

    for new in data:
        for x in range(len(new['categories'])):
            new['categories'][x] = new['categories'][x].lower()

        if category.lower() in new['categories']:
            result.append((new['title'], new['url']))

    return result
