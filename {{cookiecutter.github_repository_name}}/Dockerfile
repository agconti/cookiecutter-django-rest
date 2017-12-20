FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Adds our application code to the image
COPY . /code/
WORKDIR /code

EXPOSE 8000

# Runs the container as a non-root user
# https://www.projectatomic.io/blog/2015/08/why-we-dont-let-non-root-users-run-docker-in-centos-fedora-or-rhel/
RUN adduser -m web
USER web


# Migrates the database and runs the production server
CMD /{{ cookiecutter.app_name }}/manage.py migrate && \
    newrelic-admin run-program gunicorn \
    --pythonpath="$PWD/{{ cookiecutter.app_name }}" \
    --bind 0.0.0.0:$PORT \
    wsgi:application
