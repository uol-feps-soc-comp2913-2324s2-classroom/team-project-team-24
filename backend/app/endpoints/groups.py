# endpoints/friends.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import *
from app.models import User, Route, Friend
from app.decorators import *

bp = Blueprint('groups', __name__, url_prefix='/groups')

@bp.route('/get-all', methods=['GET'])
@jwt_required()
@membership_required
def get_groups():
    # recieve user ID
    user_id = get_current_user().id
    user = User.query.filter_by(id=user_id).first()

    groups = []
    for group in user.groups:
        groups.append({"id": group.id, "name": group.name})

    for x in Group.query.all():
        print(x, x.members)
    return jsonify({
        "groups": groups
    })

@bp.route('/create', methods=['POST'])
@jwt_required()
@membership_required
def create_group():
    # recieve user ID
    user_id = get_current_user().id

    name = request.get_json().get("groupName")
    if name == None:
        return jsonify({"error": "Missing group name"}), 400

    group_id = create_new_group(user_id, name)

    # ensure group was created properly
    if Group.query.filter_by(id=group_id, name=name).first() == None:
        return jsonify({"error": "Failed to create group"}), 400 

    return Response(f"Group {name} successfully created", 200)

@bp.route('/get-name', methods=['POST'])
@jwt_required()
@membership_required
def get_group_name():
    # recieve user ID
    user_id = get_current_user().id

    group_id = request.get_json().get("groupID")
    if group_id == None:
        return jsonify({"error": "Missing group ID"}), 400

    group = Group.query.filter_by(id=group_id).first()

    if group == None:
        return jsonify({"error": "Invalid group ID"}), 400

    if not check_for_user_in_group(user_id, group_id):
        return jsonify({"error": "User is not in this group"}), 400

    return jsonify({
        "name": group.name
    })

@bp.route('/get-trails', methods=['POST'])
@jwt_required()
@membership_required
def get_group_trails():
    # recieve user ID
    user_id = get_current_user().id

    group_id = request.json.get("groupID")
    if group_id == None:
        return jsonify({"error": "Missing group ID"}), 400

    if Group.query.filter_by(id=group_id).first() == None:
        return jsonify({"error": "Invalid group ID"}), 400

    if not check_for_user_in_group(user_id, group_id):
        return jsonify({"error": "User is not in this group"}), 400

    trails = [trail.id for trail in Group.query.filter_by(id=group_id).first().routes]

    return jsonify({
        "trails": trails
    })

@bp.route('/get-members', methods=['POST'])
@jwt_required()
@membership_required
def get_group_members():
    # recieve user ID
    user_id = get_current_user().id

    group_id = request.get_json().get("groupID")
    if group_id == None:
        return jsonify({"error": "Missing group ID"}), 400

    group = Group.query.filter_by(id=group_id).first()
    if group == None:
        return jsonify({"error": "Invalid group ID"}), 400

    if not check_for_user_in_group(user_id, group_id):
        return jsonify({"error": "User is not in this group"}), 400

    member_ids = [member.id for member in group.members]

    # get info about each group member
    members_info = []
    for member_id in member_ids:
        member = User.query.filter_by(id=member_id).first()
        members_info.append({
            "id": member_id,
            "name": member.username
        })

    return jsonify({"members": members_info})

@bp.route('/leave', methods=['POST'])
@jwt_required()
@membership_required
def leave_group():
    # recieve user ID
    user_id = get_current_user().id

    group_id = request.get_json().get("groupID")
    if group_id == None:
        return jsonify({"error": "Missing group ID"}), 400
    
    group = Group.query.filter_by(id=group_id).first()
    if group == None:
        return jsonify({"error": "Invalid group ID"}), 400
    
    if not check_for_user_in_group(user_id, group_id):
        return jsonify({"error": "User is not in this group"}), 400
    
    # leave group
    remove_user_from_group(user_id, group_id)

    # if group is empty, delete group
    if len(group.members) == 0:
        delete_group(group_id)

    return Response(f"Successfully left group", 200)

@bp.route('/add-route', methods=['POST'])
@jwt_required()
@membership_required
def add_route_to_group_route():
    # recieve user ID
    user_id = get_current_user().id

    group_id = request.get_json().get("groupID")
    route_id = request.get_json().get("routeID")

    if group_id == None or route_id == None:
        return jsonify({"error": "Missing route ID and/or group ID"}), 400

    group = Group.query.filter_by(id=group_id).first()
    if group == None:
        return jsonify({"error": "Invalid group ID"}), 400
    
    route = Route.query.filter_by(id=route_id).first()
    if route == None:
        return jsonify({"error": "Invalid route ID"}), 400
    
    if route.user_id != user_id:
        return jsonify({"error": "Route does not belong to this user"}), 400

    if not check_for_user_in_group(user_id, group_id):
        return jsonify({"error": "User not in this group"}), 400
    
    if check_for_route_in_group(route_id, group_id):
        return jsonify({"error": "Route already in group"}), 400

    add_route_to_group(route_id, group_id)
    return Response(f"Route successfully added to group", 200)

@bp.route('/add-friend', methods=['POST'])
@jwt_required()
@membership_required
def add_user_to_group_route():
    # recieve user ID
    user_id = get_current_user().id

    group_id = request.get_json().get("groupID")
    friend_id = request.get_json().get("friendID")
    if group_id == None or friend_id == None:
        return jsonify({"error": "Missing friend ID and/or group ID"}), 400

    group = Group.query.filter_by(id=group_id).first()
    if group == None:
        return jsonify({"error": "Invalid group ID"}), 400
    
    friend = User.query.filter_by(id=friend_id).first()
    if friend == None:
        return jsonify({"error": "Invalid friend ID"}), 400

    if not check_for_user_in_group(user_id, group_id):
        return jsonify({"error": "User not in this group"}), 400

    if not check_for_friendship(user_id, friend_id):
        return jsonify({"error": "Users are not friends"}), 400
    
    if check_for_user_in_group(friend_id, group_id):
        return jsonify({"error": "Friend already in group"}), 400

    add_user_to_group(friend_id, group_id)
    return Response(f"Friend successfully added to group", 200)


@bp.route('/get-trails-complete', methods=['POST'])
@jwt_required()
@membership_required
def get_group_trails_complete():
    # recieve user ID
    user_id = get_current_user().id

    group_id = request.json.get("groupID")
    if group_id == None:
        return jsonify({"error": "Missing group ID"}), 400

    if Group.query.filter_by(id=group_id).first() == None:
        return jsonify({"error": "Invalid group ID"}), 400

    if not check_for_user_in_group(user_id, group_id):
        return jsonify({"error": "User is not in this group"}), 400

    trails = [trail.id for trail in Group.query.filter_by(id=group_id).first().routes]

    # Stores a list of all the trails in the group with their names and exercise types
    trails_complete = []
    for trail_id in trails:
        trail = Route.query.filter_by(id=trail_id).first()
        trail_data = {
            "id": trail.id,
            "name": trail.name,
            "exerciseType": trail.exercise_type,
        }
        trails_complete.append(trail_data)

    return jsonify({
        "trails": trails_complete
    })