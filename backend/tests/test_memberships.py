from tests.conf import client
from flask_jwt_extended import create_access_token
from app.db_functions import *

def test_get_membership_options_success(client):
    delete_all(User)
    delete_all(MembershipPlan)

    headers = get_test_user_headers("u1", "pwd", membership=False)
    user_id = User.query.filter_by(username="u1").first().id
    m1_id = create_membership_plan("Plan 1", "Weekly", 7.00)
    m2_id = create_membership_plan("Plan 2", "Monthly", 24.00)
    set_user_membership_plan(user_id, m1_id)
    assert len(MembershipPlan.query.all()) == 2

    response = client.get("/membership/get-options", headers=headers)
    assert response.status_code == 200
    assert len(response.json["membershipOptions"]) == 2
    assert {"id": m1_id, "name": "Plan 1", "regularity": "Weekly", "price": 7, "isCurrentPlan": True} in response.json["membershipOptions"]
    assert {"id": m2_id, "name": "Plan 2", "regularity": "Monthly", "price": 24, "isCurrentPlan": False} in response.json["membershipOptions"]

def test_get_membership_options_not_authenticated(client):
    response = client.get("/membership/get-options")
    assert response.status_code == 401

def test_check_membership_success(client):
    delete_all(User)
    delete_all(MembershipPlan)

    headers = get_test_user_headers("u1", "pwd", membership=False)
    user_id = User.query.filter_by(username="u1").first().id
    membership_id = create_membership_plan("Paid", "Weekly", 7.00)
    create_membership_plan("Free", "N/A", 0)
    set_user_membership_plan(user_id, membership_id)
    assert len(MembershipPlan.query.all()) == 2

    response = client.get("/membership/get-current", headers=headers)
    assert response.status_code == 200
    assert response.json["membership"] == {"id": membership_id, "name": "Paid", "regularity": "Weekly", "price": 7.00}

def test_check_membership_no_membership(client):
    delete_all(User)
    delete_all(MembershipPlan)

    headers = get_test_user_headers("u1", "pwd", False)

    response = client.get("/membership/get-current", headers=headers)
    assert response.status_code == 200
    assert response.json["membership"] == None

def test_check_membership_free_membership(client):
    delete_all(User)
    delete_all(MembershipPlan)

    headers = get_test_user_headers("u1", "pwd", False)
    user_id = User.query.filter_by(username="u1").first().id
    create_membership_plan("Paid", "Weekly", 7.00)
    membership_id = create_membership_plan("Free", "N/A", 0)
    set_user_membership_plan(user_id, membership_id)
    assert len(MembershipPlan.query.all()) == 2

    response = client.get("/membership/get-current", headers=headers)
    assert response.status_code == 200
    assert response.json["membership"] == None

def test_check_membership_not_authenticated(client):
    response = client.get("/membership/get-current")
    assert response.status_code == 401

def test_cancel_membership_no_membership(client):
    delete_all(User)
    delete_all(MembershipPlan)

    headers = get_test_user_headers("u1", "pwd", membership=False)
    user = User.query.filter_by(username="u1").first()

    delete_user_membership(user.id)
    assert len(MembershipPlan.query.all()) == 0
    assert user.membership_id == None
    
    response = client.get("/membership/cancel", headers=headers)
    assert response.status_code == 400
    assert b"User is not a member" in response.data

def test_cancel_membership_not_authenticated(client):
    response = client.get("/membership/cancel")
    assert response.status_code == 401