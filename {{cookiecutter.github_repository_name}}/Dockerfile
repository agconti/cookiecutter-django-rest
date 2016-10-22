FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
ADD requirements /code/
COPY . /code/

WORKDIR /code
RUN pip install -r requirements/main.txt
