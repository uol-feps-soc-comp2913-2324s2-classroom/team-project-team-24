# endpoints/auth.py
from flask import Blueprint
from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, unset_jwt_cookies, jwt_required, get_current_user
from app.models import User
from app.db_functions import create_user
from app import app


bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route('/register', methods=('POST',))
def register():
    data = request.get_json()
    password = data['password']
    username = data['username']

    user = User.query.filter_by(username=username).first()
    if user is None:
        create_user(username, password)
        user = User.authenticate(username=username, password=password)
        access_token = create_access_token(identity=user.id)

        response = jsonify({'success': True, 'token': access_token})

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
        access_token = create_access_token(identity=user.id)

        response = jsonify({'success': True, 'token': access_token})
        return response, 201
    else:
        return jsonify(message="Unauthorized"), 401
    
@bp.route('/logout', methods=('POST',), endpoint='logout')
@jwt_required()
def logout():
  response = jsonify()
  unset_jwt_cookies(response)
  return response, 200


@bp.route('/verify-token', methods=('POST',), endpoint='verify-token')
@jwt_required()
def verify_token():
    return jsonify({'success': True}), 200


