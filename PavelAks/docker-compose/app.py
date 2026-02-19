import os
from flask import Flask, request

app = Flask(__name__)

PORT = int(os.environ.get("PORT", 5000))
PONG_MESSAGE = os.environ.get("Hello_MESSAGE", "Standart Hello")

@app.route("/ping")
def ping():
    return PONG_MESSAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
