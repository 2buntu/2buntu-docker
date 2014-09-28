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

# Create a volume for storing static files
VOLUME /root/www

# Add the script for running the uWSGI server and local_settings file
COPY run.sh /root/
COPY local_settings.py /root/src/twobuntu/

# Set the command for starting the uWSGI server
CMD /root/run.sh

# Expose port 8000 (intended to be linked to nginx)
EXPOSE 8000
