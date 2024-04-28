# endpoints/owner.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import *
from app.models import User

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

# what revenue levels they'll have weekly
# expected annual revenue (calculated)