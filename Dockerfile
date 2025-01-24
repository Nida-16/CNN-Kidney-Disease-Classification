FROM python:3.10-slim-buster

WORKDIR /app
COPY . /app

RUN pip install -e .

EXPOSE 8080

CMD ["python3", "app.py"]