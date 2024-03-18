# endpoints/friends.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import *
from app.gpx_functions import *
from app.models import User, Route, Friend

bp = Blueprint('groups', __name__)

@bp.route('/get_groups', methods=['GET'])
@jwt_required()
def get_groups():
    # recieve user ID
    user_id = get_current_user().id
    user = User.query.filter_by(id=user_id).first()

    groups = []
    for group in user.groups:
        groups.append({"id": group.id, "name": group.name})

    return jsonify({
        "groups": groups
    })


@bp.route('/create_group', methods=['POST'])
@jwt_required()
def create_group():
    # recieve user ID
    user_id = get_current_user().id

    name = request.form.get("groupName")
    if name == None:
        return jsonify({"error": "Missing group name"}), 400

    group_id = create_new_group(user_id, name)

    # ensure group was created properly
    if Group.query.filter_by(id=group_id, name=name).first() == None:
        return jsonify({"error": "Failed to create group"}), 400 

    return Response(f"Group {name} successfully created", 200)
