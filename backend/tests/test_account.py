from flask_jwt_extended import create_access_token
from app import app
import pytest
from tests.conf import client
from app.db_functions import *
import datetime

def test_get_account_details_success(client):
    delete_all(MembershipPlan)
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")
    user = User.query.filter_by(username="u1").first()
    user.gender = "Male"
    user.age = 25
    db.session.commit()
    membership_id = create_membership_plan("Plan 1", "Monthly", 25)
    set_user_membership_plan(user.id, membership_id)

    response = client.get("/account/get-details", headers=headers)
    assert response.status_code == 200
    assert response.json["name"] == "u1"
    assert response.json["membershipTier"] == "Plan 1"
    assert response.json["gender"] == "Male"
    assert response.json["age"] == 25
    assert response.json["paymentRegularity"] == "Monthly"

def test_get_account_details_no_membership(client):
    delete_all(MembershipPlan)
    delete_all(User)
    User.query.delete()
    db.session.commit()

    headers = get_test_user_headers("u1", "pwd")
    user = User.query.filter_by(username="u1").first()
    user.gender = "Male"
    user.age = 13
    db.session.commit()

    response = client.get("/account/get-details", headers=headers)
    assert response.status_code == 200
    assert response.json["name"] == "u1"
    assert response.json["membershipTier"] == None
    assert response.json["gender"] == "Male"
    assert response.json["age"] == 13
    assert response.json["paymentRegularity"] == None

def test_get_account_details_few_details(client):
    delete_all(MembershipPlan)
    delete_all(User)
    User.query.delete()
    db.session.commit()

    headers = get_test_user_headers("u1", "pwd")

    response = client.get("/account/get-details", headers=headers)
    assert response.status_code == 200
    assert response.json["name"] == "u1"
    assert response.json["membershipTier"] == None
    assert response.json["gender"] == None
    assert response.json["age"] == None
    assert response.json["paymentRegularity"] == None

def test_get_account_details_not_authenticated(client):
    response = client.get("/account/get-details")
    assert response.status_code == 401

def test_change_password_success(client):
    delete_all(User)

    headers = get_test_user_headers("u1", "pwd")
    response = client.post("/account/change-password", data={"password": "abc"}, headers=headers)
    assert response.status_code == 200

    user = User.query.filter_by(username="u1").first()
    encode = "abc".encode('utf-8')
    assert bcrypt.checkpw(encode, user.password)

def test_get_account_details_missing_password(client):
    headers = get_test_user_headers("u1", "pwd")
    response = client.post("/account/change-password", data={}, headers=headers)
    assert response.status_code == 400
    assert b"Missing new password" in response.data 

def test_get_account_details_not_authenticated(client):
    response = client.post("/account/change-password")
    assert response.status_code == 401

def test_delete_account_success(client):
    delete_all(User)
    
    headers = get_test_user_headers("u1", "pwd")
    assert len(User.query.filter_by(username="u1").all()) == 1

    response = client.get("/account/delete", headers=headers)
    assert response.status_code == 200
    assert len(User.query.filter_by(username="u1").all()) == 0

def test_delete_account_not_authenticated(client):
    response = client.get("/account/delete")
    assert response.status_code == 401
