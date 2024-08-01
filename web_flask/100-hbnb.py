#!/usr/bin/python3
"""
This script starts a Flask web application with /hbnb routes
"""
from flask import Flask, render_template
from models import *

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays a HTML page with State, Cities, Places, and Amenities"""
    states = storage.all(State)

    amenities = storage.all(Amenity)

    places = storage.all(Place)

    return render_template('100-hbnb.html', states=states, places=places,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    """Method to remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
