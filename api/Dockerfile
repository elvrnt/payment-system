FROM python:3.9-slim

WORKDIR /app

# Установите системные библиотеки, необходимые для компиляции psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY app.py .

# Установка Python-зависимостей
RUN pip install flask requests psycopg2

EXPOSE 8000

CMD ["python", "app.py"]
