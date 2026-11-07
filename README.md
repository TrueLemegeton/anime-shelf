# anime shelf

Личная библиотека аниме и ранобэ: поиск по названию через Shikimori API,
статусы просмотра, оценки и рецензии.

## Зачем

Google keep превращается в кашу из 100+ строк, где сезоны склеены с названиями, а прогресс в пяти форматах. Нужна своя база с нормальной структурой.

## Что сделано

- [x] Поиск аниме по названию (Shikimori API)
- [ ] Сохранение в SQLite
- [ ] Статусы и оценки
- [ ] Рецензии
- [ ] Импорт из заметки Google Keep

## Стек

- Python 3.15
- httpx - запросы к API
- SQLite - хранилище

## Запуск

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py