from tech_news.database import find_news
from tech_news.database import db


def top_5_news():
    data = find_news()
    result = []

    for x in data:
        x["soma"] = x["shares_count"] + x["comments_count"]

    data.sort(key=lambda x: x["soma"], reverse=True)
    news = data[:5]

    for x in news:
        result.append((x["title"], x["url"]))

    return result


def top_5_categories():
    result = []
    data = db.news.aggregate(
        [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "total": {"$sum": 1}}},
            {"$sort": {"_id": 1}},
        ]
    )

    for x in data:
        result.append(x["_id"])

    return result[:5]
