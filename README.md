<p align="center">
  <a href="#">
    <img src="/static_dev/favicon_package/logo.svg" alt="logo" width="1000" height="1000">
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

Clone the repository:
```bash
git clone https://github.com/dino-mayk/GoToHome.git
```

Create a virtual environment:

Windows:
```bash
python -m venv venv
```
Mac, Linux:
```bash
python3 -m venv venv
```

Activate the virtual environment:

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

Download dependencies:

Windows:
```bash
pip install -r requirements.txt
```
Mac, Linux:
```bash
pip3 install -r requirements.txt
```

[Run docker](https://www.docker.com/):

```bash
docker run -p 6379:6379 -d redis:5
```

Launch:

Windows:
```bash
python manage.py runserver
```
Mac, Linux:
```bash
python3 manage.py runserver
```

## Status

![django](https://github.com/dino-mayk/GoToHome/actions/workflows/python-package.yml/badge.svg)
![flake8](https://github.com/dino-mayk/GoToHome/actions/workflows/django.yml/badge.svg)


## Creators

**Krasnov Nikita**

- <https://twitter.com/>
- <https://github.com/>

**Dmitry Ignatiev**

- <https://twitter.com/>
- <https://github.com/>

**Timofey Kiryachek**

- <https://twitter.com/>
- <https://github.com/>


## Thanks

Thanks to our mentors from the [Yandex Academy](https://academy.yandex.ru/)


## Sponsors

No yet :(


## Copyright and license

No yet :(