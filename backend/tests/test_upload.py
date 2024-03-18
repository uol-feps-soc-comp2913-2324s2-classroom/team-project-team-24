from flask_jwt_extended import create_access_token
from app import app
import pytest
from tests.conf import client
from app.db_functions import *

def test_successful_upload(client):
    delete_all(Route)    
    
    headers = get_test_user_headers('u1', 'pwd')

    with open("example_data/track1.gpx", "rb") as file:
        response = client.post('/upload', headers=headers,
                                data={'file': (file, "track1.gpx"), 'routeName': 'test_route', 'exerciseType': 'test_exercise'})
        assert response.status_code == 200


def test_no_file_upload(client):
    delete_all(Route)

    headers = get_test_user_headers('u1', 'pwd')
    response = client.post('/upload', headers=headers,
                            data={'routeName': 'test_route', 'exerciseType': 'test_exercise'})
    assert response.status_code == 400
    assert b"No file uploaded" in response.data


def test_invalid_file_upload(client):
    delete_all(Route)

    headers = get_test_user_headers('u1', 'pwd')

    with open("example_data/waypoint1.gpx", "rb") as file:
        response = client.post('/upload', headers=headers,
                                data={'file': (file, "track1.gpx"), 'routeName': 'test_route', 'exerciseType': 'test_exercise'})
        assert response.status_code == 400
        assert b"Invalid file contents" in response.data


def test_duplicate_route_name(client):
    delete_all(Route)

    headers = get_test_user_headers('u1', 'pwd')

    with open("example_data/track1.gpx", "rb") as file:
        response = client.post('/upload', headers=headers,
                                data={'file': (file, "track1.gpx"), 'routeName': 'test_route', 'exerciseType': 'test_exercise'})
    
    with open("example_data/track1.gpx", "rb") as file:
        response = client.post('/upload', headers=headers,
                                data={'file': (file, "track1.gpx"), 'routeName': 'test_route', 'exerciseType': 'test_exercise'})
        assert response.status_code == 400
        assert b"Route name already used" in response.data


def test_empty_route_name(client):
    delete_all(Route)

    headers = get_test_user_headers('u1', 'pwd')

    with open("example_data/track1.gpx", "rb") as file:
        response = client.post('/upload', headers=headers,
                                data={'file': (file, "track1.gpx"), 'routeName': '', 'exerciseType': 'test_exercise'})

        assert response.status_code == 200

    test_user_id = User.query.filter_by(username='u1').first().id
    routes = get_routes_by_user_id(test_user_id)

    # assume this is the only route, as they were deleteed
    assert routes[0].name == "My route #1"
