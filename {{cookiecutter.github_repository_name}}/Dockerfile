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
CMD ./{{cookiecutter.app_name}}/manage.py migrate && \
    ./{{cookiecutter.app_name}}/manage.py collectstatic --noinput && \
    newrelic-admin run-program gunicorn \
    --pythonpath="./{{cookiecutter.app_name}}" \
    --bind 0.0.0.0:$PORT \
    -w 3 \
    wsgi:application
