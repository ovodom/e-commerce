from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/products')
def get_products():
    with open('products.json') as f:
        return jsonify(json.load(f))

@app.route('/order', methods=['POST'])
def place_order():
    data = request.json
    print("Order received:", data)
    return jsonify({"message": "Order placed!"})

@app.route('/healthz')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
