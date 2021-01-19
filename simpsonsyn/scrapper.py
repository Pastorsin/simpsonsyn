from dataclasses import dataclass

from typing import List

from . import http

from bs4 import BeautifulSoup


@dataclass
class Episode:
    name: str
    url: str


@dataclass
class Season:
    name: str
    url: str


def seasons() -> List[Season]:
    html = http.getSeasons()
    soup = BeautifulSoup(html, "html.parser")

    anchors = soup.select("#homepage-items > a")

    links = map(lambda anchor: anchor.attrs.get("href"), anchors)
    available_links = list(filter(bool, links))

    names = map(lambda link: link.split("/")[-1], available_links)

    return list([Season(*args) for args in zip(names, available_links)])


def episodes(season: Season) -> List[Episode]:
    html = http.get(season.url)
    soup = BeautifulSoup(html, "html.parser")

    anchors = soup.select(".movies-list > * > a")

    links = map(lambda anchor: anchor.attrs.get("href"), anchors)
    available_links = list(filter(bool, links))

    titles = soup.select(".title")
    names = map(lambda title: title.text, titles)

    return list([Episode(*args) for args in zip(names, available_links)])
