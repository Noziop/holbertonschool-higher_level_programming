#!/usr/bin/python3
''' Module that implements a simple API '''

from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/clear_users')
def clear_users():
    global users
    users = {}
    return "Users cleared"

@app.route('/data')
def data():
    if users == {}:
        abort(404)
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.get_json(force=True)
    if not new_user or 'username' not in new_user:
        return jsonify({"error": "Username is required"}), 400
    username = new_user['username']
    if username and 'name' and 'age' and 'city' in users:
        return jsonify({"error": "Username already exists"}), 400
    users[username] = new_user
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201

if __name__ == '__main__':
    app.run(debug=True)