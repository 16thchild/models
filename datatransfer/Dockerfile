FROM python:3.8-slim-buster

WORKDIR /src
ENV PYTHONUNBUFFERED 1

RUN \
  apt-get update -y; \
  apt-get upgrade -y ;\
  apt-get install -y \
    gcc \
    libmariadb-dev \
  ;\
  python -m pip install --upgrade pip

COPY ./pyproject.toml ./poetry.lock ./

RUN \
  pip install poetry ;\
  poetry config virtualenvs.create false ;\
  poetry install --no-dev

COPY . .

ENTRYPOINT ["./entrypoint.sh"]
