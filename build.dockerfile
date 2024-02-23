FROM python:3.10
LABEL authors="nergan"

ARG PYPI_TOKEN=${PYPI_TOKEN}
ARG PYPI_USERNAME=${PYPI_USERNAME}

WORKDIR /app
COPY . .

WORKDIR /app
RUN pip install .
RUN apt-get update
RUN apt-get install -y nodejs npm

WORKDIR /app/frontend
RUN npm install
RUN npm run build

WORKDIR /app
RUN pip install .[dev]
RUN pip install --upgrade build
RUN pip install --upgrade twine

RUN python -m build
