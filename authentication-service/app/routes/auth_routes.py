from flask import Blueprint, request, jsonify
from app.services.account_service import create_account, get_account_by_email
from app.services.logging_service import LoggingClient
from app.utils.jwt_utils import generate_token

auth_bp = Blueprint('auth', __name__)
logging_client = LoggingClient()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    response = create_account(data['name'], data['email'], data['password'])
    token = generate_token(response.id)
    return jsonify({"token": token, "user": {"id": response.id, "name": response.name, "email": response.email}}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    # In a real-world scenario, you'd verify the password here
    # For this example, we'll just check if the account exists
    try:
        response = get_account_by_email(data['email'])  # Assuming email is used as ID
        token = generate_token(response.id)
        logging_client.send_log('account_service', 'INFO', 'User login successful')
        return jsonify({"token": token, "user": {"id": response.id, "name": response.name, "email": response.email}})
    except:
        return jsonify({"message": "Invalid credentials"}), 401