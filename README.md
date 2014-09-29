## 2buntu Docker

This repository contains a Dockerfile and some helper scripts for building a container for the 2buntu blog. You can check out the blog yourself at [2buntu.com](http://2buntu.com).

### Running the Container

The 2buntu container can be deployed easily on a development machine for testing. In fact, only one important flag is required when launching the container:

    docker run -d -e DEBUG=true --name 2buntu 2buntu/2buntu-django-blog

(The `DEBUG` environment variable indicates to the container that the application should enable debug mode, which displays helpful tracebacks when errors are encountered.)

If you would like access to the source code directory, the static files, and the SQLite database, create a volume for /data:

    docker run -d \
      -e DEBUG=true \
      -v /home/yourname/data:/data \
      --name 2buntu \
      2buntu/2buntu-django-blog

### Deploy the Container

In order to deploy the container to production, you will need to link the container to three other containers:

 * [PostgreSQL](https://registry.hub.docker.com/_/postgres/)
 * [Redis](https://registry.hub.docker.com/_/redis/)
 * [Nginx](https://registry.hub.docker.com/_/nginx/)

Assuming that you have two containers named `postgres` and `redis`, deploy the 2buntu container like so:

    docker run -d \
      -e DEBUG=true \
      -v /home/yourname/data:/data \
      --link postgres:postgres
      --link redis:redis
      --name 2buntu \
      2buntu/2buntu-django-blog

You will also want to explicitly set values for the following environment variables:

 * `RECAPTCHA_PUBLIC_KEY`
 * `RECAPTCHA_PRIVATE_KEY`
 * `TWITTER_TOKEN`
 * `TWITTER_TOKEN_SECRET`
 * `TWITTER_CONSUMER_KEY`
 * `TWITTER_CONSUMER_SECRET`
 * `SECRET_KEY`
