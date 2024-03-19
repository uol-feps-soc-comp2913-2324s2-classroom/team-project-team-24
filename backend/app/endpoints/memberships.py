# endpoints/friends.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import *
from app.gpx_functions import *
from app.models import User

bp = Blueprint('memberships', __name__)

@bp.route('/check_membership', methods=['GET'])
@jwt_required()
def check_membership():
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
                "name": membership.name,
                "regularity": membership.payment_regularity,
                "price": membership.cost
            }

    # return trails
    return jsonify({
        "membership": membership
    })

@bp.route('/get_membership_options', methods=['GET'])
@jwt_required()
def get_membership_options():
    # get all the membership IDs, specifying a user's current membership

    # recieve user
    user = get_current_user()

    # get memberships
    membershipOptions = []
    for membership in MembershipPlan.query.all():
        membershipOptions.append({
            "name": membership.name,
            "regularity": membership.payment_regularity,
            "price": membership.cost,
            "isCurrentPlan": user.membership_id == membership.id
        })

    # return trails
    return jsonify({
        "membershipOptions": membershipOptions
    })