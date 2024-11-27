from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from repositories.user_repository import UserRepository
from models import User

bcrypt = Bcrypt()

class AuthService:
    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            token = create_access_token(identity={"id": user.id, "is_admin": user.is_admin})
            return token
        return None

    @staticmethod
    def register(username, password, is_admin=False):
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password, is_admin=is_admin)
        UserRepository.create(new_user)
