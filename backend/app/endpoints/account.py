# endpoints/friends.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import *
from app.gpx_functions import *
from app.models import User

bp = Blueprint('account', __name__)
    