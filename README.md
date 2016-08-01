# cookiecutter-django-rest
[![Build Status](https://travis-ci.org/agconti/cookiecutter-django-rest.svg?branch=docs-project-readme-travis)](https://travis-ci.org/agconti/cookiecutter-django-rest)
[![Updates](https://pyup.io/repos/github/agconti/cookiecutter-django-rest/shield.svg)](https://pyup.io/repos/github/agconti/cookiecutter-django-rest/)

For creating REST apis for mobile and web applications.

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Features](#features)
- [Contributing](#contributing)

## Overview
This cookiecutter template takes care of the setup and configuration so you can focus on making your api awesome. Scaffolding a project takes seconds and it gives you authentication, user accounts, and the docs and tests to support them. After that, just add your own resources to the api and start shipping.

This project gives you a solid foundation for your api to mature by baking in things like asynchronous queueing, image optimization, and application monitoring.

### What you'll be building

![ia diagram](https://cdn.rawgit.com/agconti/cookiecutter-django-rest/master/media/ia-diagram.svg)

## Quick Start

Install [cookiecutter](https://github.com/audreyr/cookiecutter):
```bash
pip install cookiecutter
```

Scaffold your project:
```
cookiecutter gh:agconti/cookiecutter-django-rest
```

![Scaffolding](media/scaffolding.gif)

Example of the result: https://github.com/agconti/piedpiper-web

## Features

- Django 1.9+
- PostgreSQL
- Complete [Django Rest Framework](http://www.django-rest-framework.org/) integration
- Configured for deploying to [Heroku](https://www.heroku.com)
- Asset storage via [S3](https://github.com/jschneier/django-storages)
- Class based settings and safe environmental variable management via [django-configurations](https://github.com/jazzband/django-configurations)
- [Travis](https://travis-ci.org/) config
- Monitoring with [New Relic](http://newrelic.com/)
- [Token authentication](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
- Docs with [mkdocs](http://www.mkdocs.org/)
- Testing with [django-nose](https://github.com/django-nose/django-nose) and fixtures via [factory-boy](http://factoryboy.readthedocs.org/en/latest/orms.html)
- Caching with Redis via [Django Redis](https://github.com/niwinz/django-redis)
- Easy debugging with [ipython](http://ipython.org/) and [ipdb](https://pypi.python.org/pypi/ipdb)
- Style Enforcement via [flake8](https://flake8.readthedocs.org/en/2.3.0/)
- Fabfile for easily setting up servers

## Contributing
Want a new feature? Open an issue and let's chat!
Find a bug? Submit a Pull Request!

This project adheres to the [Contributor Code of Conduct](.github/CONTRIBUTING.md).
