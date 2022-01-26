# Django News Content Aggregator

> **Note:** The project is built with `Python 3.10`, but should work with any version of Python higher than 3.6.

## How To Run The Project

Create and activate a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/) for your operating system.

Upgrade pip:

```bash
(.venv) $ python -m pip install --upgrade pip
```
Install dependencies:

```bash
(.venv) $ python -m pip install django
(.venv) $ python -m pip install django-apscheduler
(.venv) $ python -m pip install feedparser
(.venv) $ python -m pip install python-dateutil
```

Migrations

```bash
(.venv) $ python manage.py makemigrations
(.venv) $ python manage.py migrate
```

Start the Django development server:

```bash
(.venv) $ python manage.py runserver
```

You can now navigate to `localhost:8000` in your browser and inspect the finished project.

