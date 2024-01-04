FROM python:3.10
LABEL authors="nergan"

RUN apt-get update
RUN pip install pytest requests

WORKDIR /app
COPY . .

EXPOSE 5000

CMD ["pytest", "-v", "-s"]