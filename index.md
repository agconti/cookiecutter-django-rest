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

- Django 1.11+
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

- [0.7.0](#release-070)
- [0.6.0](#release-060)
- [0.5.0](#release-050)
- [0.4.0](#release-040)
- [0.3.0](#release-030)
- [0.2.0](#release-020)
- [0.1.0](#release-010)

#### Release 0.7.0 #327
- [x] Upgrade to Django 1.10 #328
- [x] Add auth password validators #253
- [x] Update manage.py with new django 1.10 content. #252
- [x] Update MIDDLEWARE_CLASSES setting to MIDDLEWARE #209
- [x] Update to Django 1.10 logging configuration #208
- [x] Update mkdocs to 0.16.1 #334
- [x] Update gevent to 1.2.0 #336
- [x] Update coverage to 4.3 #339
- [x] Update coverage to 4.3.1 #341
- [x]  Remove django-secure #356
- [x] Update gevent to 1.2.1 [#360](https://github.com/agconti/cookiecutter-django-rest/issues/360)
- [x] Update newrelic to 2.78.0.57 [#353](https://github.com/agconti/cookiecutter-django-rest/issues/353)
- [x] Update whitenoise to 3.2.3 [#352](https://github.com/agconti/cookiecutter-django-rest/issues/352)
- [x] Update django to 1.10.5  [#351](https://github.com/agconti/cookiecutter-django-rest/issues/351)
- [x] Update newrelic to 2.78.0.57 [#350](https://github.com/agconti/cookiecutter-django-rest/issues/350)
- [x] Update dj-database-url to 0.4.2 [#349](https://github.com/agconti/cookiecutter-django-rest/issues/349)
- [x] Update django-model-utils to 2.6.1 [#348](https://github.com/agconti/cookiecutter-django-rest/issues/348)
- [x] Import Error [#337](https://github.com/agconti/cookiecutter-django-rest/issues/337)
- [x] Update whitenoise to 3.3.0 [#363](https://github.com/agconti/cookiecutter-django-rest/issues/363)
- [x] Update markdown to 2.6.8 [#362](https://github.com/agconti/cookiecutter-django-rest/issues/362)
- [x] Update ipdb to 0.10.2 [#361](https://github.com/agconti/cookiecutter-django-rest/issues/361)
- [x] Update djangorestframework to 3.5.4 [#372](https://github.com/agconti/cookiecutter-django-rest/issues/372)
- [x] Update flake8 to 3.3.0 [#371](https://github.com/agconti/cookiecutter-django-rest/issues/371)
- [x] Update ipython to 5.2.2 [#369](https://github.com/agconti/cookiecutter-django-rest/issues/369)
- [x] Update djangorestframework to 3.5.4 [#374](https://github.com/agconti/cookiecutter-django-rest/issues/374)
- [x] Update flake8 to 3.3.0 [#373](https://github.com/agconti/cookiecutter-django-rest/issues/373)
- [x] Update django-versatileimagefield to 1.6.3 #376
- [x] Update boto to 2.46.1 #379
- [x] Staticfiles dirs is a list of lists #386
- [x] Update psycopg2 to 2.7 [#384](https://github.com/agconti/cookiecutter-django-rest/issues/384)
- [x] Update django to 1.10.6 [#383](https://github.com/agconti/cookiecutter-django-rest/issues/383)
- [x] Update newrelic to 2.80.1.61 [#382](https://github.com/agconti/cookiecutter-django-rest/issues/382)
- [x] Update ipython to 5.3.0 [#381](https://github.com/agconti/cookiecutter-django-rest/issues/381)
- [x] Update gunicorn to 19.7.0 #387
- [x] Update django-rq to 0.9.5 #394
- [x] Update newrelic to 2.82.0.62 #395
- [x] Update mkdocs to 0.16.2 #393
- [x] Update psycopg2 to 2.7.1 #392
- [x] Update djangorestframework to 3.6.2 #391
- [x] Update django-model-utils to 3.0.0 [#402](https://github.com/agconti/cookiecutter-django-rest/issues/402)
- [x] Update mkdocs to 0.16.3 [#401](https://github.com/agconti/cookiecutter-django-rest/issues/401)
- [x] Update django to 1.11 [#400](https://github.com/agconti/cookiecutter-django-rest/issues/400)
- [x] Update pytz to 2017.2 [#398](https://github.com/agconti/cookiecutter-django-rest/issues/398)
- [x] Update django-filter to 1.0.2 [#397](https://github.com/agconti/cookiecutter-django-rest/issues/397)
- [x] Update gunicorn to 19.7.1 [#396](https://github.com/agconti/cookiecutter-django-rest/issues/396)
- [x] Update ipython to 6.0.0 #407- [ ] Update newrelic to 2.86.0.65 [#411](https://github.com/agconti/cookiecutter-django-rest/issues/411)
- [x] Update fabric to 1.13.2 [#409](https://github.com/agconti/cookiecutter-django-rest/issues/409)
- [x] Update ipdb to 0.10.3 [#408](https://github.com/agconti/cookiecutter-django-rest/issues/408)
- [x] Update django-versatileimagefield to 1.7.0 [#406](https://github.com/agconti/cookiecutter-django-rest/issues/406)
- [x] Update django-filter to 1.0.4 [#420](https://github.com/agconti/cookiecutter-django-rest/issues/420)
- [x] Update newrelic to 2.86.1.66 [#419](https://github.com/agconti/cookiecutter-django-rest/issues/419)
- [x] Update coverage to 4.4.1 [#417](https://github.com/agconti/cookiecutter-django-rest/issues/417)
- [x] Update djangorestframework to 3.6.3 [#415](https://github.com/agconti/cookiecutter-django-rest/issues/415)

#### Release 0.6.0 #167

- [x] Update travis badge to private repo #26
- [x] django-configuration conflicts with pycharm python console #234
- [x] Add jwt and oauth2 for third parties (social) #239
- [x] Upgrade gevent to secure version #322
- [x] Update newrelic to 2.76.0.55 #321
- [x] Update factory-boy to 2.8.1 #320
- [x] Update boto to 2.45.0 #319
- [x] Update pytz to 2016.10 #314
- [x] Update django-versatileimagefield to 1.6.2 #313
- [x] Update boto to 2.44.0 #312
- [x] Update fabric to 1.13.1 #311
- [x] Update django-filter to 1.0.1 #303
- [x] Update flake8 to 3.2.1 #302
- [x] Upgrade Django to secure version, 1.9.11 #297
- [x] Update django-versatileimagefield to 1.6.1 #296
- [x] Update flake8 to 3.2.0 #294
- [x] Update newrelic to 2.74.0.54 #293
- [x] Update django-rq to 0.9.4 #288
- [x] Update mkdocs to 0.16.0
- [x] Update djangorestframework to 3.5.2 #281
- [x] Update newrelic to 2.72.1.53 #278
- [x] Update django-redis-cache to 1.7.1 #279
- [x] Add dependency caching for traivs #272
- [x] Update djangorestframework to 3.5 #275
- [x] Update newrelic to 2.72.0.52 #271
- [x] Update djangorestframework to 3.5.0 #270
- [x] Update django-rq #269
- [x] Update boto to 2.43.0 #265
- [x] Update django-filter to 0.15.3 #263
- [x] Update pytz to 2016.7 #261
- [x] Update django-filter to 0.15.2
- [x] Update whitenoise to 3.2.2
- [x] Update django-model-utils to 2.6
- [x] Update django-filter to 0.15.0
- [x] Update djangorestframework to 3.4.7
- [x] Update markdown to 2.6.7
- [x] Update newrelic to 2.70.0.51 #240
- [x] Update djangorestframework to 3.4.6 #237
- [x] Update django-redis-cache to 1.7.0 #232
- [x] Update djangorestframework to 3.4.5 #231
- [x] Update django-filter to 0.14.0 #228
- [x] Update ipython to 5.1.0 #229
- [x] Update django-model-utils to 2.5.2 #223
- [x] Update whitenoise to 3.2.1 #222
- [x] Update flake8 to 3.0.4 #219
- [x] Update django-rq to 0.9.2
- [x] Update djangorestframework to 3.4.3 #215
- [x] Update django-model-utils to 2.5.1 #213
- [x] Update djangorestframework to 3.4.2 #212
- [x] Move pyup badge to top level readme #201
- [x] Limit default pagination size to 10 #191
- [x] Update logging config to match django 1.9 changes #190
- [x] Add pyup for easy dependency management. #189
- [x] Set django storages default acl to public read #188
- [x] Update IsOwnerOrReadOnly to IsUserOrReadOnly #187
- [x] Add RQ_SHOW_ADMIN_LINK to true in config/common #186
- [x] Add `created_on_demand` versatile image field to True for local development #185
- [x] Upgrade to DRF 3.4 #184
- [x] Error when running migrate command on Azure VM #181
- [x] Update users serializer for new write only field syntax #183
- [x] Upgrade Django 1.9.7 #180
- [x] Update `IsOwnerOrReadOnly` permission docstring to be more clear #178
- [x] Upgrade `django-redis-cache` to `v1.6.5` #173
- [x] Update `/users` documentation. #172
- [x] Update language in README overview #168
- [x] Add push notifications to features list  [#123](https://api.github.com/repos/agconti/cookiecutter-django-rest/issues/123) [[ Decided against implementing ]](https://github.com/agconti/cookiecutter-django-rest/issues/122#issuecomment-205048991)
- [x] Implement `django-push-notifications` over django-pnm [#122](https://api.github.com/repos/agconti/cookiecutter-django-rest/issues/122) [[ Decided against implementing ]](https://github.com/agconti/cookiecutter-django-rest/issues/122#issuecomment-205048991)
- [x] Upgrade auth to use jwt [#21](https://api.github.com/repos/agconti/cookiecutter-django-rest/issues/21) [[ Decided against implementing ]](https://github.com/agconti/cookiecutter-django-rest/pull/146#issuecomment-205039612)
- [x] Update dependencies #175
- [x] Add ia diagram that details the scaffolded server's structure to docs [#119](https://api.github.com/repos/agconti/cookiecutter-django-rest/issues/119)
- [x] Evaluate heroku redis as a replacement for Redis To Go [#99](https://api.github.com/repos/agconti/cookiecutter-django-rest/issues/99)
- [x] Evaluate django-q to replace django-rq [#59](https://api.github.com/repos/agconti/cookiecutter-django-rest/issues/59)
- [x] Update travis badge to private repo [#26](https://api.github.com/repos/agconti/cookiecutter-django-rest/issues/26)

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
