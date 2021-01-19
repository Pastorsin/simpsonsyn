import requests


def get(url: str, headers=None) -> str:
    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception

        return response.text

    except Exception:
        raise Exception(f"Ha ocurrido un error al acceder a {url}")


def getSeasons() -> str:
    URL = "https://simpsons-latino.net/"
    return get(URL)
