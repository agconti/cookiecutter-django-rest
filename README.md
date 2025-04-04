<p align="center">
  <img width="64" style="border-radius:64px;" src="media/cdr-icon.png" alt="cookiecutter-django-rest">
  <h3 align="center">cookiecutter-django-rest</h3>
  <p align="center">a factory for building bleeding edge, best practiced, scalable, rest apis</p>
  <p align="center">
    <a href="https://github.com/agconti/cookiecutter-django-rest/actions/workflows/push.yaml">
      <img src="https://github.com/agconti/cookiecutter-django-rest/actions/workflows/push.yaml/badge.svg?branch=master" alt="Build Status">
    </a>
  </p>
</p>

You need to make a scalable api on a deadline. You deeply care about the quality of your work.
`cookiecutter-django-rest` takes care of the details so you can focus on making your api awesome.  Scaffolding a project takes seconds and it gives you [authentication](https://github.com/agconti/cookiecutter-django-rest/blob/master/%7B%7Bcookiecutter.github_repository_name%7D%7D/docs/api/authentication.md), [user accounts](https://github.com/agconti/cookiecutter-django-rest/blob/master/%7B%7Bcookiecutter.github_repository_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/users/views.py), and the [docs](https://github.com/agconti/cookiecutter-django-rest/blob/master/%7B%7Bcookiecutter.github_repository_name%7D%7D/docs/api/users.md) and [tests](https://github.com/agconti/cookiecutter-django-rest/blob/master/%7B%7Bcookiecutter.github_repository_name%7D%7D/%7B%7Bcookiecutter.app_name%7D%7D/users/test/test_views.py) to support them. Just add your own resources to the api and start shipping. ✨ 💅

## Highlights
- Modern Python development with Python 3.13+
- Bleeding edge Django 5.0+
- Fully dockerized, local development via docker-compose.
- PostgreSQL 16.4+
- Start off with full test coverage and [continuous integration](https://github.com/agconti/cookiecutter-django-rest/blob/master/%7B%7Bcookiecutter.github_repository_name%7D%7D/.travis.yml).
- Complete [Django Rest Framework](http://www.django-rest-framework.org/) integration
- Always current dependencies and security updates enforced by [pyup.io](https://pyup.io/).
- A slim but robust foundation -- just enough to maximize your productivity, nothing more.

## Quick Start

Install [cookiecutter](https://github.com/audreyr/cookiecutter):

```bash
brew install cookiecutter
```

Scaffold your project:
```
cookiecutter gh:agconti/cookiecutter-django-rest
```

![Scaffolding](media/scaffolding.gif)