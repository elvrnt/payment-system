FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install flask

EXPOSE 4000

CMD ["python3", "app.py"]
