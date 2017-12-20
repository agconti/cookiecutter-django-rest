# {{cookiecutter.github_repository_name}}

[![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}})
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

{{cookiecutter.description}}. Check out the project's [documentation](http://{{cookiecutter.github_username}}.github.io/{{cookiecutter.github_repository_name}}/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  
- [Travis CLI](http://blog.travis-ci.com/2013-01-14-new-client/)
- [Heroku Toolbelt](https://toolbelt.heroku.com/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run -rm web ./viral/manage.py createsuperuser
```


# Continuous Deployment

Deployment automated via Travis. When builds pass on the master or qa branch, Travis will deploy that branch to Heroku. Enable this by:

Create the production and qa servers:

Click the deploy button and name your app `{{cookiecutter.app_name}}-prod`:

[![Create Prod](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/agconti/cdr-docker)

Click the deploy button and name your app `{{cookiecutter.app_name}}-qa`:

[![Create QA](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/agconti/cdr-docker)

Securely add your heroku credentials to travis so it can automatically deploy your changes.
```bash
travis encrypt HEROKU_AUTH_TOKEN="$(heroku auth:token)" --add
```

You're ready to ship! ✨ 💅 🛳
