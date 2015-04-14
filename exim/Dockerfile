FROM 2buntu/base:latest
MAINTAINER Nathan Osman <nathan@quickmediasolutions.com>

# Since installation is not interactive, we need to "seed" answers to the
# interactive questions - do that with debconf-set-selections
RUN \
    echo exim4-config exim4/dc_eximconfig_configtype select "internet site; mail is sent and received directly using SMTP" | debconf-set-selections && \
    echo exim4-config exim4/use_split_config boolean true | debconf-set-selections && \
    echo exim4-config exim4/mailname string "2buntu.com" | debconf-set-selections

# Install the Exim daemon from the archives
RUN \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y exim4-daemon-light && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add config file and update the configuration
ADD 000_localmacros /etc/exim4/conf.d/main/
RUN update-exim4.conf

# Add the script that runs Exim
ADD run /etc/service/exim4/

# Expose port 25 (SMTP)
EXPOSE 25
