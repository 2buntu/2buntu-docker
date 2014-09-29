#!/bin/bash
set -e

src/manage.py collectstatic --noinput
src/manage.py migrate

uwsgi \
  --http-socket 0.0.0.0:80 \
  --plugin python \
  --chdir /root/src \
  --module twobuntu.wsgi \
  --static-map /media=/data/www/media \
  --static-map /static=/data/www/static

