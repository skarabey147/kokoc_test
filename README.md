# Kokoc Group Tests
Тестовое задание на Django для Kokoc Group.

# Описание проекта

Приложение предназначено для прохождения тестов и опросов. Сайт ведет статистику по пройдемым тестам, подсчитывает очки за пройденные тесты. 
Реализованна аутентификация, просмотр профилей пользователей. В будущем планируется добавить магазин, для траты накопленной валюты, 
упаковать в контейнеры Docker.

# Используемые технологии
- Python 3.10
- Django 4.0

# Запуск проекта
Клонировать репозиторий, перейти в новую директорию:
```
git clone https://github.com/Skarabey147/kokoc_test
```
Инициализировать виртуальное окружение:
```
python -m venv venv
```
Активировать виртуальное окружение:
```
. venv/Scripts/activate
```
Установить зависимости проекта:
```
pip install -r requirements.txt
```
Выполнить миграции, для этого перейти в директорию с файлом manage.py:
```
python manage.py migrate
```
Зарегистировать администратора для добавления опросов:
```
python manage.py createsuperuser
```
Запустить проект:
```
python manage.py runserver
```
