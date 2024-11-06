#!/usr/bin/python3
"""Flask application for Techium website."""
from flask import Flask, render_template
import json



app = Flask(__name__)

@app.route('/')
def home():
    """Home page route."""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page route."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact page route."""
    return render_template('contact.html')

@app.route('/items')
def items():
    """Items page route."""
    with open('items.json', 'r') as file:
        data = json.load(file)
        items_list = data['items']
    return render_template('items.html', items=items_list)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
