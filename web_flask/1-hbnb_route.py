#!/usr/bin/python3
"""flask module"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
@app.route("/hbnb", strict_slashes=False)
def hello():
    """print output"""
    return "Hello HBNB!"

def hbnb():
    """print output"""
    return "HBNB"


if __name__ == "__main__":
    """set port and host"""
    app.run(host='8.8.8.8', port=5000)
