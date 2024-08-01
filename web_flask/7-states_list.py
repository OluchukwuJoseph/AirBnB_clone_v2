#!/usr/bin/python3
"""7-states_list module"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """states_list: display a HTML page: (inside the tag BODY)"""
    state_obj = storage.all(State)

    return render_template('7-states_list.html', state_obj=state_obj)


@app.teardown_appcontext
def teardown_db(exception):
    """To remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
