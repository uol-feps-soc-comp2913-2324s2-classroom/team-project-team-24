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
    email = data['email']

    if username == "":
        return jsonify(error="Please enter a username"), 400
    
    if password == "":
        return jsonify(error="Please enter a password"), 400
    
    if email == "":
        return jsonify(error="Please enter an email"), 400

    user = User.query.filter_by(username=username).first()
    if user is not None:
        return jsonify(error="Username already in use - please pick another."), 400
    
    if User.query.filter_by(email=email).first() is not None:
        return jsonify(error="Email already in use."), 400
    
    create_user(username, password, email)
    user = User.authenticate(username=username, password=password)
    access_token = create_access_token(identity=user)

    response = jsonify({'success': True, 'token': access_token})

    return response, 201
        
    
@bp.route('/login', methods=('POST',))
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.authenticate(username, password)
    if user:
        access_token = create_access_token(identity=user)

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


