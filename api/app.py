import time
import psycopg2
from psycopg2 import OperationalError
import sqlite3

def wait_for_db():
    while True:
        try:
            # Пробуем подключиться к базе данных
            conn = psycopg2.connect(
                host="db",
                port="5432",
                dbname="orders_db",
                user="postgres",
                password="secret"
            )
            conn.close()  # Закрываем соединение, если оно успешно
            break  # Выход из цикла, если подключение успешно
        except OperationalError:
            print("Waiting for database to be ready...")
            time.sleep(5)

# Вызовем функцию ожидания перед основным кодом
wait_for_db()

LOGGING_URL = "http://logging-service:5044/log"

DB_PATH = '/data/orders.db'

def log_event(event, status):
    payload = {"event": event, "status": status}
    try:
        requests.post(LOGGING_URL, json=payload)
    except Exception as e:
        print(f"Failed to log event: {e}")

# Ваш основной код
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# Подключение к базе данных
db_conn = psycopg2.connect(
    host="db",
    port="5432",
    dbname="orders_db",
    user="postgres",
    password="secret"
)
cursor = db_conn.cursor()

@app.route('/order', methods=['POST'])
def create_order():
    log_event("Order processing started", "info")
    data = request.json
    cursor.execute(
        "INSERT INTO orders (user_id, product_id, amount, status) VALUES (%s, %s, %s, %s)",
        (data['user_id'], data['product_id'], data['amount'], 'pending')
    )
    db_conn.commit()
    log_event("Order created successfully", "success")
    return jsonify({"message": "Order created successfully!"}), 200

@app.route('/orders', methods=['GET'])
def get_orders():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return jsonify(orders)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)

