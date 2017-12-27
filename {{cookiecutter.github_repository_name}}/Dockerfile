FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Adds our application code to the image
COPY . /code/
WORKDIR /code

EXPOSE 8000

# Migrates the database, uploads staticfiles, and runs the production server
CMD manage.py migrate && \
    manage.py collectstatic --noinput && \
    newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT  --log-file - {{cookiecutter.app_name}}.wsgi:application
