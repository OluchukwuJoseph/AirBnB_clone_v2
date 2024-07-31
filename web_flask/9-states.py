#!/usr/bin/python3
"""
This script starts a Flask web application with /states and /states/<id> routes
"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Displays a HTML with all States"""
    states = storage.all(State)

    return render_template('9-states.html', states=states, found=True)


@app.route('/states/<id>', strict_slashes=False)
def cities_of_state(id):
    """Displays HTML with all cities linked to state id"""
    state_objs = storage.all(State)

    key = f"State.{id}"
    if key in state_objs:
        state = state_objs[key]
        found = True
    else:
        found = False
        state = ""

    cities = []
    city_objs = storage.all(City).values()

    for city in city_objs:
        if city.state_id == id:
            cities.append(city)

    return render_template('9-states.html', cities=cities,
                           found=found, state=state)


@app.teardown_appcontext
def teardown(self):
    """Method to remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
