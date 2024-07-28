#!/usr/bin/python3
"""
This script starts a Flask web application with '/', '/hbnb', '/c/<text>',
'/python/<text>', '/number/<n>' and /number_template/<n> route.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """This function is executed when / route is queryed"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """This function is executed when /hbnb route is queryed"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """This function is executed when /c/<text> route is queryed"""
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """This function is executed when /python/<text> route is queryed"""
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """This function is executed when /number/<n> route is queryed"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """This function is executed when /number_template/<n> route is queryed"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_od_or_even(n):
    """To be executed when /number_odd_or_even/<n> route is queryed"""
    if n % 2 == 0:
        num_type = "even"
    else:
        num_type = "odd"

    return render_template("6-number_odd_or_even.html", n=n, num_type=num_type)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
