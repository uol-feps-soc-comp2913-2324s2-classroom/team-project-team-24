# endpoints/upload.py
from flask import Blueprint, Response
from flask import request
from flask_jwt_extended import get_current_user, jwt_required
import gpxpy
from app import db, app
from app.db_functions import create_user, get_routes_by_user_id
from app.models import User, Route

bp = Blueprint('upload', __name__)

@bp.route('/upload', methods=('POST',))
@jwt_required()
def upload():
    user_id = get_current_user().id

    route_name = request.form["routeName"]
    # route name is optional, generate default name if empty
    if route_name == "":
        # get existing user routes
        routes = get_routes_by_user_id(user_id)

        valid_name_found = False
        i = 1
        while valid_name_found == False:
            valid_name_found = True
            for route in routes:
                if route.name == f"My route #{i}":
                    valid_name_found = False
                    i += 1

        route_name = f"My route #{i}"
    else:
        # check that user hasn't already used this name
        # get existing user routes
        routes = get_routes_by_user_id(user_id)

        for route in routes:
            if route.name == route_name:
                return Response("Route name already used", 400)

    exercise_type = request.form["exerciseType"]
    if exercise_type == "":
        exercise_type = "None"

    if len(request.files) == 0:
        return Response("No file uploaded", 400)
    
    file = request.files["file"]
    gpx_data = file.read().decode("utf-8")

    if len(gpx_data) == 0:
        return Response("Invalid file", 400)
    
    # check file is appropriate gpx type
    try:
        gpx = gpxpy.parse(gpx_data)

        if len(gpx.tracks) == 0:
            return Response("Invalid file contents", 400)
    except gpxpy.gpx.GPXXMLSyntaxException:
        return Response("Invalid file type", 400)

    # save route data to db
    route = Route(data=gpx_data, name=route_name, exercise_type=exercise_type, user_id=user_id)
    db.session.add(route)
    db.session.commit()

    return Response(f"Route '{route_name}' with type '{exercise_type}' and id {route.id} uploaded to user with id {user_id}", 200)
