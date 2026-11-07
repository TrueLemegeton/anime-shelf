import httpx
from time import sleep


HEADERS = {"User-Agent": "anime-shelf/0.1 (contact: lemegeton.work@gmail.com)"}

for anime_id in range(20):

    response = httpx.get(f'https://shikimori.io/api/animes/{anime_id}', headers=HEADERS, timeout=10)
    print(f'Статус: {response.status_code}')
    
    if response.status_code != 200:
        print('\n===========================')
        print(f'Аниме с id = {anime_id} не было найдено в API.')
        sleep(1)
        continue
    

    anime_data = response.json()
    
    print('\n===========================')
    print(f'id: {anime_data['id']}')
    print(f'name: {anime_data['name']}')
    print(f'kind {anime_data['kind']}')
    print(f'status: {anime_data['status']}')
    print(f'episodes: {anime_data['episodes']}')
    print(f'score: {anime_data['score']}')
      
    sleep(1)



