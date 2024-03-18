from flask_jwt_extended import create_access_token
from app import app
import pytest
from tests.conf import client
from app.db_functions import *

def test_get_groups_success(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    group_id = create_new_group(user_id, "Group")

    response = client.get("/get_groups", headers=headers)
    assert response.status_code == 200
    assert len(response.json["groups"]) == 1
    assert response.json["groups"] == [{"id": group_id, "name": "Group"}]

def test_get_groups_empty(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")

    response = client.get("/get_groups", headers=headers)
    assert response.status_code == 200
    assert len(response.json["groups"]) == 0
    assert response.json["groups"] == []

def test_create_group_success(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id

    response = client.post("/create_group", data={"groupName": "Group A"}, headers=headers)
    assert response.status_code == 200
    assert len(get_user_group_ids(user_id)) == 1
    assert "Group A" in get_user_group_names(user_id)
    response_2 = client.post("/create_group", data={"groupName": "Group B"}, headers=headers)
    assert response_2.status_code == 200
    assert len(get_user_group_ids(user_id)) == 2
    assert "Group A" in get_user_group_names(user_id) and "Group B" in get_user_group_names(user_id)

def test_create_group_missing_name(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id

    response = client.post("/create_group", data={}, headers=headers)
    assert response.status_code == 400
    assert len(get_user_group_ids(user_id)) == 0
    assert b"Missing group name" in response.data
