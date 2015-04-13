FROM phusion/baseimage:latest
MAINTAINER Nathan Osman <nathan@quickmediasolutions.com>

# Enable the SSH daemon in the container
RUN rm -f /etc/service/sshd/down

# Add all of the SSH keys to the container
ADD ssh /tmp/ssh/
RUN cat /tmp/ssh/* >> /root/.ssh/authorized_keys && rm -rf /tmp/ssh
