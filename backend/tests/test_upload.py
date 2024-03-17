from flask_jwt_extended import create_access_token
from app import app
import pytest
from tests.conf import client
from app.db_functions import *

def test_successful_upload(client):
    delete_all(Route)    
    
    if User.query.filter_by(username='uploadtest').first() == None:
        create_user('uploadtest', 'pwd')
    
    test_user = User.query.filter_by(username='uploadtest').first()
    access_token = create_access_token(identity=test_user)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    with open("example_data/track1.gpx", "rb") as file:
        response = client.post('/upload', headers=headers,
                                data={'file': (file, "track1.gpx"), 'routeName': 'test_route', 'exerciseType': 'test_exercise'})
        assert response.status_code == 200


def test_no_file_upload(client):
    delete_all(Route)

    if User.query.filter_by(username='uploadtest').first() == None:
        create_user('uploadtest', 'pwd')

    test_user = User.query.filter_by(username='uploadtest').first()
    access_token = create_access_token(identity=test_user)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    response = client.post('/upload', headers=headers,
                            data={'routeName': 'test_route', 'exerciseType': 'test_exercise'})
    assert response.status_code == 400
    assert b"No file uploaded" in response.data


def test_invalid_file_upload(client):
    delete_all(Route)

    if User.query.filter_by(username='uploadtest').first() == None:
        create_user('uploadtest', 'pwd')

    test_user = User.query.filter_by(username='uploadtest').first()
    access_token = create_access_token(identity=test_user)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    with open("example_data/waypoint1.gpx", "rb") as file:
        response = client.post('/upload', headers=headers,
                                data={'file': (file, "track1.gpx"), 'routeName': 'test_route', 'exerciseType': 'test_exercise'})
        assert response.status_code == 400
        assert b"Invalid file contents" in response.data


def test_duplicate_route_name(client):
    delete_all(Route)

    if User.query.filter_by(username='uploadtest').first() == None:
        create_user('uploadtest', 'pwd')

    test_user = User.query.filter_by(username='uploadtest').first()
    access_token = create_access_token(identity=test_user)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

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

    if User.query.filter_by(username='uploadtest').first() == None:
        create_user('uploadtest', 'pwd')

    test_user = User.query.filter_by(username='uploadtest').first()
    access_token = create_access_token(identity=test_user)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    with open("example_data/track1.gpx", "rb") as file:
        response = client.post('/upload', headers=headers,
                                data={'file': (file, "track1.gpx"), 'routeName': '', 'exerciseType': 'test_exercise'})

        assert response.status_code == 200

    routes = get_routes_by_user_id(test_user.id)

    # assume this is the only route, as they were deleteed
    assert routes[0].name == "My route #1"
