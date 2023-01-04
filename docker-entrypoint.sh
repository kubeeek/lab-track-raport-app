#!/bin/bash
echo "Waiting"
./wait-for-it.sh -t 30 "db:3306"

echo "Apply database migrations"
python manage.py migrate

echo "Seed database"
python manage.py loaddata seed_testing_facility.json seed_test_sample.json seed_test_label.json

echo "Running the app"
python manage.py runserver 0.0.0.0:8000