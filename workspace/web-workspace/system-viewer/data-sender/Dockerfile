FROM ubuntu:latest
ENV PYTHONUNBUFFERED 1

RUN mkdir /myapp
WORKDIR /myapp

RUN apt-get update
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip
RUN apt-get install -y python3.8-venv
RUN apt-get install -y cron
RUN apt-get install -y openssh-client

RUN python3.8 -m pip install poetry
COPY pyproject.toml poetry.lock /myapp/

RUN poetry install --no-root

COPY . .

RUN echo "*/2 * * * * cd /myapp/ && /usr/local/bin/poetry run python /myapp/ssh-sender.py" >> mycron
RUN crontab mycron
RUN rm mycron

ENTRYPOINT ["/myapp/run.sh"]

CMD ["bash"]