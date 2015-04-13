FROM phusion/baseimage:latest
MAINTAINER Nathan Osman <nathan@quickmediasolutions.com>

# Use the init command in baseimage-docker
CMD ["/sbin/my_init"]

# Add the script that runs Exim
ADD run /etc/service/exim4/

# Since installation is not interactive, we need to "seed" answers to the
# interactive questions - do that with debconf-set-selections
RUN \
    echo exim4-config exim4/dc_eximconfig_configtype select "internet site; mail is sent and received directly using SMTP" | debconf-set-selections && \
    echo exim4-config exim4/mailname string "2buntu.com" | debconf-set-selections

# Install the Exim daemon from the archives
RUN \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y exim4-daemon-light && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose port 25 (SMTP)
EXPOSE 25
