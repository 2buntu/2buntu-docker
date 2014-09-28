#!/bin/bash
set -e

src/manage.py collectstatic --noinput
src/manage.py migrate

uwsgi \
  --http-socket 0.0.0.0:8000 \
  --plugin python \
  --chdir /root/src \
  --module twobuntu.wsgi
