from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    return AuthService.register_user(username, password)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    return AuthService.login_user(username, password)