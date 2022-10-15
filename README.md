# Тестовый проект на Django

### Запуск

- Находимся в папке проекта
- python3 -m venv venv
- pip install -U pip && pip install -r requirements.txt
- cd postgres_l27
- docker-compose up -d
- cd ..
- source venv/bin/activate
- cd project
- python3 manage.py migrate
- python3 manage.py csv_to_json
- python3 manage.py add_new_ads
- python3 manage.py add_new_categories
- python3 manage.py createsuperuser
- python3 manage.py runserver
