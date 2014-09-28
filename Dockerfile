FROM ubuntu:14.04
MAINTAINER Nathan Osman <admin@quickmediasolutions.com>

# Install the packages needed to
#  - clone the repository
#  - build the binary Python packages
#  - get uWSGI up and running
RUN \
  apt-get update && \
  apt-get install -y git python-pip python-dev libpq-dev libjpeg8-dev uwsgi uwsgi-plugin-python && \
  rm -rf /var/lib/apt/lists/*

# Switch to the home directory, clone the repository, and install pip packages
WORKDIR /root
RUN \
  git clone https://github.com/2buntu/2buntu-Django-Blog.git src && \
  pip install -r src/requirements.txt

# Add the local_settings file
ADD local_settings.py /root/src/twobuntu/local_settings.py

# TODO:
# - create volume for www data
