#!/usr/bin/python3
""" flasl module """

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
    """print output"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """print output"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """print output"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    """set port and host"""
    app.run(host='0.0.0.0', port=5000)
