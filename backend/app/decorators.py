from app.db_functions import get_user_membership_id
from flask import jsonify
from flask_jwt_extended import get_current_user

def membership_required(fn):
    def wrapper():
        if get_user_membership_id(get_current_user().id) is None:
            return jsonify({"error": "User is not a member"}), 400
        else:
            return fn()

    return wrapper