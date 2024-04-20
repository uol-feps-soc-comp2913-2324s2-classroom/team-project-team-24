# endpoints/friends.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import *
from app.models import User

bp = Blueprint('memberships', __name__, url_prefix='/membership')

@bp.route('/get-current', methods=['GET'])
@jwt_required()
def get_current_membership():
    # ensure the user isn't on a free membership

    # recieve user
    user = get_current_user()

    # get memberships
    membership = MembershipPlan.query.filter_by(id=user.membership_id).first()

    if membership is not None:
        if membership.cost <= 0:
            membership = None
        else:
            membership = {
                "id": membership.id,
                "name": membership.name,
                "regularity": membership.payment_regularity,
                "price": membership.cost
            }

    # return trails
    return jsonify({
        "membership": membership
    })

@bp.route('/get-options', methods=['GET'])
@jwt_required()
def get_membership_options():
    # get all the membership IDs, specifying a user's current membership

    # recieve user
    user = get_current_user()

    # get memberships
    membershipOptions = []
    for membership in MembershipPlan.query.all():
        membershipOptions.append({
            "id": membership.id,
            "name": membership.name,
            "regularity": membership.payment_regularity,
            "price": membership.cost,
            "isCurrentPlan": user.membership_id == membership.id
        })

    # return trails
    return jsonify({
        "membershipOptions": membershipOptions
    })

@bp.route('/cancel', methods=['GET'])
@jwt_required()
def cancel_membership():
    # recieve user
    user = get_current_user()

    # ensure that user is a member
    if get_user_membership_id(user.id) == None or get_membership_price(user.id) == 0:
        return jsonify({"error": "User is not a member"}), 400

    delete_user_membership(user.id)
    return Response("Cancelled user membership", 200)

@bp.route('/purchase', methods=['POST'])
@jwt_required()
def purchase_membership():
    # recieve user
    user = get_current_user()
    membership_id = request.get_json().get("membershipID")

    # ensure that user is a member
    if get_user_membership_id(user.id) == membership_id:
        return jsonify({"error": "User is already on this membership tier"}), 400

    set_user_membership_plan(user.id, membership_id)
    return Response("User purchased new membership", 200)