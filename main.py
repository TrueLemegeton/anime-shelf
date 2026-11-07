import httpx
from time import sleep


HEADERS = {"User-Agent": "anime-shelf/0.1 (contact: lemegeton.work@gmail.com)"}
url = "https://shikimori.io/api/animes"

params = {'search': 'причина п', 'limit': 5}
response = httpx.get(url=url, params=params, headers=HEADERS, timeout=10)

animes = response.json()
for anime in animes:
    print('\n<----------------------------------->')
    print(f'id: {anime['id']}')
    print(f'name: {anime['name']}')
    print(f'kind {anime['kind']}')
    print(f'status: {anime['status']}')
    print(f'episodes: {anime['episodes']}')
    print(f'score: {anime['score']}')