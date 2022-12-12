Go To Home

![flake8 test](https://github.com/dino-mayk/IntensiveYandex/actions/workflows/python-package.yml/badge.svg)

# Оглавление

- [Установка](#установка)
- [Запуск](#запуск)
- [Тесты](#тесты)
- [Разработка](#разработка)

# Установка

Клонируйте репозиторий:
```bash
git clone https://github.com/dino-mayk/IntensiveYandex.git
```

Создайте виртуальное окружение:

Windows:
```bash
python -m venv venv
```
Mac, Linux:
```bash
python3 -m venv venv
```

Активируйте виртуальное окружение:

Windows:
```bash
cd venv/Scripts/
.\activate
```
Mac, Linux:
```bash
source venv/bin/activate
```

Скачайте зависимости:

Windows:
```bash
pip install -r requirements.txt
```
Mac, Linux:
```bash
pip3 install -r requirements.txt
```

# Запуск 

Windows:
```bash
python manage.py runserver
```
Mac, Linux:
```bash
python3 manage.py runserver
```

# Тесты

Windows:
```bash
python manage.py test
```
Mac, Linux:
```bash
python3 manage.py test
```

# Разработка

Создание миграции:

Windows:
```bash
python manage.py makemigrations <app>
```
Mac, Linux:
```bash
python3 manage.py makemigrations <app>
```

Добавление миграции:

Windows:
```bash
python manage.py migrate
```
Mac, Linux:
```bash
python3 manage.py migrate
```

Создание сквош миграции:

Windows:
```bash
python manage.py squashmigrations <appname> <squashfrom> <squashto>
```
Mac, Linux:
```bash
python3 manage.py squashmigrations <appname> <squashfrom> <squashto>
```

Создание фикстур:

Windows:
```bash
python manage.py dumpdata > data.json
```
Mac, Linux:
```bash
python3 manage.py dumpdata > data.json
```

Запуск isort:

```bash
isort .
```

Диаграмма базы данных:

```bash
https://app.quickdatabasediagrams.com/#/d/ReX14b
```

Создание администратора:

Windows:
```bash
python manage.py createsuperuser
```

Mac, Linux:
```bash
python3 manage.py createsuperuser
```

Смена пароля в аккаунте:

Windows:
```bash
python manage.py changepassword <user_name>
```

Mac, Linux:
```bash
python3 manage.py changepassword <user_name>
```

Создание приложения:

Windows:
```bash
python manage.py startapp <app_name>
```

Mac, Linux:
```bash
python3 manage.py startapp <app_name>
```

Критичные данные располагаются в .env локально, для разработки в dev.env.
Чтобы запустить на production измените комментарий в settings.py.
