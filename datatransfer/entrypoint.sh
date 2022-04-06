#!/bin/sh

if [ -e ".env" ]; then
    echo "execute in local machine environment"
    until (python manage.py check --database default) do echo '...waiting...' && sleep 1; done;
    python manage.py showmigrations
    python manage.py migrate
    python manage.py showmigrations
    python manage.py runserver 0.0.0.0:8000
else
    echo "execute in k8s environment"
    python manage.py collectstatic --noinput
    python manage.py showmigrations
    python manage.py migrate
    python manage.py showmigrations
    gunicorn --log-level debug config.asgi:application --bind=0.0.0.0:8000 -k uvicorn.workers.UvicornWorker
fi
