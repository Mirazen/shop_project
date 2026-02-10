# Установка и запуск

## 1. Клонирование репозитория
```bash
git clone <https://github.com/Mirazen/shop_project.git>
cd <shop_project>
```
## 2. Установка зависимостей
```bash
pip install -r requirements.txt
```
## 3. Настройка базы данных
Создай базу данных в PostgreSQL:
```bash
CREATE DATABASE shop_db;
```
Примени миграции:
```bash
python manage.py migrate
python manage.py loaddata data.json
```
## 4. Запуск сервера
```bash
python manage.py runserver
```
