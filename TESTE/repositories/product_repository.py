from models import Product
from database import db

class ProductRepository:
    @staticmethod
    def get_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def get_all():
        return Product.query.all()

    @staticmethod
    def create(product):
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(product):
        db.session.delete(product)
        db.session.commit()