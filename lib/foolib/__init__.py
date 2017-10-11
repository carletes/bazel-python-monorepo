import requests

from barlib import num_cpus


__all__ = [
    "url_content",
]


def url_content(url):
    return requests.get(url).content, num_cpus()
