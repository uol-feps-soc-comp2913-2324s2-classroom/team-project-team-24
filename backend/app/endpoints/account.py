# endpoints/friends.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import *
from app.gpx_functions import *
from app.models import User

bp = Blueprint('account', __name__)

@bp.route('/get_account_details', methods=['GET'])
@jwt_required()
def get_account_details():
    # recieve user
    user = get_current_user()
    membership = MembershipPlan.query.filter_by(id=user.membership_id).first()

    # return trails
    return jsonify({
        "name": user.username,
        "profilePhoto": user.profile_picture,
        "membershipTier": membership.name if membership is not None else None,
        "gender": user.sex,
        "age": get_age_from_date_of_birth(user.date_of_birth),
        "paymentRegularity": membership.payment_regularity if membership is not None else None
    })

@bp.route('/change_password', methods=['POST'])
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

@bp.route('/delete_account', methods=['POST'])
@jwt_required()
def delete_account():
    # recieve user
    user = get_current_user()

    # delete account
    db.session.delete(user)
    db.session.commit()

    return Response(f"Account deleted", 200)
