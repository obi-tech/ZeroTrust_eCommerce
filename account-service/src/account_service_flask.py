# auth_service/auth_service.py
from flask import Flask, request, jsonify
import jwt
import datetime
import hashlib
import os
from functools import wraps
from db import get_account_collection

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

# Helper Functions
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = get_account_collection().find_one({'email': data['email']})
        except:
            return jsonify({'message': 'Invalid token!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if get_account_collection().find_one({'email': data['email']}):
        return jsonify({'message': 'Account already exists!'}), 400
    hashed_password = hash_password(data['password'])
    get_account_collection().insert_one({'name': data['name'], 'email': data['email'], 'password': hashed_password})
    return jsonify({'message': 'Account registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    account = get_account_collection().find_one({'email': data['email']})
    if account and account['password'] == hash_password(data['password']):
        token = jwt.encode({'email': account['email'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/account', methods=['GET'])
@token_required
def get_account(current_user):
    return jsonify({'name': current_user['name'], 'email': current_user['email']})

@app.route('/account', methods=['PUT'])
@token_required
def update_account(current_user):
    data = request.get_json()
    update_data = {}
    if 'name' in data:
        update_data['name'] = data['name']
    if 'email' in data:
        update_data['email'] = data['email']
    if 'password' in data:
        update_data['password'] = hash_password(data['password'])
    get_account_collection().update_one({'_id': current_user['_id']}, {'$set': update_data})
    return jsonify({'message': 'Account updated successfully!'})

@app.route('/account', methods=['DELETE'])
@token_required
def delete_account(current_user):
    get_account_collection().delete_one({'_id': current_user['_id']})
    return jsonify({'message': 'Account deleted successfully!'})

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=11500)
