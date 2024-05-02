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
#   "numUsers": n,
#   "memberships": [
#     {
#       "id": n,
#       "name": "Annual",
#       "payment_regularity": "yearly",
#       "cost": 99.5,
#       "numMembers": n
#     },
#     {
#       "id": n,
#       "name": "Monthly",
#       "payment_regularity": "monthly",
#       "cost": 12.5,
#       "numMembers": n
#     },
#     ...
#   ]
# }

@bp.route('/get-owner-membership-data', methods=['GET'])
@jwt_required()
@membership_required
def get_owner_membership_data():
    user = get_current_user()

    if not user.is_owner:
        return jsonify({"error": "Not authorised"}), 400

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

# response = {
#   "data": [
#     {
#       "date": "29-04-2024",
#       "amount": 105.00
#     },
#     {
#       "date": "06-05-2024",
#       "amount": 80.50
#     },
#     ...
#   ]
# }

@bp.route('/get-future-revenue', methods=['GET'])
@jwt_required()
@membership_required
def get_future_revenue():
    user = get_current_user()
    if not user.is_owner:
        return jsonify({"error": "Not authorised"}), 400

    response = {}

    # set up data list with valid dates
    data = []
    day_offset = 0
    today = date.today()
    for i in range(52):
        d = today + (i * datetime.timedelta(days=7))
        data.append({
            "date": str(d),
            "amount": 0
        })

    # for each user, calculate the amount they will be paying by each date in data
    for user in User.query.all():
        next_future_payment = user.membership_start_date
        membership = MembershipPlan.query.filter_by(id=user.membership_id).first()
        
        # determine how often the user will be paying
        if membership.payment_regularity == "yearly":
            day_offset = 365
        elif membership.payment_regularity == "monthly":
            day_offset = 31
        elif membership.payment_regularity == "weekly":
            day_offset = 7

        # get the first date that the user will be paying
        while next_future_payment.date() < date.today():
            next_future_payment += datetime.timedelta(days=day_offset)

        # find closest date after each payment,
        # then increment that date's total payment amount by the user's membership price
        for i in range(len(data)):
            if datetime.datetime.strptime(data[i]["date"], "%Y-%m-%d").date() >= next_future_payment.date():
                data[i]["amount"] += membership.cost
                next_future_payment += datetime.timedelta(days=day_offset)

    response["data"] = data
    return jsonify(response)
