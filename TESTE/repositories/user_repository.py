from models import User
from database import db

class UserRepository:
    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()
