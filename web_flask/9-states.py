#!/usr/bin/python3
"""9-states module"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """Displays a HTML with all States or all cities linked to state id"""
    states = storage.all(State)

    if state_id is None:
        return render_template('9-states.html', states=states, found=True)

    key = f"State.{state_id}"
    if key in states.keys():
        state = states[key]
        found = True
    else:
        found = False
        state = ""

    cities = []
    city_objs = storage.all(City).values()

    for city in city_objs:
        if city.state_id == state_id:
            cities.append(city)

    return render_template('9-states.html', cities=cities,
                           found=found, state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """To remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
