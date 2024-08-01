#!/usr/bin/python3
"""7-states_list module"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """cities_by_states: display a HTML with the state and all its cities"""
    states = storage.all(State)
    cities = storage.all(City)

    return render_template(
            '8-cities_by_states.html',
            state_obj=state_obj,
            city_obj=city_obj
            )


@app.teardown_appcontext
def teardown_db(exception):
    """To remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
