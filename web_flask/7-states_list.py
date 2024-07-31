#!/usr/bin/python3
"""This script starts a Flask web application with /states_list route"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """This function will be executed when /states_list is queryed"""
    states = storage.all(State)

    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def app_teardown(self):
    """Method to remove current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
