# endpoints/friends.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import *
from app.gpx_functions import *
from app.models import User, Route, Friend

bp = Blueprint('friends', __name__)

@bp.route('/get_friends', methods=['GET'])
@jwt_required()
def get_friends():
    # recieve user ID
    user_id = get_current_user().id

    # get user's friends' IDs
    user_friends = []
    friends = Friend.query.all()
    for friend in friends:
        if friend.user_1_id == user_id:
            if friend.user_2_id not in friends:
                user_friends.append(friend.user_2_id)

        if friend.user_2_id == user_id:
            if friend.user_1_id not in friends:
                user_friends.append(friend.user_1_id)

    # get info about each friend
    friends_info = []
    for friend_id in user_friends:
        friend = User.query.filter_by(id=friend_id).first()
        friends_info += {
            "id": friend_id,
            "name": friend.username,
            "profilePhoto": friend.profile_picture
        }

    return jsonify({"friends": friends_info})

@bp.route('/add_friend', methods=['POST'])
@jwt_required()
def add_friend():
    user_id = get_current_user().id
    user_2_id = request.form.get("userID2")

    if user_2_id == None:
        return jsonify({"error": "User 2 ID not given"}), 400
    
    if User.query.filter_by(id=user_2_id).first() == None:
        return jsonify({"error": "Invalid ID"}), 400

    if check_for_friendship(user_id, user_2_id):
        return jsonify({"error": "Friendship already exists"}), 400

    create_friendship(user_id, user_2_id)
    return Response("Friendship created", 200)

@bp.route('/send_friend_request', methods=['POST'])
@jwt_required()
def send_friend_request():
    user_id = get_current_user().id
    to_id = request.form.get("receiveUserID")

    if to_id == None:
        return jsonify({"error": "Receive user ID not given"}), 400
    
    if User.query.filter_by(id=to_id).first() == None:
        return jsonify({"error": "Invalid ID"}), 400

    if check_for_friendship(user_id, to_id):
        return jsonify({"error": "Users are already friends"}), 400

    if check_for_friend_request(user_id, to_id):
        return jsonify({"error": "Friend request already exists"}), 400

    create_friend_request(user_id, to_id)
    return Response("Friend request created", 200)