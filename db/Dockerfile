FROM postgres:latest

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_DB=orders_db

# Копируем SQL файл для инициализации базы данных
COPY init.sql /docker-entrypoint-initdb.d/

# Контейнер PostgreSQL автоматически выполнит все SQL-скрипты в этой папке при запуске
