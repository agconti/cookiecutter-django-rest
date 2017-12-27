<p align="center">
  <div style="background: linear-gradient(325deg, #4203DA, #FF04AD); border-radius: 50%; width: 64px; height: 64px; margin: 0 auto;"></div>
  <h3 align="center">cookiecutter-django-rest</h3>
  <p align="center">A factory for building bleeding edge, best practiced, scalable, apis<p>
  <p align="center">
    <a href="https://travis-ci.org/agconti/cookiecutter-django-rest">
      <img src="https://travis-ci.org/agconti/cookiecutter-django-rest.svg?branch=master" alt="Build Status">
    </a>
    <a href="https://pyup.io/repos/github/agconti/cookiecutter-django-rest/">
      <img src="https://pyup.io/repos/github/agconti/cookiecutter-django-rest/shield.svg" alt="Dependencies">
    </a>
    <a href="https://pyup.io/repos/github/agconti/cookiecutter-django-rest/">
      <img src="https://pyup.io/repos/github/agconti/cookiecutter-django-rest/python-3-shield.svg" alt="Python 3">
    </a>
  </p>
</p>

You need to make a scalable api on a deadline. You deeply care about the quality of your work.
`cookiecutter-django-rest` takes care of the details so you can focus on making your api awesome.  Scaffolding a project takes seconds and it gives you authentication, user accounts, and the docs and tests to support them. Just add your own resources to the api and start shipping. ✨ 💅



## Highlights
- Modern Python development with Python 3.6+
- Bleeding edge Django 1.11+
- Fully dockerized, local development via docker-compose.
- PostgreSQL 9.6+
- Start off with 100% test coverage, continuous integration, and continuous deployment.
- Complete [Django Rest Framework](http://www.django-rest-framework.org/) integration
- Auto deployment to heroku, but since we're using containers we can easily deploy anywhere
- Always current dependencies and security updates, via [pyup.io](https://pyup.io/)
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

Example of the result: https://github.com/agconti/piedpiper-web

Try creating a user!

```bash
curl -d '{"username":"testuser", "password":"test", "email":"test@test.com", "first_name":"test", "last_name":"user"}' \
     -H "Content-Type: application/json" \
     -X POST https://piedpiper-prod.herokuapp.com/api/v1/users/
```
