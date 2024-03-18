from flask_jwt_extended import create_access_token
from app import app
import pytest
from tests.conf import client
from app.db_functions import *

def test_get_trails_success(client):
    delete_all(Route)
    delete_all(User)
    
    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    r1 = create_route_from_file("example_data/track1.gpx", "Trail 1", "Running", user_id)
    r2 = create_route_from_file("example_data/track2.gpx", "Trail 2", "Running", user_id)

    response = client.get("/get_trails", headers=headers)
    assert response.status_code == 200
    assert r1 in response.json["trails"] and r2 in response.json["trails"]

def test_get_trails_not_authenticated(client):
    response = client.get("/get_trails")
    assert response.status_code == 401

def test_get_trail_data_success(client):
    delete_all(Route)
    delete_all(User)
    
    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    route_id = create_route_from_file("example_data/track1.gpx", "Trail 1", "Running", user_id)

    response = client.get("/get_trail_data", json={"trailID": route_id}, headers=headers)
    assert response.status_code == 200
    assert response.json["name"] == "Trail 1"
    assert str(response.json["date"]) == "2013-06-11 10:00:00+00:00"
    assert int(response.json["distance"]) == 25
    assert response.json["time"] == {"hours": 0, "minutes": 49, "seconds": 40}
    assert int(response.json["speed"]) == 30
    assert response.json["calories"] == 0
    assert response.json["gpx"] == Route.query.filter_by(id=route_id).first().data

def test_get_trail_data_not_authenticated(client):
    response = client.get("/get_trail_data", json={"trailID": -1})
    assert response.status_code == 401

def test_get_trail_data_success(client):
    # TODO: fails sometimes with GPXXMLSyntaxException
    
    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    create_route_from_file("example_data/track1.gpx", "Trail 1", "Running", user_id)
    
    route_id = Route.query.filter_by(user_id=user_id, name="Trail 1").first().id

    response = client.get("/get_trail_data", json={"trailID": route_id}, headers=headers)
    assert response.status_code == 200
    assert response.json["time"] == {"hours": 0, "minutes": 49, "seconds": 40}
    assert response.json["time"] == {"hours": 0, "minutes": 49, "seconds": 40}
    assert response.json["calories"] == 0

def test_get_overall_stats_not_authenticated(client):
    response = client.get("/get_overall_stats")
    assert response.status_code == 401

# TODO
# def test_delete_trail_success(client):
#     delete_all(Route)
#     delete_all(User)

#     headers = get_test_user_headers("u1", "pwd")
#     user_id = User.query.filter_by(username="u1").first().id

#     r1_id = create_route_from_file("example_data/track1.gpx", "Route 1", "Walking", user_id)
#     create_route_from_file("example_data/track2.gpx", "Route 2", "Running", user_id)

#     assert len(Route.query.filter_by(user_id=user_id).all()) == 2
#     response = client.post("/delete_trail", data={"trailID": r1_id}, headers=headers)
#     assert response.status_code == 200
#     assert len(Route.query.filter_by(user_id=user_id).all()) == 1
#     assert Route.query.filter_by(user_id=user_id).first().name == "Route 2"

def test_delete_trail_invalid_id(client):
    delete_all(Route)
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")
    response = client.post("/delete_trail", data={"trailID": -1}, headers=headers)
    assert response.status_code == 400

def test_delete_trail_not_authenticated(client):
    response = client.post("/delete_trail", data={"trailID": -1})
    assert response.status_code == 401