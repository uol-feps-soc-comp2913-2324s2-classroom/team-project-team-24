# endpoints/trails.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import get_routes_by_user_id
from app.models import User, Route
from app.gpx import GPX
import gpxpy
from app.decorators import *

bp = Blueprint('trails', __name__, url_prefix="/trail")

@bp.route('/get-overall-stats', methods=['GET'])
@jwt_required()
@membership_required
def get_overall_stats():
    # get overall trail stats for a given user ID

    # recieve user ID
    user_id = get_current_user().id
    if user_id is None:
        return jsonify({"error": "Missing user ID"}), 400

    # ensure user ID is valid
    if User.query.filter_by(id=user_id).first() == None:
        return jsonify({"error": "Invalid user ID"}), 400

    # get trails from user ID
    trails = get_routes_by_user_id(user_id)

    durations = [GPX(trail.data).get_duration() for trail in trails]
    totalDuration = sum(durations)
    totalDuration_h = int(totalDuration / 3600)
    totalDuration_m = int((totalDuration % 3600) / 60)
    totalDuration_s = int(totalDuration % 60)

    longestDuration = max(durations)
    longestDuration_h = int(longestDuration / 3600)
    longestDuration_m = int((longestDuration % 3600) / 60)
    longestDuration_s = int(longestDuration % 60)

    # TODO: calorie calculation

    return jsonify({
        # Total time spent doing activities in a period of time
        "totalDuration": {"hours": totalDuration_h, "minutes": totalDuration_m, "seconds": totalDuration_s},
        # Longest activity in time period
        "longestTime": {"hours": longestDuration_h, "minutes": longestDuration_m, "seconds": longestDuration_s},
        # Total calories burn in time period
        "totalCalories": 0
    })

@bp.route('/get-longest', methods=['GET'])
@jwt_required()
@membership_required
def get_longest_trail():
    # get longest distance trail ID for a given user ID

    # recieve user ID
    user_id = get_current_user().id
    if user_id is None:
        return jsonify({"error": "Missing user ID"}), 400

    # ensure user ID is valid
    if User.query.filter_by(id=user_id).first() == None:
        return jsonify({"error": "Invalid user ID"}), 400

    # get trails from user ID
    trails = get_routes_by_user_id(user_id)
    longest = {
        "distance": 0,
        "trailID": -1,
    }

    for trail in trails:
        dist = GPX(trail.data).get_total_distance_km()
        if dist > longest["distance"]:
            longest["distance"] = dist
            longest["trailID"] = trail.id


    # get trail IDs from trails
    print(longest)
    # return trails
    return jsonify({
        "trailID": longest["trailID"]
    })

@bp.route('/get-all', methods=['GET'])
@jwt_required()
@membership_required
def get_trails():
    # get all the trail IDs for a given user ID

    # recieve user ID
    user_id = get_current_user().id
    if user_id is None:
        return jsonify({"error": "Missing user ID"}), 400

    # ensure user ID is valid
    if User.query.filter_by(id=user_id).first() == None:
        return jsonify({"error": "Invalid user ID"}), 400

    # get trails from user ID
    trails = get_routes_by_user_id(user_id)

    # get trail IDs from trails
    trail_ids = [trail.id for trail in trails]
    print(trail_ids)
    # return trails
    return jsonify({
        "trails": trail_ids
    })

@bp.route('/get-data', methods=['POST'])
@jwt_required()
@membership_required
def get_trail_data():
    # get data for a given trail ID
    
    # recieve route ID
    user_id = get_current_user().id
    trail_id = request.get_json().get("trailID")
    if trail_id is None:
        return jsonify({"error": "Missing trail ID"}), 400

    # ensure route ID is valid
    route = Route.query.filter_by(id=trail_id).first()
    if route == None or route.user_id != user_id:
        return jsonify({"error": "Invalid trail ID"}), 400

    # get route
    route = Route.query.filter_by(id=trail_id).first()
    
    if route.data == None:
        return jsonify({"error": "Invalid trail data"}), 400

    gpx = GPX(route.data)
    duration = gpx.get_duration()
    hours = int(duration / 3600)
    minutes = int((duration % 3600) / 60)
    seconds = int(duration % 60)

    # TODO: calorie calculation

    # return trails
    return jsonify({
        "name": route.name,
        "date": str(gpx.time),
        "distance": gpx.get_total_distance_km(),    # In Km
        "time": {"hours": hours, "minutes": minutes, "seconds": seconds},
        "speed": gpx.get_speed(),   # In Km/h
        "calories": 0,
    })

@bp.route('/get-map', methods=['POST'])
@jwt_required()
@membership_required
def get_trail_map():
    # recieve route ID
    user_id = get_current_user().id
    trail_id = request.get_json().get("trailID")
    if trail_id is None:
        return jsonify({"error": "Missing trail ID"}), 400
    
    # ensure route ID is valid
    route = Route.query.filter_by(id=trail_id).first()
    if route == None or route.user_id != user_id:
        return jsonify({"error": f"Invalid trail ID {trail_id}"}), 400

    # get route
    route = Route.query.filter_by(id=trail_id).first()
    
    if route.data == None:
        return jsonify({"error": "Invalid trail data"}), 400
    
    gpx = GPX(route.data)
    map_html = gpx.display()
    return Response(map_html, mimetype='text/html')

@bp.route('/delete', methods=['POST'])
@jwt_required()
@membership_required
def delete_trail():
    # delete a trail from the database

    # recieve user ID and trail ID
    user_id = get_current_user().id
    trail_id = request.get_json().get("trailID")

    # ensure route ID is valid
    route = Route.query.filter_by(id=trail_id).first()
    if route == None or route.user_id != user_id:
        return jsonify({"error": "Invalid trail ID"}), 400

    # delete route from database
    Route.query.filter_by(id=trail_id).delete()
    db.session.commit()

    return Response(f"Route {trail_id} successfully deleted", 200)

@bp.route('/upload', methods=('POST',))
@jwt_required()
@membership_required
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

