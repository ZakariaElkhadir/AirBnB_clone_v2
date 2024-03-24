#!/usr/bin/python3
"""flask module"""
from flask import Flask, render_template

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

@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("python/<text>", strict_slashes=False)
def python_route(text):
    """print output"""
    return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """print output"""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """print output"""
    return render_template('5-number.html', number=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """print output"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', number=n, odd_even="even")
    else:
        return render_template('6-number_odd_or_even.html', number=n, odd_even="odd")


if __name__ == "__main__":
    """set port and host"""
    app.run(host='0.0.0.0', port=5000)
