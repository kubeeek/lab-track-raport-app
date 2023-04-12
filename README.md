# About the app
An MVC application that has been developed as part of a Python course, modeled after an existing system used in Provincial Inspectorates of Trade Quality. The application enables tracking of tests and generating reports in .docx and .csv files.

# Running the app
## Introduction
There are two ways to run the app: using Docker or locally on your machine.

## Using Docker
1. Make sure you have Docker installed.
2. Make sure that files `wait-for-it.sh` and `docker_entrypoint.sh` have execution permissions.
3. Run this command in the root directory of a project, enter: ``docker-compose up``

## Running it locally
1. Before beginning, ensure that you have Python 3 and pip installed on your machine
2. To install the necessary dependencies, run: `pip install -r requirements.txt`
3. In addition, make sure you have configured the database (MySQL) and specified the proper config in the settings.py file
4. Migrate: `python manage.py migrate`
5. Run the app: `python manage.py runserver 0.0.0.0:8000`

## Running tests 
1. Type in the project root: ``python -Wa manage.py test .\webapp\tests\ --settings=jibadproject.settings_test``
