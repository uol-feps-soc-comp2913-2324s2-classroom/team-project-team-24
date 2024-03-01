# endpoints/auth.py
from flask import Blueprint
from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from models import User


bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route('/register', methods=('POST',))
def register():
    data = request.get_json()
    password = data['password']
    username = data['username']

    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(
            username=username,
            password=password
        )

        user.add()    
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        response = jsonify()
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        return response, 201
    else:
        return jsonify(message="Unable to create user."), 400
    
@bp.route('/login', methods=('POST',))
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.authenticate(username, password)
    if user:
        access_token = create_access_token(identity=user.user_id)
        refresh_token = create_refresh_token(identity=user.user_id)

        response = jsonify()
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response, 201
    else:
        return jsonify(message="Unauthorized"), 401