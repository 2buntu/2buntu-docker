#!/bin/bash
set -e

python3 /data/src/manage.py collectstatic --noinput
python3 /data/src/manage.py migrate

uwsgi \
  --http-socket 0.0.0.0:80 \
  --plugin python3 \
  --chdir /data/src \
  --module twobuntu.wsgi \
  --static-map /media=/data/www/media \
  --static-map /static=/data/www/static

