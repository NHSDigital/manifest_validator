FROM python:3

COPY . /app

RUN pip install --upgrade pip setuptools
RUN pip install poetry

WORKDIR /app

RUN poetry install
CMD ["poetry", "run", "python"m
