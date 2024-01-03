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
CMD ["python", "main.py"]