"""A tiny Flask service that validates and echoes user payloads."""

from flask import Flask, jsonify, request

from src.models import User

app = Flask(__name__)


@app.post("/users")
def create_user():
    user = User(**request.get_json(force=True))
    return jsonify(user.as_payload()), 201


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
