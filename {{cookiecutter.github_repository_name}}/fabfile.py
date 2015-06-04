import os
import random
import string

from fabric.api import env, local, require, lcd
from fabric.colors import cyan
from fabric.operations import prompt

current_dir = os.getcwd()
env.project_name = '{{cookiecutter.app_name}}'
env.environments = ['dev',
                    'qa',
                    'prod']


def serve():
    local('python {}/manage.py runserver'.format(env.project_name))

def test():
    """
    Runs nose test suite
    """
    with lcd(current_dir):
        local('flake8')
        print cyan('flake8 passed!', bold=True)
        local('python {}/manage.py test '
              '--with-progressive --logging-clear-handlers'.format(env.project_name))

def init():
    """
    Initializes repository by configuring Travis and deploying servers
    """
    print cyan('Initializing...', bold=True)
    set_remotes()
    ask_for_aws_keys()
    for environment in env.environments:
        env.environment = environment
        env.server_name = '{}-{}'.format(env.project_name, env.environment)
        create_standard_server()
    deploy_docs()


def set_remotes():
    """
    Sets git remotes based on project structure
    """
    require('project_name')
    print cyan('Setting git remotes...')

    local('git remote add dev git@heroku.com:{}-dev.git'.format(env.project_name))
    local('git remote add qa git@heroku.com:{}-qa.git'.format(env.project_name))
    local('git remote add prod git@heroku.com:{}-prod.git'.format(env.project_name))

def ask_for_aws_keys():
    """
    Gets AWS keys from user
    """
    env.aws_access = prompt('AWS_ACCESS_KEY_ID?')
    env.aws_secret = prompt('AWS_SECRET_ACCESS_KEY?')

def create_standard_server():
    """
    Creates a sever with a standard build
    """
    create_server()
    configure_sever()
    push()
    migrate()
    create_superuser()
    open_heroku()


def create_server():
    """
    Creates a new server on heroku
    """
    require('environment')
    require('project_name')

    print cyan('Creating new server'.format(env.project_name, env.environment))
    require('environment')
    local('heroku create {}-{} --buildpack https://github.com/heroku/heroku-buildpack-python'
          .format(env.project_name, env.environment))


def configure_sever():
    """
    Configures server with a general configuration
    """
    require('environment')
    local('heroku addons:create heroku-postgresql:dev --remote {}'.format(env.environment))
    local('heroku pg:backups schedule DATABASE_URL --remote {}'.format(env.environment))
    local('heroku pg:promote DATABASE_URL --remote {}'.format(env.environment))
    local('heroku addons:create redistogo:nano --remote {}'.format(env.environment))
    local('heroku addons:create zeropush:inception --remote {}'.format(env.environment))
    local('heroku config:set ZEROPUSH_AUTH_TOKEN=`heroku config:get ZEROPUSH_PROD_TOKEN --remote={0}` --remote={0}'.format(env.environment))
    local('heroku addons:create newrelic:wayne --remote {}'.format(env.environment))
    local('heroku config:set NEW_RELIC_APP_NAME="{}" --remote {}'.format(env.project_name, env.environment))
    local('heroku config:set DJANGO_CONFIGURATION=Production --remote {}'.format(env.environment))
    local('heroku config:set DJANGO_SECRET_KEY="{}" --remote {}'.format(create_secret_key(), env.environment))
    set_aws_keys()
    ps()


def deploy_docs():
    print cyan('Deploying docs...')
    local('mkdocs gh-deploy')


def push():
    print cyan('Pushing to Heroku...')
    require('environment')
    local('git push {} master:master'.format(env.environment))


def migrate():
    require('environment')
    local('heroku run python {}/manage.py migrate --remote {}'.format(env.project_name,
                                                                      env.environment))


def create_superuser():
    require('environment')
    local('heroku run python {}/manage.py '
          'createsuperuser --remote {}'.format(env.project_name, env.environment))


def ps():
    """
    Scales a web dyno on Heroku
    """
    require('environment')
    local('heroku ps:scale web=1 --remote {}'.format(env.environment))


def open_heroku():
    require('environment')
    local('heroku open --remote {}'.format(env.environment))


def set_aws_keys():
    """
    Configures S3 Keys
    """
    local('heroku config:set DJANGO_AWS_ACCESS_KEY_ID={} --remote {}'
          .format(env.aws_access, env.environment))
    local('heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY={} --remote {}'
          .format(env.aws_secret, env.environment))
    local('heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME={0}-{1} --remote {1}'
          .format(env.project_name, env.environment))


def create_secret_key():
    """
    Creates a random string of letters and numbers
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
