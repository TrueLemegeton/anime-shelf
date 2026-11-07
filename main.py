import httpx
from time import sleep 


HEADERS = {"User-Agent": "anime-shelf/0.1 (contact: lemegeton.work@gmail.com)"}
url = "https://shikimori.io/api/animes"


def search_anime(query: str, limit: int=5) -> list[dict]:
    '''Функция для нахождения аниме по названию'''
    params = {'search': query, 'limit': limit}
    response = httpx.get(url=url, params=params, headers=HEADERS, timeout=10)

    return response.json()
    
def main() -> None:
    '''Главная функция.'''
    query = input('Какое аниме ищем: ')
    for anime in search_anime(query):
        print('<-------------->')
        print(f'id: {anime['id']}')
        print(f'name: {anime['name']}')
        print('name_ru', anime['russian'])
        print(f'kind {anime['kind']}')
        print(f'status: {anime['status']}')
        print(f'episodes: {anime['episodes']}')
        print(f'score: {anime['score']}')
        
  
    



if __name__ == '__main__':
    main()