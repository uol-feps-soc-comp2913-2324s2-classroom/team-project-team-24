# endpoints/owner.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import *
from app.models import User
from app.decorators import *
from datetime import date

bp = Blueprint('owner', __name__, url_prefix='/owner')

# how many users the application has
# what subscription types those users have

# response = {
#     numUsers = 10,
#     subscriptions = {
#         "user1": "monthly",
#         ...
#     }
# }

@bp.route('/get-owner-membership-data', methods=['GET'])
@jwt_required()
@membership_required
def get_owner_membership_data():
    response = {}
    response["numUsers"] = len(User.query.all())

    memberships = []
    for membership in MembershipPlan.query.all():
        memberships.append({
            "id": membership.id,
            "name": membership.name,
            "payment_regularity": membership.payment_regularity,
            "cost": membership.cost,
            "numMembers": len(User.query.filter_by(membership_id=membership.id).all())
        })

    response["memberships"] = memberships
    return jsonify(response)

# what revenue levels they'll have weekly
# expected annual revenue (calculated)

@bp.route('/get-future-revenue', methods=['GET'])
@jwt_required()
@membership_required
def get_future_revenue():
    response = {}

    today = date.today()
    for i in range(52):
        d = today + (i * datetime.timedelta(days=7))
        response[str(d)] = 0

    print(response)
    return jsonify(response)