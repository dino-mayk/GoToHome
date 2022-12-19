<p align="center">
  <a href="#">
    <img src="/static_dev/favicon_package/logo.svg" alt="logo">
  </a>
</p>

<h3 align="center">GoToHome</h3>

## Table of contents

- [Quick start](#quick-start)
- [Status](#status)
- [Creators](#creators)
- [Thanks](#thanks)
- [Sponsors](#sponsors)
- [Copyright and license](#copyright-and-license)


## Quick start

### Clone the repository:
```bash
git clone https://github.com/dino-mayk/GoToHome.git
```

### Create a virtual environment:

Windows:
```bash
python -m venv venv
```
Mac, Linux:
```bash
python3 -m venv venv
```

### Activate the virtual environment:

Windows:
```bash
cd venv/Scripts/
```
```bash
.\activate
```
Mac, Linux:
```bash
source venv/bin/activate
```

### Install dependencies:

Windows:
```bash
pip install -r requirements.txt
```
Mac, Linux:
```bash
pip3 install -r requirements.txt
```

### Download programs:

#### Install to start the server:
  - [Docker](https://www.docker.com/)

#### Install for testing:
  - [Chrome web browser](https://www.google.com/chrome/)
  - [Chromedriver](https://sites.google.com/chromium.org/driver/getting-started)

### Launch:

#### Docker:

```bash
docker run -p 6379:6379 -d redis:5
```

#### Django server:

Windows:
```bash
python manage.py runserver
```
Mac, Linux:
```bash
python3 manage.py runserver
```

## Status

![flake8](https://github.com/dino-mayk/GoToHome/actions/workflows/python-package.yml/badge.svg)
![django](https://github.com/dino-mayk/GoToHome/actions/workflows/django.yml/badge.svg)


## Creators

**Krasnov Nikita**

- <https://t.me/dino_mayk>
- <https://github.com/dino-mayk>

**Dmitry Ignatiev**

- <https://t.me/nekoprrr>
- <https://github.com/DmitriyIgnatev>

**Timofey Kiryachek**

- <https://t.me/TecHeReTiC>
- <https://github.com/TecHeReTiC3141>


## Thanks

Thanks to our mentors from the [Yandex Academy](https://academy.yandex.ru/)


## Sponsors

No yet :(


## Copyright and license

No yet :(