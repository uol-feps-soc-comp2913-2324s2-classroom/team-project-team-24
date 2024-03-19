from tests.conf import client
from flask_jwt_extended import create_access_token
from app.db_functions import *

def test_get_membership_options_success(client):
    delete_all(User)
    delete_all(MembershipPlan)

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    membership_id = create_membership_plan("Plan 1", "Weekly", 7.00)
    create_membership_plan("Plan 2", "Monthly", 24.00)
    set_user_membership_plan(user_id, membership_id)
    assert len(MembershipPlan.query.all()) == 2

    response = client.get("/get_membership_options", headers=headers)
    assert response.status_code == 200
    assert len(response.json["membershipOptions"]) == 2
    assert {"name": "Plan 1", "regularity": "Weekly", "price": 7, "isCurrentPlan": True} in response.json["membershipOptions"]
    assert {"name": "Plan 2", "regularity": "Monthly", "price": 24, "isCurrentPlan": False} in response.json["membershipOptions"]

def test_get_membership_options_not_authenticated(client):
    response = client.get("/get_membership_options")
    assert response.status_code == 401

def test_check_membership_success(client):
    delete_all(User)
    delete_all(MembershipPlan)

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    membership_id = create_membership_plan("Paid", "Weekly", 7.00)
    create_membership_plan("Free", "N/A", 0)
    set_user_membership_plan(user_id, membership_id)
    assert len(MembershipPlan.query.all()) == 2

    response = client.get("/check_membership", headers=headers)
    assert response.status_code == 200
    assert response.json["membership"] == {"name": "Paid", "regularity": "Weekly", "price": 7.00}

def test_check_membership_no_membership(client):
    delete_all(User)
    delete_all(MembershipPlan)

    headers = get_test_user_headers("u1", "pwd")

    response = client.get("/check_membership", headers=headers)
    assert response.status_code == 200
    assert response.json["membership"] == None

def test_check_membership_free_membership(client):
    delete_all(User)
    delete_all(MembershipPlan)

    headers = get_test_user_headers("u1", "pwd")
    user_id = User.query.filter_by(username="u1").first().id
    create_membership_plan("Paid", "Weekly", 7.00)
    membership_id = create_membership_plan("Free", "N/A", 0)
    set_user_membership_plan(user_id, membership_id)
    assert len(MembershipPlan.query.all()) == 2

    response = client.get("/check_membership", headers=headers)
    assert response.status_code == 200
    assert response.json["membership"] == None

def test_check_membership_not_authenticated(client):
    response = client.get("/check_membership")
    assert response.status_code == 401