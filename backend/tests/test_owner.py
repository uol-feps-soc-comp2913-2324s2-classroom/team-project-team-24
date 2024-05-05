from flask_jwt_extended import create_access_token
from app import app
import pytest
from tests.conf import client
from app.db_functions import *

def test_get_owner_membership_data_success(client):
    delete_all(User)
    delete_all(MembershipPlan)
    
    headers = get_test_user_headers("u1", "pwd", is_owner=True)
    m1 = MembershipPlan.query.filter_by(id=create_membership_plan("A", "weekly", 2.50)).first()
    m2 = MembershipPlan.query.filter_by(id=create_membership_plan("B", "monthly", 25.00)).first()
    m3 = MembershipPlan.query.filter_by(id=create_membership_plan("C", "yearly", 250.00)).first()
    create_user("u2", "pwd")
    u2 = User.query.filter_by(username="u2").first()
    create_user("u3", "pwd")
    u3 = User.query.filter_by(username="u3").first()
    create_user("u4", "pwd")
    u4 = User.query.filter_by(username="u4").first()
    set_user_membership_plan(u2.id, m1.id)
    set_user_membership_plan(u3.id, m2.id)
    set_user_membership_plan(u4.id, m3.id)

    response = client.get("/owner/get-owner-membership-data", headers=headers)
    assert response.status_code == 200
    assert response.json["numUsers"] == 3
    assert {"id": m1.id, "name": m1.name, "payment_regularity": m1.payment_regularity, "cost": m1.cost, "numMembers": 1} in response.json["memberships"]
    assert {"id": m2.id, "name": m2.name, "payment_regularity": m2.payment_regularity, "cost": m2.cost, "numMembers": 1} in response.json["memberships"]
    assert {"id": m3.id, "name": m3.name, "payment_regularity": m3.payment_regularity, "cost": m3.cost, "numMembers": 1} in response.json["memberships"]

    delete_all(User)
    delete_all(MembershipPlan)

def test_get_owner_membership_data_not_authenticated(client):
    response = client.get("/owner/get-owner-membership-data")
    assert response.status_code == 401

def test_get_owner_membership_data_not_owner(client):
    headers = get_test_user_headers("u1", "pwd", is_owner=False)
    response = client.get("/owner/get-owner-membership-data", headers=headers)
    assert response.status_code == 400
    assert b"Not authorised" in response.data

def test_get_future_revenue_not_authenticated(client):
    response = client.get("/owner/get-future-revenue")
    assert response.status_code == 401

def test_get_future_revenue_not_owner(client):
    headers = get_test_user_headers("u1", "pwd", is_owner=False)
    response = client.get("/owner/get-future-revenue", headers=headers)
    assert response.status_code == 400
    assert b"Not authorised" in response.data
