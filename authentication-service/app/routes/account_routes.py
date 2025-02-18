from flask import Blueprint, request, jsonify
from app.services.account_service import create_account, get_account, update_account, delete_account
from app.auth import token_required

account_bp = Blueprint('account', __name__)

@account_bp.route('/accounts', methods=['POST'])
@token_required
def create_account_route():
    data = request.json
    response = create_account(data['name'], data['email'], data['password'])
    return jsonify({"id": response.id, "name": response.name, "email": response.email}), 201

@account_bp.route('/accounts/<account_id>', methods=['GET'])
@token_required
def get_account_route(account_id):
    response = get_account(account_id)
    return jsonify({"id": response.id, "name": response.name, "email": response.email})

@account_bp.route('/accounts/<account_id>', methods=['PUT'])
@token_required
def update_account_route(account_id):
    data = request.json
    response = update_account(account_id, data['name'], data['email'], data['password'])
    return jsonify({"id": response.id, "name": response.name, "email": response.email})

@account_bp.route('/accounts/<account_id>', methods=['DELETE'])
@token_required
def delete_account_route(account_id):
    response = delete_account(account_id)
    return jsonify({"message": response.message})