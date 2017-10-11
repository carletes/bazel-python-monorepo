import requests


__all__ = [
    "url_content",
]


def url_content(url):
    return requests.get(url).content
