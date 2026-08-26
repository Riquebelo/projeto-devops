from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/products")
def products():
    with open("app/produtos.json", "r", encoding="utf-8") as file:
        products = json.load(file)

    return jsonify(products)
