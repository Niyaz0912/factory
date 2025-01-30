# Приложение "Помощник оператора"

## Описание

Это приложение предназначено для управления сменными заданиями, пользователями (операторами) в производственной среде.
Пользователи могут регистрироваться, входить в систему, обновлять свои данные и просматривать информацию о сменных 
заданиях. А также в приложении есть специальный модуль "История процесса", в котором операторы записывают параметры 
изготовляемой продукции и ведут смену (запуск станка, периодический контроль, поломка и ремонт и т.д.).

## Используемые технологии

- **Django**: Веб-фреймворк для создания веб-приложений на Python.
- **Pandas**: Библиотека для работы с данными и анализа данных.
- **Bootstrap**: CSS-фреймворк для стилизации интерфейса.
- **PostgreSQL**: Система управления базами данных 
## Установка

Следуйте этим шагам, чтобы запустить приложение локально:

### 1. Клонирование репозитория

Сначала клонируйте репозиторий на свой компьютер: https://github.com/Niyaz0912/factory


### 2. Создание виртуального окружения

Создайте виртуальное окружение для установки зависимостей: python -m venv venv


### 3. Установка зависимостей

Установите необходимые зависимости: pip install -r requirements.txt


### 4. Настройка базы данных
в файле settings.py внесите настройки для работы с PostgreSQL

Создание БД, Админа, Мастера и экземпляра Оператора производится при помощи класса BaseCommand:

python manage.py ccdb (создает БД в PostgreSQL)

python manage.py ccsu (создает Админа, Мастера и Оператора).



### 5. Применение миграций

Примените миграции, чтобы создать необходимые таблицы в базе данных при помощи команд:
python manage.py makemigrations,
python manage.py migrate


### 6. Запуск сервера

Запустите сервер разработки: 

python manage.py runserver

