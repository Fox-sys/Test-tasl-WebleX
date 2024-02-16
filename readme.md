# Тестовое задание для компании WelbeX

## Установка (Linux)

- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- \**Создать .env файл и заполнить его по шаблону .env.example**
- sudo docker-compose up --build
- uvicorn manage:app --reload