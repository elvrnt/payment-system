FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install flask

EXPOSE 3000

CMD ["python3", "app.py"]
