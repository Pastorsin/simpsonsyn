import sys

import random

import questionary
from questionary import Choice

from typing import List, Any

from . import scrapper
from .scrapper import Season, Episode


def render_checkbox(title: str, choices: List[Choice]) -> List[Any]:
    checkbox = questionary.checkbox(title, choices=choices)
    items_selected = checkbox.ask()

    if not items_selected:
        stop()

    return items_selected


def choose_seasons() -> List[Season]:
    seasons = scrapper.seasons()

    seasons_selected = render_checkbox(
        "Seleccione las temporadas para randomear",
        choices=[Choice(season.name, value=season) for season in seasons],
    )

    return seasons_selected


def choose_episodes_of(season: Season) -> List[Episode]:
    episodes = scrapper.episodes(season)

    episodes_selected = render_checkbox(
        f"Temporada {season.name} Seleccione los episodios para randomear",
        choices=[Choice(episode.name, value=episode) for episode in episodes],
    )

    return episodes_selected


def start():
    seasons_selected = choose_seasons()
    season = random.choice(seasons_selected)

    episodes_selected = choose_episodes_of(season)
    episode = random.choice(episodes_selected)

    questionary.print(f"Capítulo elegido: {episode.name}", style="fg:#ffaa33")
    questionary.print(f"Miralo en: {episode.url}", style="bold fg:#ffaa33")


def stop(error=False):
    exit_code = 1 if error else 0
    sys.exit(exit_code)
