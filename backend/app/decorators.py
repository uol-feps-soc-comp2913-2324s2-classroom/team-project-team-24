from app.db_functions import get_user_membership_id
from flask import jsonify
from flask_jwt_extended import get_current_user

def membership_required(func):
    def wrapper():
        if get_user_membership_id(get_current_user().id) is None:
            return jsonify({"error": "User is not a member"}), 400
        else:
            return func()
        
    wrapper.__name__ = func.__name__
    return wrapper

def ownership_required(func):
    def wrapper():
        if get_current_user().is_owner != True:
            return jsonify({"error": "User is not an owner"}), 400
        else:
            return func()
        
    wrapper.__name__ = func.__name__
    return wrapper