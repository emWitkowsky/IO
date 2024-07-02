import requests
from flask import Flask, jsonify, request, make_response
from flask_pymongo import PyMongo
from keycloak import KeycloakOpenID, KeycloakAdmin
from keycloak.exceptions import KeycloakError
import bcrypt
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, supports_credentials=True)

PORT = os.getenv("PORT") | 5000
DATABASE_URL = os.getenv("DATABASE_URL") | "mongodb://localhost:27017/myDatabase"

# MongoDB configuration
app.config["MONGO_URI"] = DATABASE_URL
mongo = PyMongo(app)

# Keycloak configuration
KEYCLOAK_SERVER_URL = os.getenv("KEYCLOAK_SERVER_URL") | 'http://localhost:8080/'
KEYCLOAK_REALM_NAME = os.getenv("KEYCLOAK_REALM_NAME") | 'demo-realm'
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID") | 'flask-app'
KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET") | 'FqXzK17tw7L2POkIRHFkxB5q1ajnoh3a'
KEYCLOAK_ADMIN_USERNAME = os.getenv("KEYCLOAK_ADMIN_USERNAME") | 'admin'
KEYCLOAK_ADMIN_PASSWORD = os.getenv("KEYCLOAK_ADMIN_PASSWORD") | 'admin'

# Secret key for JWT encoding/decoding
SECRET_KEY = os.getenv("SECRET_KEY") | "tajnehaslo123"

keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_SERVER_URL,
                                 realm_name=KEYCLOAK_REALM_NAME,
                                 client_id=KEYCLOAK_CLIENT_ID,
                                 client_secret_key=KEYCLOAK_CLIENT_SECRET)

keycloak_admin = KeycloakAdmin(server_url=KEYCLOAK_SERVER_URL,
                               username=KEYCLOAK_ADMIN_USERNAME,
                               password=KEYCLOAK_ADMIN_PASSWORD,
                               realm_name=KEYCLOAK_REALM_NAME,
                               verify=False)

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Check if user already exists in MongoDB
    if mongo.db.users.find_one({"username": username}):
        return jsonify({"error": "Username already exists"}), 400

    # Store user in MongoDB
    mongo.db.users.insert_one({
        "username": username,
        "password": hashed_password.decode('utf-8')
    })

    # Create user in Keycloak
    try:
        keycloak_admin.create_user(payload={
            'username': username,
            'enabled': True,
            'credentials': [{'type': 'password', 'value': password}],
            'realmRoles': ['user']
        })
    except Exception as e:
        return jsonify({"error": "Error creating user in Keycloak"}), 500

    return jsonify({"message": "User registered successfully"}), 201


# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Retrieve user from MongoDB
    user = mongo.db.users.find_one({"username": username})

    if not user:
        return jsonify({"error": "User not found"}), 404

    # Verify password
    if not bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        return jsonify({"error": "Invalid password"}), 401

    # Generate access token using Keycloak
    try:
        access_token = keycloak_openid.token(username=username, password=password)

        resp = make_response(jsonify({'username': username}))
        resp.set_cookie('token', access_token['access_token'], httponly=True, secure=True, samesite='Strict')
        resp.set_cookie('refresh_token', access_token['refresh_token'], httponly=True, secure=True, samesite='Strict')
        return resp

    except KeycloakError as e:
        return jsonify({"error": "Keycloak error"}), 500
    except Exception as e:
        return jsonify({"error": "Unexpected error"}), 500


@app.route('/hello', methods=['GET'])
def hello_user():
    token = request.cookies.get('token')
    if not token:
        return jsonify({'error': 'Not logged in'}), 401

    try:
        # Verify token with Keycloak
        userinfo = keycloak_openid.userinfo(token)

        # Extract username from userinfo response
        username = userinfo.get('preferred_username')

        if not username:
            return jsonify({"error": "Username not found in userinfo"}), 401

        # Store username in MongoDB if not already stored
        if not mongo.db.users.find_one({"username": username}):
            mongo.db.users.insert_one({"username": username})

        return jsonify({"message": f"Hello, {username}"}), 200

    except KeycloakError as e:
        return jsonify({"error": "Error while accessing userinfo"}), 401
    except Exception as e:
        return jsonify({"error": "Unexpected error"}), 500


@app.route('/refresh_token', methods=['POST'])
def refresh_token():
    refresh_token = request.cookies.get('refresh_token')
    if not refresh_token:
        return jsonify({'error': 'Refresh token missing'}), 401

    token = keycloak_openid.refresh_token(refresh_token)

    resp = make_response(jsonify({'message': 'Token refreshed successfully'}))
    resp.set_cookie('token', token['access_token'], httponly=True, secure=True, samesite='Strict')
    resp.set_cookie('refresh_token', token['refresh_token'], httponly=True, secure=True, samesite='Strict')
    return resp


@app.route('/logout', methods=['POST'])
def logout():
    resp = make_response(jsonify({'message': 'Logged out successfully'}))
    resp.set_cookie('token', '', expires=0)
    resp.set_cookie('refresh_token', '', expires=0)
    return resp


if __name__ == '__main__':
    app.run(port=PORT)
