from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from repositories.user_repository import UserRepository
from models.user import User

class AuthService:
    @staticmethod
    def register_user(username, password):
        if UserRepository.find_by_username(username):
            return {'message': 'User already exists'}, 400

        hashed_password = generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        UserRepository.save(new_user)
        return {'message': 'User registered successfully'}, 201

    @staticmethod
    def login_user(username, password):
        user = UserRepository.find_by_username(username)
        if not user or not check_password_hash(user.password, password):
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return {'access_token': access_token}, 200