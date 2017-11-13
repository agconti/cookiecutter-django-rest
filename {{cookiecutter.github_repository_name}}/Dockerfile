FROM python:3.6
ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements
RUN pip install -r /requirements/main.txt
COPY . /code/

EXPOSE 8000

WORKDIR /code
CMD ["python", "./{{cookiecutter.app_name}}/manage.py", "migrate"]
CMD ["python", "./{{cookiecutter.app_name}}/manage.py", "runserver", "0.0.0.0:8000"]
