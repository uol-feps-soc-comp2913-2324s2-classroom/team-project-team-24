# endpoints/friends.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import *
from app.models import User
import stripe

# This is your Stripe CLI webhook secret for testing your endpoint locally.
WEBHOOK_SECRET = 'whsec_7d4a3ea9df544e2d813140092a64baa04aaa6256129ededc7adcc9584f321355'

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
    stripe.Subscription.modify(
        user.stripe_subscription,
        cancel_at_period_end=True,
    )
    user.stripe_subscription = None
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

@bp.route('/get-checkout-session', methods=['POST'])
@jwt_required()
def create_checkout_session():
    membership_id = request.get_json().get("membershipID")
    membership = MembershipPlan.query.filter_by(id=membership_id).first()
    print(membership)
    YOUR_DOMAIN = "http://localhost:8080"
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': membership.stripe_price,
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=YOUR_DOMAIN + '/membership',
            cancel_url=YOUR_DOMAIN + '/membership',
            metadata={
                "userID": get_current_user().id,
                "membershipID": membership_id,
            }
        )
    except Exception as e:
            return str(e)

    return jsonify({"url": checkout_session.url})

@app.route('/webhook', methods=['POST'])
def webhook_received():
    
    request_data = request.get_json()

    if WEBHOOK_SECRET:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                    payload=request.data, sig_header=signature, secret=WEBHOOK_SECRET)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']
    metadata = data_object["metadata"]

    if event_type == 'checkout.session.completed':
        # ensure that user is not a member
        if get_user_membership_id(int(metadata["userID"])) == int(metadata["membershipID"]):
            return jsonify({"error": "User is already on this membership tier"}), 400
        
        # Cancel a previous membership
        user = User.query.filter_by(id=int(metadata["userID"])).first()
        print(user.stripe_subscription)
        if user.stripe_subscription != None:
            stripe.Subscription.modify(
                user.stripe_subscription,
                cancel_at_period_end=True,
            )
            user.stripe_subscription = None
        
        set_user_membership_plan(int(metadata["userID"]), int(metadata["membershipID"]))
        user.stripe_subscription = data_object["subscription"]
        db.session.add(user)
        db.session.commit()
    
    elif event_type == 'invoice.paid':
        pass
    
    elif event_type == 'invoice.payment_failed':
        if get_membership_price(int(metadata["userID"])) != 0:
            delete_user_membership(int(metadata["userID"]))

    return jsonify({'status': 'success'})