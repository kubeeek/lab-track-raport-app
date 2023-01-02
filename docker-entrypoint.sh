#!/bin/bash
echo "Waiting"
./wait-for-it.sh "db:3306"

echo "Apply database migrations"
python manage.py migrate

echo "Seed database"
python manage.py loaddata seed_testing_facility.json

echo "Running the app"
python manage.py runserver 0.0.0.0:8000