#{{cookiecutter.github_repository_name}}
{{cookiecutter.description}}. Check out the project's [documentation](http://{{cookiecutter.github_username}}.github.io/{{cookiecutter.github_repository_name}}/).

# Prerequisites 
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](http://www.postgresql.org/)
- [travis cli](http://blog.travis-ci.com/2013-01-14-new-client/)
- [heroku toolbelt](https://toolbelt.heroku.com/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements/local.txt
```
Create the database:

```bash
createdb {{cookiecutter.app_name}}
```

Migrate, create a superuser, and run the server:
```bash
python {{cookiecutter.app_name}}/manage.py migrate
python {{cookiecutter.app_name}}/manage.py createsuperuse
python {{cookiecutter.app_name}}/manage.py runserver
```

# Create Servers
By default the included fabfile will setup three environments:

- dev -- The bleeding edge of development
- qa -- For quality assurance testing
- prod -- For the live application

Create these servers on Heroku with:

```bash
fab init
```

# Automated Deployment
Deployment is handled via Travis. When builds pass Travis will automatically deploy that branch to Heroku. Enable this with:
```bash
travis setup heroku
```
