from flask import Blueprint, request, jsonify
from models import db, User
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__)


@user_bp.route('', methods=['GET'])
@jwt_required()
def get_users():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if user.is_admin:
        users = User.query.all()
        return jsonify([user.serialize() for user in users]), 200
    return jsonify({"message": "Admin access required"}), 403


@user_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def edit_user(id):
    current_user_id = get_jwt_identity()
    user = User.query.get(id)
    if user and (user.id == current_user_id or user.is_admin):
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.password = data.get('password', user.password)  
        db.session.commit()
        return jsonify(user.serialize()), 200
    return jsonify({"message": "You can only edit your own user or be admin"}), 403


@user_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    current_user_id = get_jwt_identity()
    user = User.query.get(id)
    if user and (user.id == current_user_id or user.is_admin):
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "You can only delete your own user or be admin"}), 403
