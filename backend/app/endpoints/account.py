# endpoints/friends.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import *
from app.models import User

bp = Blueprint('account', __name__, url_prefix='/account')

@bp.route('/set-details', methods=['POST'])
@jwt_required()
def set_account_details():
    # recieve user ID and new password
    user = get_current_user()
    data = request.get_json()
    print(data)
    print(request.files["profilePhoto"].read().decode("utf-8"))
    # I don't mind if any/all of the data is missing
    if data.get('name') is not None:
        user.name = data['name']

    if data.get('email') is not None:
        user.email = data['email']

    if data.get('age') is not None:
        user.age = data['age']

    if data.get('gender') is not None:
        user.gender = data['gender']

    if data.get('profilePhoto') is not None:
        user.profile_photo = data['profilePhoto']
    

    db.session.commit()

    return Response(f"Details successfully updated", 200)

@bp.route('/get-details', methods=['GET'])
@jwt_required()
def get_account_details():
    # recieve user
    user = get_current_user()
    membership = MembershipPlan.query.filter_by(id=user.membership_id).first()

    # return trails
    return jsonify({
        "name": user.username,
        "email": user.email,
        "profilePhoto": user.profile_picture,
        "membershipTier": membership.name if membership is not None else None,
        "gender": user.gender,
        "age": user.age,
        "paymentRegularity": membership.payment_regularity if membership is not None else None
    })

@bp.route('/change-password', methods=['POST'])
@jwt_required()
def change_password():
    # recieve user ID and new password
    user = get_current_user()
    password = request.form.get("password")

    # ensure new password given
    if password == None:
        return jsonify({"error": "Missing new password"}), 400

    # change password
    user.password = hash_pwd(password)
    db.session.commit()

    return Response(f"Password successfully changed", 200)

@bp.route('/delete', methods=['GET'])
@jwt_required()
def delete_account():
    # recieve user
    user = get_current_user()

    # delete account
    db.session.delete(user)
    db.session.commit()

    return Response(f"Account deleted", 200)
