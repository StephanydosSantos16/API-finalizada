from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import db, Usuario

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    if not username or not password:
        return jsonify({"msg": "Nome de usuário e senha são necessários!"}), 400

    user = Usuario.query.filter_by(username=username).first()
    if user:
        return jsonify({"msg": "Usuário já existe!"}), 400

    hashed_password = generate_password_hash(password)
    new_user = Usuario(username=username, senha=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "Usuário criado com sucesso!"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"msg": "Nome de usuário e senha são necessários!"}), 400

    user = Usuario.query.filter_by(username=username).first()
    if not user:
        return jsonify({"msg": "Usuário não encontrado!"}), 404

    if not check_password_hash(user.senha, password):
        return jsonify({"msg": "Senha incorreta!"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200
