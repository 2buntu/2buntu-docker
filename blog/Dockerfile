FROM ubuntu:14.04
MAINTAINER Nathan Osman <admin@quickmediasolutions.com>

# Install the packages needed to
#  - clone the repository
#  - build the binary Python packages
#  - get uWSGI up and running
RUN \
  apt-get update && \
  apt-get install -y git python3-pip libpq-dev libjpeg8-dev uwsgi uwsgi-plugin-python3 && \
  rm -rf /var/lib/apt/lists/*

# Switch to the /data directory, clone the repository, and add the local_settings file
WORKDIR /data
RUN git clone https://github.com/2buntu/2buntu-Django-Blog.git src
COPY local_settings.py /data/src/twobuntu/

# Install the required packages from PIP
RUN pip3 install -r src/requirements.txt

# Add the script for running the uWSGI server and local_settings file
COPY run.sh /root/
CMD /root/run.sh

# Expose port 80 (intended to be linked to nginx or equivalent)
EXPOSE 80
