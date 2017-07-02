# docker-enfetch

A tiny script to restore existing Docker containers' environmental variables to re-usable YAML config.

## Why?

Deploying an app with Docker-compose, you often split `compose`-file into several ones. Like:

```
docker-compose \
    -f docker-compose.base.yml \ <== base file with common containers config
    -f docker-compose.live.yml \ <== production-specific options
    -f docker-compose.cred.yml \ <== credentials, like passwords, AWS keys,etc
    up -d
```

File `docker-compose.cred.yml` is not commited into repository. But to update app, or deploy a new version, you need exactly the same `docker-compose.cred.yml`-file, which you initially deployed your app with.

**This small tool analyzes existing docker containers and restores original `compose` -files with environent variables.**

## Install

Just install deps:

```sh
cd <path-to-repo>
pip install -r requirements.txt
```

## Usage

Env into current docker-host // docker-mahcine profile like:

```
docker-machine env <machine-name>
eval $(docker-machine env <machine-name>)
```

After this, your docker env vars will be set (`DOCKER_TLS_VERIFY`, `DOCKER_HOST`, `DOCKER_CERT_PATH`, `DOCKER_MACHINE_NAME`, etc).

Start docker-enfetch:

```sh
python ~/docker-enfetch/enfetch.py
```

An output wiil be like:

```yml
version: 2
services:
  db:
    environment:
      POSTGRES_PASSWORD: <filtered>
  web:
    environment:
      APP_URL: <filtered>
      DBPASS: <filtered>
      DEVISE_SECRET_KEY: <filtered>
      PORT: 80
      RACK_ENV: production
      RAILS_ENV: production
      RAILS_SERVE_STATIC_FILES: 1
      SECRET_KEY_BASE: <filtered>
```

Obviously, insted of `<filtered>` you'll get real creds from containers' env var.

So, pipe output into real file:

```sh
python ~/docker-enfetch/enfetch.py > live/docker-compose.creds.yml
```

And you'll done!

## LICENSE

(C) 2017, f1nnix, [WTFPL](https://en.wikipedia.org/wiki/WTFPL) license.
