#!/usr/bin/python3

"""Starts a Flask web application"""
import os
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Displays a HTML page with a list of states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """displays a HTML page with a list of states"""
    states = storage.all(State)
    cities = storage.all(City)
    return render_template(
        '9-states.html', states=states, cities=cities, id=id)


@app.teardown_appcontext
def closer(exception):
    """Closes the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
