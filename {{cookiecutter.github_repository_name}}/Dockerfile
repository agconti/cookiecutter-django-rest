FROM python:3.12-slim as base
FROM base as builder

# Allows docker to cache installed dependencies between builds
RUN apt-get update && apt-get -y install libpq-dev gcc
COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --target=packages -r requirements.txt

FROM base as runtime
COPY --from=builder packages /usr/lib/python3.12/site-packages
ENV PYTHONPATH=/usr/lib/python3.12/site-packages

# Security Context 
RUN useradd -m nonroot
USER nonroot

COPY . code
WORKDIR code

EXPOSE 8000
# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - {{cookiecutter.app_name}}.wsgi:application
