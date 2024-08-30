FROM python:3.12-alpine as base
FROM base as builder

RUN mkdir /install
WORKDIR /install

# Allows docker to cache installed dependencies between builds
COPY requirements.txt /requirements.txt
RUN pip install --config-settings="--prefix=/install" -r /requirements.txt

FROM base as runtime
COPY --from=builder /install /usr/local
COPY . code
WORKDIR code

EXPOSE 8000
# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - {{cookiecutter.app_name}}.wsgi:applicatio
