# cookiecutter-django-rest
[![Build Status](https://travis-ci.org/agconti/cookiecutter-django-rest.svg?branch=docs-project-readme-travis)](https://travis-ci.org/agconti/cookiecutter-django-rest)
[![Updates](https://pyup.io/repos/github/agconti/cookiecutter-django-rest/shield.svg)](https://pyup.io/repos/github/agconti/cookiecutter-django-rest/)

For creating REST apis for mobile and web applications.

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Features](#features)
- [Contributing](#contributing)
- [Release Notes](#release-notes)

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

![Scaffolding](https://cdn.rawgit.com/agconti/cookiecutter-django-rest/master/media/scaffolding.gif)

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

## Release notes 

- [0.5.0](#release-050)
- [0.4.0](#release-040)
- [0.3.0](#release-030)
- [0.2.0](#release-020)
- [0.1.0](#release-010)

#### Release 0.5.0
- [x] Remove duplicate append slash setting in `config/common` #162
- [x] Add .github folder and include issue and pull request templates #160
- [x] Remove django sites configuration since its not needed for rest apis #161
- [x] Update django template loaders settings #158
- [x] Scale heroku dynos to hobby tier #157
- [x] Add django-unique-upload for unique uploads with uuids #154
- [x] Set versatile image's field to 'create_images_on_demand' to false in production by default. #153
- [x] boto not add the Signature and Key to #152 
- [x] Set APPEND_SLASH to False #149

#### Release 0.4.0
- [x] Updated drf page number pagination settings #145
- [x] Upgrade user model `pk`s to `uuids` [#65](https://api.github.com/repos/agconti/cookiecutter-django-rest/issues/65)
- [x] For connivence, separate runserver from createsuperuser  [#140](https://api.github.com/repos/agconti/cookiecutter-django-rest/issues/140)
- [x] Add @python_2_unicode_compatible to models [#139](https://api.github.com/repos/agconti/cookiecutter-django-rest/issues/139)
- [x] Remove zeropush config from fab init #138
- [x] Use standard django-configurations once it releases `0.9` #63
- [x] Refactor settings to use Django class based settings instead of Django Configurations #118
- [x] Add .editorconfig file #101
- [x] Update dependencies #129
- [x] django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet #131
- [x] Heroku link is broken in ReadMe #135
- [x] Add django configurations to features list #133

#### Release 0.3.0
- [x] Add travis badge to project readme #110
- [x] Allow for python 3 support for urlparse #113
- [x] Change to `api-root` from 301 to 302 #115 
- [x] Upgrade to factory boy 2.6 #117
- [x] Add django 1.8 security middleware to common.py #121
- [x] Upgrade to Django 1.9 #124
- [x] Remove Django-pnm #126

#### Release 0.2.0

- Update heroku postgresql addon config #98
- Fix fabfile spacing #103
- Do super() in test case of users #106
- Remove auth_token from UserSerializer #104
- Set up automated testing via travis #107

#### Release 0.1.0
- Update users app with the appropriate test cases #1 
- Add api docs for user app #2
- add tests for auth tokens #43
- Add api docs for auth #3 
- Add django-storages-redux config to production. #6
- Handle "/" routing #7
- add redis to app readme prerequisites. #9
- Upgrade mkdocs to 0.14.0 #10 
- Add `git init` to project ReadMe #17
- Update pg backups with schedule time #18
- Migrate the database after deploys #19
- add fab dev and qa tasks back in #20
- Update docs index to include readme #27
- Update flake8 fab task to target project dir #30
- Exclude migrations from flake8 #31
- Configure nosetests arguments #32 
- Update flake8 to allow for easy debugging #37
- Add faker for mocking #41
- Remove email notifications from travis #48
- Update cookie cutter params to specify username / **organization name** #47
- Add github username to heroku repo deploy #46
- Update app routing to use a single DefaultRouter #45
- Exclude mkdocs site dir via gitignore #52
- Update django-pnm to 0.1.5 #54
- Update Authentication docs to include obtain `auth_token` endpoint #56
- Add caching via django-redis to features list #58
- Update ReadMe with more detailed background on project #60
- Upgrade to Django 1.8 after django-configurations has been upgraded. #8
- Add gif of scaffolding to ReadMe #66 
- Fix broken heroku run command #71 
- Database values are not set in Travis file #69
- Running ./manage.py test will result in "Coverage.py warning: Module walc was never imported." #67
- Tests should have `--nologcapture` added to the NOSE_ARGS #77
- Add `contributing.md` #74
- RelatedObjectDoesNotExist: User has no auth_token. #75
- Configure Django template debug settings #82
- Update to DRF 3.2.3 #81
- Update to Django 1.8.4 #80
- Upgrade Django-pnm to 1.6 #86
- Update `RedirectView.permanent` to true for `api-root` route #90
- Upgrade dependencies #89 
- Update `.travis` postgres config #88
- Add `.coveragerc` #73
