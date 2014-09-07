FROM ubuntu:14.04
MAINTAINER Nathan Osman <admin@quickmediasolutions.com>

# Create the twobuntu user
RUN useradd -m twobuntu

# Install the packages to clone the repository and the dependencies
RUN \
  apt-get update && \
  apt-get install -y git python-pip python-dev libpq-dev libjpeg8-dev

# Switch to the twobuntu user
USER twobuntu
WORKDIR /home/twobuntu

# Clone the repository
RUN git clone https://github.com/2buntu/2buntu-Django-Blog.git
