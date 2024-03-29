FROM python:3.10
LABEL authors="nergan"

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
RUN rm -rf tests

RUN python -m build
