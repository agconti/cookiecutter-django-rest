# cookiecutter-django-rest
For scaffolding django apps that create the REST apis for rapdily developing mobile apps. 

## Features

- Complete [Django Rest Framework](http://www.django-rest-framework.org/) integration
- Django Rest Framework [token auth](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) configuration
- Easy push notifciation integration with [Django-pnm](http://fueled.github.io/django-push-notifications/)
- Easy async queing with [django-rq](https://github.com/ui/django-rq)
- Configured for deploying to [Heroku](www.heroku.com)
- Monitoring with [New Relic](http://newrelic.com/)
- Docs with [mkdocs](http://www.mkdocs.org/)
- Testing with [django-nose](https://github.com/django-nose/django-nose) and fixtures via [factory-boy](http://factoryboy.readthedocs.org/en/latest/orms.html)
- Easy debugging with [ipython](http://ipython.org/) and [ipdb](https://pypi.python.org/pypi/ipdb)
- Style Enforcement via [flake8](https://flake8.readthedocs.org/en/2.3.0/)
- [Travis](https://travis-ci.org/) config
- Fabfile for easily setting up servers

# Installation
```bash
pip install cookiecutter
```

# To Scaffold
```
cookiecutter gh:agconti/cookiecutter-django-rest
```

