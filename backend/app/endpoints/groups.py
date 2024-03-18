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

    