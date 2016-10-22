#{{cookiecutter.github_repository_name}}
[![Build Status](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}})

{{cookiecutter.description}}. Check out the project's [documentation](http://{{cookiecutter.github_username}}.github.io/{{cookiecutter.github_repository_name}}/).

# Prerequisites
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](http://www.postgresql.org/)
- [redis](http://redis.io/)
- [travis cli](http://blog.travis-ci.com/2013-01-14-new-client/)
- [heroku toolbelt](https://toolbelt.heroku.com/)

# Initialize the project

Initialize the git repository

```bash
git init
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}.git
```

Build the docker containers for development

```bash
docker-compose -f local.yml build
```

Start the for local development

```bash
docker-compose -f local.yml up
```

Migrate the database and create a superuser:
```bash
docker run web {{cookiecutter.app_name}}/manage.py migrate
docker run web {{cookiecutter.app_name}}/manage.py createsuperuser
```


# Automated Deployment
Deployment is handled via Travis. When builds pass Travis will automatically deploy that branch to Heroku. Enable this with:
```bash
travis encrypt $(heroku auth:token) --add deploy.api_key
```
