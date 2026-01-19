# Установка и запуск

## 1. Клонирование репозитория
```bash
git clone <https://github.com/Mirazen/shop_project.git>
cd <shop_project>
```
## 2. Создание виртуального окружения
```bash
pip install uv
uv venv
```
## 3. Установка зависимостей
```bash
uv run pip install -r requirements.txt
```
## 4. Настройка базы данных
Создай базу данных в PostgreSQL:
```bash
CREATE DATABASE shop_db;
```
Примени миграции:
```bash
python manage.py migrate
python manage.py loaddata data.json
```
## 5. Запуск сервера
```bash
uv run manage.py runserver
```