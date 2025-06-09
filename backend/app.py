from flask import Flask, request, jsonify
import json
import psycopg2
import os

app = Flask(__name__)

# PostgreSQL config from env vars
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route('/products')
def get_products():
    with open('products.json') as f:
        return jsonify(json.load(f))

@app.route("/api/order", methods=["POST"])
def place_order():
    data = request.json
    customer = data.get("customer_name")
    product = data.get("product_name")
    quantity = data.get("quantity", 1)

    conn = get_connection()
    cur = conn.cursor()

    # Create table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY,
            customer_name TEXT,
            product_name TEXT,
            quantity INTEGER
        )
    """)

    # Insert the order
    cur.execute("""
        INSERT INTO orders (customer_name, product_name, quantity)
        VALUES (%s, %s, %s)
    """, (customer, product, quantity))

    conn.commit()
    cur.close()
    conn.close()

    print("Order saved to DB:", data)
    return jsonify({"message": "Order placed successfully"}), 201

@app.route('/healthz')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
