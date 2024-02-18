# Тестовое задание для компании WelbeX

## Установка (Linux)

- заполнить .env файл по примеру .env.example
- sudo docker-compose up --build
- sudo docker-compose exec web python manage.py alembic upgrade head


## Эндпоинты
- /api/routes/ping -> pong
- /api/routes/{id} -> маршрут по id
- /api/routes -> сгенерировать на основе существующего файла новый экземпляр маршрута
- /api/routes?format=csv -> закинуть новый файл и создать на его основе маршрут

## Что можно добавить в апи

- получение всех маршрутов
- получить активный файл

## Запуск юнит тестов

```bash
sudo docker-compose exec web python manage.py run_tests
```
- Добавлять новые тесты можно по примеру и наследуясь от BaseTest