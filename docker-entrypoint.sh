#!/bin/bash
echo "Waiting"
./wait-for-it.sh "db:3306" python manage.py migrate

echo "Apply database migrations"
python manage.py migrate

echo "Running the app"
python manage.py runserver 0.0.0.0:8000