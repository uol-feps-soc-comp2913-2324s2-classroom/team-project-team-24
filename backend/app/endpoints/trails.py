# endpoints/trails.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import db_delete, get_routes_by_user_id
from app.gpx_functions import *
from app.models import User, Route
import gpxpy

bp = Blueprint('trails', __name__)

@bp.route('/get_overall_stats', methods=['GET'])
@jwt_required()
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

    durations = [trail.get_duration() for trail in trails]
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

@bp.route('/get_trails', methods=['GET'])
@jwt_required()
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

    # return trails
    return jsonify({
        "trails": trail_ids
    })

@bp.route('/get_trail_data', methods=['GET'])
@jwt_required()
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

    gpx = gpxpy.parse(route.data)
    duration = get_duration(gpx)
    hours = int(duration / 3600)
    minutes = int((duration % 3600) / 60)
    seconds = int(duration % 60)

    # TODO: calorie calculation

    # return trails
    return jsonify({
        "name": route.name,
        "date": str(gpx.time),
        "distance": get_total_distance_km(gpx),    # In Km
        "time": {"hours": hours, "minutes": minutes, "seconds": seconds},
        "speed": get_speed(gpx),   # In Km/h
        "calories": 0,
        "gpx": route.data,
    })

@bp.route('/delete_trail', methods=['POST'])
@jwt_required()
def delete_trail():
    # delete a trail from the database

    # recieve user ID and trail ID
    user_id = get_current_user().id
    trail_id = request.form["trailID"]

    # ensure route ID is valid
    route = Route.query.filter_by(id=trail_id).first()
    if route == None or route.user_id != user_id:
        return jsonify({"error": "Invalid trail ID"}), 400

    # delete route from database
    db_delete(route)

    return Response(f"Route {trail_id} successfully deleted", 200)