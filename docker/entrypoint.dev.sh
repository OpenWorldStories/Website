#!/bin/sh

echo "Waiting for database..."

while ! nc -z mariadb-server 3306; do
    sleep 0.1
done

echo "database started"

python manage.py makemigrations
python manage.py migrate

exec "$@"
