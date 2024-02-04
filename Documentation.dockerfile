FROM python:3.10
LABEL authors="nergan"

WORKDIR /app
COPY . .

RUN pip install .[dev]
RUN sphinx-apidoc -o docs nerfw/

WORKDIR /app/docs
RUN make html
