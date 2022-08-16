#!/bin/sh

set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear
#gunicorn wagsley.wsgi:application

# You can put other setup logic here

# Evaluating passed command:
exec "$@"