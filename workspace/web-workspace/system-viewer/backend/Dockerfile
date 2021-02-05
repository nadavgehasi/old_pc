FROM python:3.8.2
ENV PYTHONUNBUFFERED 1

RUN mkdir /myapp
WORKDIR /myapp
RUN mkdir database

RUN pip install poetry
COPY requirements.txt pyproject.toml poetry.lock /myapp/

RUN poetry install --no-root
RUN poetry run pip install -r requirements.txt

COPY . .
#RUN poetry install

EXPOSE 8000

ENTRYPOINT ["/myapp/run.sh"]

CMD ["poetry", "run", "python", "manage.py", "runserver", "0:8000"]
