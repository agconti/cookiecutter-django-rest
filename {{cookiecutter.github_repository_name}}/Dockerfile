FROM python:3.6
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /code/
WORKDIR /code

EXPOSE 8000
