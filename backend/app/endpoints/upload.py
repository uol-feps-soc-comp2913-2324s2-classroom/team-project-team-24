# endpoints/upload.py
from flask import Blueprint, Response
from flask import request
from app import db, app
from tests.test_db import create_user
from app.models import User, Route

bp = Blueprint('upload', __name__)

@bp.route('/upload', methods=('POST',))
def upload():
    # test user, will need to be replaced with actual authentication
    if User.query.filter_by(username="test_user").first() is None:
        create_user("test_user", "pwd")

    user_id = User.query.filter_by(username="test_user").first().id

    route_name = request.form["routeName"]
    # route name is optional, generate default name if empty
    if route_name == "":
        route_name = "My route"

    exercise_type = request.form["exerciseType"]
    if exercise_type == "":
        exercise_type = "None"

    if len(request.files) == 0:
        return Response("No file uploaded", 400)
    
    file = request.files["file"]
    gpx_data = file.read().decode("utf-8")

    if len(gpx_data) == 0:
        return Response("Invalid file", 400)

    # save route data to db
    route = Route(data=gpx_data, name=route_name, exercise_type=exercise_type, user_id=user_id)
    db.session.add(route)
    db.session.commit()

    return Response(f"Route '{route_name}' with type '{exercise_type}' and id {route.id} uploaded to user with id {user_id}", 200)
