FROM python:3.12-slim

WORKDIR /app

COPY app.py .

ENV VERSION=v4

EXPOSE 8080

USER 1000

CMD ["python", "app.py"]
