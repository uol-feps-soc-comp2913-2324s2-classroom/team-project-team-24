# endpoints/trails.py
from flask import Blueprint, Response, request, jsonify
from flask_jwt_extended import get_current_user, jwt_required
from app import db, app
from app.db_functions import get_routes_by_user_id
from app.models import User, Route
from app.gpx import GPX
import gpxpy
from app.decorators import *
from sqlalchemy import and_
import folium

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
    if User.query.filter_by(id=user_id).first() is None:
        return jsonify({"error": "Invalid user ID"}), 400
    # get trails from user ID
    trails = get_routes_by_user_id(user_id)
    trail_data = []
    for trail in trails:
        trail_data.append({
            "id": trail.id,
            "name": trail.name,
            "exercise_type": trail.exercise_type
        })

    return jsonify({
        "trails": trail_data
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
        "date": gpx.time.strftime("%d/%m/%Y"),
        "type": route.exercise_type,
        "distance": gpx.get_total_distance_km(),    # In Km
        "time": {"hours": hours, "minutes": minutes, "seconds": seconds},
        "speed": gpx.get_speed(),   # In Km/h
        "calories": 0,
    })

@bp.route('/get-map', methods=['POST'])
@jwt_required()
@membership_required
def get_trail_map():
    # Receive route ID
    user_id = get_current_user().id
    trail_id = request.get_json().get("trailID")
    if trail_id is None:
        return jsonify({"error": "Missing trail ID"}), 400
    
    # Ensure route ID is valid
    route = Route.query.filter_by(id=trail_id).first()
    if route is None or route.user_id != user_id:
        return jsonify({"error": f"Invalid trail ID {trail_id}"}), 400
    # Get route
    if route.data is None:
        return jsonify({"error": "Invalid trail data"}), 400
    
    # Display map
    gpx = GPX(route.data)
    map_html = gpx.display()
    
    return Response(map_html, mimetype='text/html')

@bp.route('/get-selected-map', methods=['POST'])
@jwt_required()
@membership_required
def get_selected_trails_map():
    user_id = get_current_user().id
    trail_ids = request.get_json().get("trailIDs")
    
    if not trail_ids:
        return jsonify({"error": "No trail IDs provided"}), 400
    
    routes = Route.query.filter(Route.id.in_(trail_ids), Route.user_id == user_id).all()
    
    if not routes:
        return jsonify({"error": "No valid routes found"}), 400
    
    map_obj = folium.Map(location=[0, 0], zoom_start=2)
    
    for route in routes:
        gpx = GPX(route.data)
        points = []
        for track in gpx.gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append(tuple([point.latitude, point.longitude]))
        folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(map_obj)
    
    map_html = map_obj._repr_html_()
    
    return jsonify({"mapHtml": map_html})

@bp.route('/zoom-to-trail', methods=['POST'])
@jwt_required()
@membership_required
def zoom_to_trail():
    user_id = get_current_user().id
    trail_id = request.get_json().get("trailID")
    
    if not trail_id:
        return jsonify({"error": "No trail ID provided"}), 400
    
    route = Route.query.filter_by(id=trail_id, user_id=user_id).first()
    
    if not route:
        return jsonify({"error": "Invalid trail ID"}), 400
    
    gpx = GPX(route.data)
    points = []
    for track in gpx.gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    
    if not points:
        return jsonify({"error": "No track points found"}), 400
    
    map_obj = folium.Map(location=points[0], zoom_start=14)
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(map_obj)
    
    map_html = map_obj._repr_html_()
    
    return jsonify({"mapHtml": map_html})

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
    
    routeID = Route.query.filter(and_(Route.name == route_name, Route.user_id == user_id)).first().id
    print(routeID)
    return jsonify({
        "trailID": routeID,
    })

