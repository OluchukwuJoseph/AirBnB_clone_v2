#!/usr/bin/python3
"""
This script starts a Flask web application with '/' and '/hbnb' route
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """This function is executed when / route is queryed"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function is executed when /hbnb route is queryed"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
