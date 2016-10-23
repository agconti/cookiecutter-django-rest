FROM python:2.7
ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements
RUN pip install -r /requirements/main.txt
COPY . /code/

WORKDIR /code

EXPOSE 6379
