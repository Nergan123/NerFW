FROM python:3.10
LABEL authors="nergan"

WORKDIR /app
COPY . .

RUN pip install .[dev]

WORKDIR /app/docs
RUN make html
