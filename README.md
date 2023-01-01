# Introduction
There are two ways to run the app: using Docker or locally on your machine.

## Using Docker
1. Run this command in the root directory of a project, enter: 

``docker-compose up``

## Running it locally
1. Before beginning, ensure that you have Python 3 and pip installed on your machine
2. To install the necessary dependencies, run: `pip install -r requirements.txt`
3. In addition, make sure you have configured the database and specified the proper config in the settings.py file
4. Migrate: `python manage.py migrate`
5. Run the app: `python manage.py runserver 0.0.0.0:8000`