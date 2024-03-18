from flask_jwt_extended import create_access_token
from app import app
import pytest
from tests.conf import client
from app.db_functions import *

def test_get_friends_success(client):
    delete_all(Friend)
    delete_all(User)
    
    headers = get_test_user_headers("u1", "pwd")
    user_1 = User.query.filter_by(username="u1").first()
    create_user("u2", "pwd")
    user_2 = User.query.filter_by(username="u2").first()
    create_user("u3", "pwd")
    user_3 = User.query.filter_by(username="u3").first()

    create_friendship(user_1.id, user_2.id)
    create_friendship(user_1.id, user_3.id)

    response = client.get("/get_friends", headers=headers)
    assert response.status_code == 200
    assert len(user_1.friends()) == 2
    assert len(user_2.friends()) == 1
    assert len(user_3.friends()) == 1

def test_get_friends_empty(client):
    delete_all(Friend)
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")
    user = User.query.filter_by(username="u1").first()

    response = client.get("/get_friends", headers=headers)
    assert response.status_code == 200
    assert len(user.friends()) == 0

def test_add_friend_success(client):
    delete_all(Friend)
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")
    create_user("u2", "pwd")
    user_2 = User.query.filter_by(username="u2").first()

    response = client.post("/add_friend", data={"userID2": user_2.id}, headers=headers)
    assert response.status_code == 200

def test_add_friend_duplicate(client):
    delete_all(Friend)
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")
    user_1 = User.query.filter_by(username="u1").first()
    create_user("u2", "pwd")
    user_2 = User.query.filter_by(username="u2").first()
    create_friendship(user_1.id, user_2.id)

    response = client.post("/add_friend", data={"userID2": user_2.id}, headers=headers)
    assert response.status_code == 400
    assert b"Friendship already exists" in response.data

def test_add_friend_missing_id(client):
    delete_all(Friend)
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")

    response = client.post("/add_friend", data={}, headers=headers)
    assert response.status_code == 400
    assert b"User 2 ID not given" in response.data

def test_add_friend_invalid_id(client):
    delete_all(Friend)
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")

    response = client.post("/add_friend", data={"userID2": -1}, headers=headers)
    assert response.status_code == 400
    assert b"Invalid ID" in response.data

def test_send_friend_request_success(client):
    delete_all(FriendRequest)
    delete_all(Friend)
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")
    user_1 = User.query.filter_by(username="u1").first()
    create_user("u2", "pwd")
    user_2 = User.query.filter_by(username="u2").first()

    response = client.post("/send_friend_request", data={"receiveUserID": user_2.id}, headers=headers)
    assert response.status_code == 200
    assert user_1 in user_2.incoming_friend_requests() and len(user_2.incoming_friend_requests()) == 1
    assert user_2 in user_1.outgoint_friend_requests() and len(user_1.outgoint_friend_requests()) == 1

def test_send_friend_request_duplicate(client):
    delete_all(FriendRequest)
    delete_all(Friend)
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")
    user_1 = User.query.filter_by(username="u1").first()
    create_user("u2", "pwd")
    user_2 = User.query.filter_by(username="u2").first()
    create_friend_request(user_1.id, user_2.id)

    response = client.post("/send_friend_request", data={"receiveUserID": user_2.id}, headers=headers)
    assert response.status_code == 400
    assert b"Friend request already exists" in response.data

def test_send_friend_request_already_friends(client):
    delete_all(FriendRequest)
    delete_all(Friend)
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")
    user_1 = User.query.filter_by(username="u1").first()
    create_user("u2", "pwd")
    user_2 = User.query.filter_by(username="u2").first()
    create_friendship(user_1.id, user_2.id)

    response = client.post("/send_friend_request", data={"receiveUserID": user_2.id}, headers=headers)
    assert response.status_code == 400
    assert b"Users are already friends" in response.data

def test_send_friend_request_missing_id(client):
    delete_all(FriendRequest)
    delete_all(Friend)
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")

    response = client.post("/send_friend_request", data={}, headers=headers)
    assert response.status_code == 400
    assert b"Receive user ID not given" in response.data

def test_send_friend_request_invalid_id(client):
    delete_all(FriendRequest)
    delete_all(Friend)
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")

    response = client.post("/send_friend_request", data={"receiveUserID": -1}, headers=headers)
    assert response.status_code == 400
    assert b"Invalid ID" in response.data