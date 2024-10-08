#!/usr/bin/python3
''' Module that implements a simple API '''

from flask import Flask, jsonify, request

app = Flask(__name__)


users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    return jsonify([user['username'] for user in users.values()])


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
    new_user = request.form.to_dict() if request.form else request.json
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
    app.run(debug=True)
