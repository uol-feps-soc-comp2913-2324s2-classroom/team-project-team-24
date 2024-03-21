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

def test_get_group_trails_success(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_1_id = User.query.filter_by(username="u1").first().id
    create_user("u2", "pwd")
    user_2_id = User.query.filter_by(username="u2").first().id

    r1 = create_route_from_file("example_data/track1.gpx", "Trail 1", "Running", user_1_id)
    r1_id = Route.query.filter_by(name="Trail 1", user_id=user_1_id).first().id
    r2 = create_route_from_file("example_data/track2.gpx", "Trail 2", "Running", user_2_id)
    r2_id = Route.query.filter_by(name="Trail 2", user_id=user_2_id).first().id
    group_id = create_new_group(user_1_id, "Group")
    add_user_to_group(user_2_id, group_id)
    add_route_to_group(r1_id, group_id)
    add_route_to_group(r2_id, group_id)

    response = client.get("/get_group_trails", json={"groupID": group_id}, headers=headers)
    assert response.status_code == 200
    assert len(response.json["trails"]) == 2
    assert r1_id in response.json["trails"] and r2_id in response.json["trails"]

def test_get_group_trails_empty(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    group_id = create_new_group(user_id, "Group")

    response = client.get("/get_group_trails", json={"groupID": group_id}, headers=headers)
    assert response.status_code == 200
    assert response.json["trails"] == []

def test_get_group_trails_missing_id(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")

    response = client.get("/get_group_trails", json={}, headers=headers)
    assert response.status_code == 400
    assert b"Missing group ID" in response.data

def test_get_group_trails_invalid_id(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")

    response = client.get("/get_group_trails", json={"groupID": -1}, headers=headers)
    assert response.status_code == 400
    assert b"Invalid group ID" in response.data

def test_get_group_trails_not_in_group(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_1_id = User.query.filter_by(username="u1").first().id
    create_user("u2", "pwd")
    user_2_id = User.query.filter_by(username="u2").first().id

    create_route_from_file("example_data/track1.gpx", "Trail 1", "Running", user_2_id)
    route_id = Route.query.filter_by(name="Trail 1", user_id=user_2_id).first().id
    group_id = create_new_group(user_2_id, "Group")
    add_route_to_group(route_id, group_id)

    response = client.get("/get_group_trails", json={"groupID": group_id}, headers=headers)
    assert response.status_code == 400
    assert b"User is not in this group" in response.data

def test_get_group_members_success(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_1 = User.query.filter_by(username="u1").first()
    create_user("u2", "pwd")
    user_2 = User.query.filter_by(username="u2").first()
    create_user("u3", "pwd")
    user_3 = User.query.filter_by(username="u3").first()

    group_id = create_new_group(user_1.id, "Team")
    add_user_to_group(user_2.id, group_id)

    response = client.get("/get_group_members", json={"groupID": group_id}, headers=headers)
    assert response.status_code == 200
    assert len(response.json["members"]) == 2
    assert {user_1.id, user_2.id} == {response.json["members"][0]["id"], response.json["members"][1]["id"]}

def test_get_group_members_invalid_id(client):
    reset_groups()
    
    headers = get_test_user_headers("u1", "pwd")

    response = client.get("/get_group_members", json={"groupID": -1}, headers=headers)
    assert response.status_code == 400
    assert b"Invalid group ID" in response.data

def test_get_group_members_missing_id(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")

    response = client.get("/get_group_members", json={}, headers=headers)
    assert response.status_code == 400
    assert b"Missing group ID" in response.data

def test_get_group_members_not_in_group(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_1_id = User.query.filter_by(username="u1").first().id
    create_user("u2", "pwd")
    user_2_id = User.query.filter_by(username="u2").first().id
    group_id = create_new_group(user_2_id, "Group")

    response = client.get("/get_group_members", json={"groupID": group_id}, headers=headers)
    assert response.status_code == 400
    assert b"User is not in this group" in response.data

def test_leave_group_success(client):
    reset_groups()
    
    headers = get_test_user_headers("u1", "pwd")
    user_1_id = User.query.filter_by(username="u1").first().id
    create_user("u2", "pwd")
    user_2_id = User.query.filter_by(username="u2").first().id
    group_id = create_new_group(user_1_id, "Group")
    add_user_to_group(user_2_id, group_id)

    assert len(Group.query.filter_by(id=group_id).first().members) == 2
    response = client.post("/leave_group", data={"groupID": group_id}, headers=headers)
    assert response.status_code == 200
    assert len(Group.query.filter_by(id=group_id).first().members) == 1
    assert not check_for_user_in_group(user_1_id, group_id)
    assert check_for_user_in_group(user_2_id, group_id)

def test_leave_group_delete_group(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    group_id = create_new_group(user_id, "Group")

    assert len(User.query.filter_by(id=user_id).first().groups) == 1
    assert len(Group.query.filter_by(id=group_id).first().members) == 1
    response = client.post("/leave_group", data={"groupID": group_id}, headers=headers)
    assert response.status_code == 200
    assert len(User.query.filter_by(id=user_id).first().groups) == 0

def test_leave_group_not_in_group(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_1_id = User.query.filter_by(username="u1").first().id
    create_user("u2", "pwd")
    user_2_id = User.query.filter_by(username="u2").first().id
    group_id = create_new_group(user_2_id, "Group")

    assert len(Group.query.filter_by(id=group_id).first().members) == 1
    assert not check_for_user_in_group(user_1_id, group_id)
    assert check_for_user_in_group(user_2_id, group_id)

    response = client.post("/leave_group", data={"groupID": group_id}, headers=headers)
    assert response.status_code == 400
    assert b"User is not in this group" in response.data 
    assert len(Group.query.filter_by(id=group_id).first().members) == 1
    assert not check_for_user_in_group(user_1_id, group_id)
    assert check_for_user_in_group(user_2_id, group_id)

def test_leave_group_invalid_id(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")

    response = client.post("/leave_group", data={"groupID": -1}, headers=headers)
    assert response.status_code == 400
    assert b"Invalid group ID" in response.data

def test_leave_group_missing_id(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")

    response = client.post("/leave_group", data={}, headers=headers)
    assert response.status_code == 400
    assert b"Missing group ID" in response.data

def test_add_route_to_group_success(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    route = create_route_from_file("example_data/track1.gpx", "Trail 1", "Running", user_id)
    route_id = Route.query.filter_by(name="Trail 1", user_id=user_id).first().id
    group_id = create_new_group(user_id, "Group")

    assert len(Group.query.filter_by(id=group_id).first().routes) == 0
    response = client.post("/add_route_to_group", data={"routeID": route_id, "groupID": group_id}, headers=headers)
    assert response.status_code == 200
    assert len(Group.query.filter_by(id=group_id).first().routes) == 1
    assert Group.query.filter_by(id=group_id).first().routes[0].id == route_id

def test_add_route_to_group_route_already_in_group(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    route = create_route_from_file("example_data/track1.gpx", "Trail 1", "Running", user_id)
    route_id = Route.query.filter_by(name="Trail 1", user_id=user_id).first().id

    group_id = create_new_group(user_id, "Group")
    add_route_to_group(route_id, group_id)

    response = client.post("/add_route_to_group", data={"routeID": route_id, "groupID": group_id}, headers=headers)
    assert response.status_code == 400
    assert b"Route already in group" in response.data

def test_add_route_to_group_user_not_in_group(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_1_id = User.query.filter_by(username="u1").first().id
    create_user("u2", "pwd")
    user_2_id = User.query.filter_by(username="u2").first().id
    route = create_route_from_file("example_data/track1.gpx", "Trail 1", "Running", user_1_id)
    route_id = Route.query.filter_by(name="Trail 1", user_id=user_1_id).first().id

    group_id = create_new_group(user_2_id, "Group")

    response = client.post("/add_route_to_group", data={"routeID": route_id, "groupID": group_id}, headers=headers)
    assert response.status_code == 400
    assert b"User not in this group" in response.data

def test_add_route_to_group_route_doesnt_belong_to_user(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_1_id = User.query.filter_by(username="u1").first().id
    create_user("u2", "pwd")
    user_2_id = User.query.filter_by(username="u2").first().id
    route = create_route_from_file("example_data/track1.gpx", "Trail 1", "Running", user_2_id)
    route_id = Route.query.filter_by(name="Trail 1", user_id=user_2_id).first().id

    group_id = create_new_group(user_1_id, "Group")

    response = client.post("/add_route_to_group", data={"routeID": route_id, "groupID": group_id}, headers=headers)
    assert response.status_code == 400
    assert b"Route does not belong to this user" in response.data

def test_add_route_to_group_invalid_route(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    group_id = create_new_group(user_id, "Group")

    response = client.post("/add_route_to_group", data={"routeID": -1, "groupID": group_id}, headers=headers)
    assert response.status_code == 400
    assert b"Invalid route ID" in response.data

def test_add_route_to_group_invalid_group(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    route = create_route_from_file("example_data/track1.gpx", "Trail 1", "Running", user_id)
    route_id = Route.query.filter_by(name="Trail 1", user_id=user_id).first().id

    response = client.post("/add_route_to_group", data={"routeID": route_id, "groupID": -1}, headers=headers)
    assert response.status_code == 400
    assert b"Invalid group ID" in response.data

def test_add_route_to_group_missing_id(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")

    response = client.post("/add_route_to_group", data={}, headers=headers)
    assert response.status_code == 400
    assert b"Missing route ID and/or group ID" in response.data

def test_add_friend_to_group_success(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    group_id = create_new_group(user_id, "Group")
    create_user("u2", "pwd")
    friend_id = User.query.filter_by(username="u2").first().id
    create_friendship(user_id, friend_id)

    assert len(Group.query.filter_by(id=group_id).first().members) == 1
    assert check_for_user_in_group(user_id, group_id)
    assert not check_for_user_in_group(friend_id, group_id)

    response = client.post("/add_friend_to_group", data={"friendID": friend_id, "groupID": group_id}, headers=headers)
    assert response.status_code == 200
    assert len(Group.query.filter_by(id=group_id).first().members) == 2
    assert check_for_user_in_group(user_id, group_id)
    assert check_for_user_in_group(friend_id, group_id)

def test_add_friend_to_group_friend_already_in_group(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    group_id = create_new_group(user_id, "Group")
    create_user("u2", "pwd")
    friend_id = User.query.filter_by(username="u2").first().id
    create_friendship(user_id, friend_id)
    add_user_to_group(friend_id, group_id)

    assert len(Group.query.filter_by(id=group_id).first().members) == 2
    assert check_for_user_in_group(user_id, group_id)
    assert check_for_user_in_group(friend_id, group_id)

    response = client.post("/add_friend_to_group", data={"friendID": friend_id, "groupID": group_id}, headers=headers)
    assert response.status_code == 400
    assert b"Friend already in group" in response.data
    assert len(Group.query.filter_by(id=group_id).first().members) == 2
    assert check_for_user_in_group(user_id, group_id)
    assert check_for_user_in_group(friend_id, group_id)

def test_add_friend_to_group_user_not_in_group(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    create_user("u2", "pwd")
    friend_id = User.query.filter_by(username="u2").first().id
    create_friendship(user_id, friend_id)
    create_user("u3", "pwd")
    user_2_id = User.query.filter_by(username="u3").first().id
    create_friendship(user_2_id, friend_id)
    
    group_id = create_new_group(friend_id, "Group")

    response = client.post("/add_friend_to_group", data={"friendID": user_2_id, "groupID": group_id}, headers=headers)
    assert response.status_code == 400
    assert b"User not in this group" in response.data

def test_add_friend_to_group_users_arent_friends(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    create_user("u2", "pwd")
    user_2_id = User.query.filter_by(username="u2").first().id
    group_id = create_new_group(user_id, "Group")

    response = client.post("/add_friend_to_group", data={"friendID": user_2_id, "groupID": group_id}, headers=headers)
    assert response.status_code == 400
    assert b"Users are not friends" in response.data

def test_add_friend_to_group_invalid_friend(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    group_id = create_new_group(user_id, "Group")

    response = client.post("/add_friend_to_group", data={"friendID": -1, "groupID": group_id}, headers=headers)
    assert response.status_code == 400
    assert b"Invalid friend ID" in response.data

def test_add_friend_to_group_invalid_group(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    create_user("u2", "pwd")
    friend_id = User.query.filter_by(username="u2").first().id
    create_friendship(user_id, friend_id)

    response = client.post("/add_friend_to_group", data={"friendID": friend_id, "groupID": -1}, headers=headers)
    assert response.status_code == 400
    assert b"Invalid group ID" in response.data

def test_add_friend_to_group_missing_id(client):
    reset_groups()

    headers = get_test_user_headers("u1", "pwd")

    response = client.post("/add_friend_to_group", data={}, headers=headers)
    assert response.status_code == 400
    assert b"Missing friend ID and/or group ID" in response.data