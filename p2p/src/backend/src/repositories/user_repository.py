from models.user import User
from extensions import db

class UserRepository:
    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def save(user):
        db.session.add(user)
        db.session.commit()