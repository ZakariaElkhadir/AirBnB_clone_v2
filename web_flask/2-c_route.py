#!/usr/bin/python3
"""
flask module
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """print output"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """print output"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """the space will replaced with underscore"""
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    """set port and host"""
    app.run(host='0.0.0.0', port=5000)
