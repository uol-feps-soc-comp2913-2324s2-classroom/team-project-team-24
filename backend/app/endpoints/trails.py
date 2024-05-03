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
    
    if durations != []:
        totalDuration = sum(durations)
        totalDuration_h = int(totalDuration / 3600)
        totalDuration_m = int((totalDuration % 3600) / 60)
        totalDuration_s = int(totalDuration % 60)

        longestDuration = max(durations)
        longestDuration_h = int(longestDuration / 3600)
        longestDuration_m = int((longestDuration % 3600) / 60)
        longestDuration_s = int(longestDuration % 60)
    else:
        totalDuration = 0
        longestDuration_h = 0
        longestDuration_m = 0
        longestDuration_s = 0
        totalDuration_h = 0
        totalDuration_m = 0
        totalDuration_s = 0
        longestDuration = 0


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
    try:
        # get data for a given trail ID
        
        # receive route ID
        user_id = get_current_user().id
        data = request.get_json()
        trail_id = data.get("trailID")
        
        if trail_id is None:
            return jsonify({"error": "Missing trail ID"}), 400

        # ensure route ID is valid
        route = Route.query.filter_by(id=trail_id, user_id=user_id).first()
        if route is None:
            return jsonify({"error": "Invalid trail ID"}), 400

        # get route data and return it
        gpx = GPX(route.data)
        duration = gpx.get_duration()
        hours = int(duration / 3600)
        minutes = int((duration % 3600) / 60)
        seconds = int(duration % 60)

        # TODO: calorie calculation

        return jsonify({
            "name": route.name,
            "date": gpx.time.strftime("%d/%m/%Y"),
            "type": route.exercise_type,
            "distance": gpx.get_total_distance_km(),    # In Km
            "time": {"hours": hours, "minutes": minutes, "seconds": seconds},
            "speed": gpx.get_speed(),   # In Km/h
            "calories": 0,
        })

    except Exception as e:
        app.logger.error(f"Error fetching trail data: {e}")
        return jsonify({"error": "An error occurred while fetching the trail data"}), 500

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
    
    # Get the trail IDs from the request
    trail_ids = request.get_json().get("trailIDs")
    
    # Make a new folium map
    map_obj = folium.Map(location=[0, 0], zoom_start=2)
    
    if trail_ids:
        # Get the routes for the trail IDs
        routes = Route.query.filter(Route.id.in_(trail_ids), Route.user_id == user_id).all()
        
        if routes:
            bounds = []
            for route in routes:
                # Get the points from the route data
                gpx = GPX(route.data)
                points = []
                for track in gpx.gpx.tracks:
                    for segment in track.segments:
                        for point in segment.points:
                            # Add latitude and longitude of each point to the points list
                            points.append(tuple([point.latitude, point.longitude]))
                            bounds.append([point.latitude, point.longitude])
                # Add a polyline to the map object using the points list
                folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(map_obj)
            
            if bounds:
                # Fit the map to the bounds of the routes
                map_obj.fit_bounds(bounds)
    
    # Get the html representation of the map object
    map_html = map_obj._repr_html_()
    
    # Return map html as a json
    return jsonify({"mapHtml": map_html})

@bp.route('/zoom-to-trail', methods=['POST'])
@jwt_required()
@membership_required
def zoom_to_trail():
    """
    Zooms to a specific trail on a map. 
    Similar to get_selected_trails_map, but zooms to a specific trail.

    Returns:
        A json containing the html representation (repr) of the map.
    """
    
    user_id = get_current_user().id
    trail_id = request.get_json().get("trailID")
    selected_trail_ids = request.get_json().get("selectedTrailIDs")
    
    #Error handling 
    if not trail_id:
        return jsonify({"error": "No trail ID provided"}), 400
    
    if not selected_trail_ids:
        return jsonify({"error": "No selected trail IDs provided"}), 400
    
    routes = Route.query.filter(Route.id.in_(selected_trail_ids), Route.user_id == user_id).all()
    
    if not routes:
        return jsonify({"error": "No valid routes found"}), 400
    
    zoom_route = next((route for route in routes if route.id == trail_id), None)
    
    if not zoom_route:
        return jsonify({"error": "Invalid trail ID"}), 400
    
    map_obj = folium.Map(location=[0, 0], zoom_start=2)
    
    # Essentially: use bounds to define where to zoom 
    bounds = []
    for route in routes:
        gpx = GPX(route.data)
        points = []
        for track in gpx.gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append(tuple([point.latitude, point.longitude]))
                    bounds.append([point.latitude, point.longitude])
        folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(map_obj)
    
    zoom_points = []
    zoom_gpx = GPX(zoom_route.data)
    for track in zoom_gpx.gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                zoom_points.append(tuple([point.latitude, point.longitude]))
    
    if zoom_points:
        map_obj.fit_bounds([zoom_points[0], zoom_points[-1]])
    elif bounds:
        map_obj.fit_bounds(bounds)
    
    map_html = map_obj._repr_html_()
    
    return jsonify({"mapHtml": map_html})

@bp.route('/delete', methods=['POST'])
@jwt_required()
@membership_required
def delete_trail():
    try:
        user_id = get_current_user().id
        # Get trail id from request data
        data = request.get_json()
        trail_id = data.get("trailID")

        if trail_id is None:
            return jsonify({"error": "Missing trail ID"}), 400

        # Check if route exists and belongs to user
        route = Route.query.filter_by(id=trail_id, user_id=user_id).first()
        if route is None:
            return jsonify({"error": "Invalid trail ID"}), 400

        # Delete route from database, easier than old filter method
        db.session.delete(route)
        db.session.commit()

        # Success message
        return jsonify({"message": f"Route {trail_id} successfully deleted"}), 200

    except Exception as e:
        # Log error and return error message
        app.logger.error(f"Error deleting trail: {e}")
        return jsonify({"error": "An error occurred while deleting the trail"}), 500

@bp.route('/download', methods=['GET'])
@jwt_required()
@membership_required
def download_trail():
    # download a trail from the database

    # recieve user ID and trail ID
    user_id = get_current_user().id
    trail_id = request.get_json().get("trailID")

    # ensure route ID is valid
    route = Route.query.filter_by(id=trail_id).first()
    if route == None or route.user_id != user_id:
        return jsonify({"error": "Invalid trail ID"}), 400

    return jsonify({
        "data": route.data
    })

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
    return jsonify({
        "trailID": routeID,
    })

