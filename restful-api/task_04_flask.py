#!/usr/bin/python3
''' Module that implements a simple API '''

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {}


@app.route('/')
def home():
    """
    Home route that welcomes users to the Flask API.

    Returns:
        str: A welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/clear_users')
def clear_users():
    """
    Clears all users from the users dictionary.

    Returns:
        tuple: A JSON response confirming the action and a 200 status code.
    """
    global users
    users.clear()
    return jsonify({"message": "All users cleared"}), 200


@app.route('/data')
def data():
    """
    Retrieves a list of all usernames in the users dictionary.

    Returns:
        Response: A JSON array of usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Provides a simple status check for the API.

    Returns:
        str: "OK" if the API is running.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Retrieves user information for a specific username.

    Args:
        username (str): The username to look up.

    Returns:
        tuple: A JSON response with user data if found,
        or an error message and 404 status if not found.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user to the users dictionary.

    Expects a JSON payload with user information including a 'username' field.

    Returns:
        tuple: A JSON response confirming the addition
        with user data and 201 status, or an error message
        with 400 status if the request is invalid.
    """
    new_user = request.get_json()
    if not new_user or 'username' not in new_user:
        return jsonify({"error": "Username is required"}), 400

    username = new_user['username']
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = new_user
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == '__main__':
    app.run()
