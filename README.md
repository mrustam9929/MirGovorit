# Тестовое задание MirGovorit backend

## СТЕК

- Django
- DRF

## Установка

### .ENV EXAMPLE

```
DEVELOPMENT_MODE=DEVELOPER
SECRET_KEY=xxx
ALLOWED_HOSTS=*
DEBUG=1

```

## **Установка зависимостей:**

```bash
pip install -r requirements.txt
```

или

```bash
poetry install
```

```bash
python manage.py migrate
```

## **Запуск проекта**

### Заполнить тестовыми данными

```bash
python manage.py create_test_data
```

### Запуск проекта

```bash
python manage.py runserver
```

### URLS
http://localhost:8000/admin - админка django. Логин: admin, пароль: admin

http://localhost:8000/api/docs - API документация swagger

http://localhost:8000/recipe-list/<product_id>/ - Список продуктов
 