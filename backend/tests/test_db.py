import pytest
from app.models import *
from app import app, db
import bcrypt
import string, random
from app.db_functions import get_random_string, create_user, delete_all, delete_user, db_add

"""
CURRENTLY TESTS HAVE NO EDGE CASES/ERROR CHECKING!
"""

# ----------------------------------------------------------------
# TESTS START

def test_user_creation():
    """
    Creates 10 users, and then tries to authenticate each one.
    """
    for i in range(1):
        uname = get_random_string(10)
        pwd = get_random_string(15)
        create_user(uname, pwd)
        assert User.authenticate(uname, pwd).username == uname
        assert User.authenticate(uname, 'pwd') == None
        delete_user(uname, pwd)
        
def test_friends():
    """
    Tests frienships by:
        - Creates 3 users
        - u1 friends u2 and u3
        - Check for all 3 that they have the correct friends
    """
    delete_all(Friend)
    delete_all(User)
    u1 = create_user('test3', 'pwd')
    u2 = create_user('test4', 'pwd')
    u3 = create_user('test5', 'pwd')
    
    f1 = Friend(u1, u2)
    f2 = Friend(u1, u3)
    
    db_add(f1, f2)
        
    u1 = User.authenticate('test3', 'pwd')
    u2 = User.authenticate('test4', 'pwd')
    u3 = User.authenticate('test5', 'pwd')
    
    assert u1.friends() == {u2, u3}
    assert u2.friends() == {u1}
    assert u3.friends() == {u1}
 
def test_friend_requests():
    """
    Tests friend requests by:
        - Creates 3 users
        - u1 requests u2
        - u2 requests u3
        - checks all incoming and outgoing fields for all users
    """
    delete_all(User)
    delete_all(FriendRequest)
    u1 = create_user('u1', 'pwd')
    u2 = create_user('u2', 'pwd')
    u3 = create_user('u3', 'pwd')
    
    r1 = FriendRequest(u1, u2)
    r2 = FriendRequest(u2, u3)
    
    db_add(r1, r2)
        
    u1 = User.authenticate('u1', 'pwd')
    u2 = User.authenticate('u2', 'pwd')
    u3 = User.authenticate('u3', 'pwd')
    
    assert u1.outgoing_friend_requests() == {u2}
    assert u1.incoming_friend_requests() == set()
    assert u2.outgoing_friend_requests() == {u3}
    assert u2.incoming_friend_requests() == {u1}
    assert u3.outgoing_friend_requests() == set()
    assert u3.incoming_friend_requests() == {u2}
    
def test_membership():
    """
    Test membership by:
        - Creates 3 membership categories
        - Creates 4 users
        - Assigns users to categories
        - Checks both that the MembershipPlan.members.all() contains the right users
        - And User.membership is the correct membership
    """
    delete_all(MembershipPlan)
    delete_all(User)
    
    m1 = MembershipPlan()
    m1.name = "Test"
    m2 = MembershipPlan()
    m2.name = "Test2"
    m3 = MembershipPlan()
    m3.name = "Test3"
    
    u1 = create_user('u1', 'pwd')
    u2 = create_user('u2', 'pwd')
    u3 = create_user('u3', 'pwd')
    u4 = create_user('u4', 'pwd')
    
    u1.membership = m1
    u2.membership = m1
    u3.membership = m1
    u4.membership = m2
    
    db_add(m1, m2, m3, u1, u2, u3, u4)
        
    m1, m2, m3 = MembershipPlan.query.all()
    u1 = User.authenticate('u1', 'pwd')
    u2 = User.authenticate('u2', 'pwd')
    u3 = User.authenticate('u3', 'pwd')
    u4 = User.authenticate('u4', 'pwd')
    
    assert m1.members.all() == [u1, u2, u3]
    assert u1.membership == m1
    assert u2.membership == m1
    assert m2.members.all() == [u4]
    assert m3.members.all() == []

def test_users_and_routes_in_groups():
    """
    Tests putting users and routes in groups by:
        - Create 3 users, 3 routes, 2 groups
        - u1 has routes r1, r2
        - u3 has route r3
        - g1.users = [u1, u2, u3]
        - g1.routes = [r2]
        - g2.users = [u1, u3]
        - g2.routes = [r1, r2, r3]
        - Checks all is then correct (from group, user, and route perspective)
    """
    delete_all(User)
    delete_all(Group)
    delete_all(Route)
    
    u1 = create_user('u1', 'pwd')
    u2 = create_user('u2', 'pwd')
    u3 = create_user('u3', 'pwd')
    
    r1 = Route()
    r2 = Route()
    r3 = Route()
    r1.user = u1
    r2.user = u1
    r3.user = u3
    db_add(r1, r2, r3)
    
    g1 = Group()
    g1.name = "test1"
    g1.members = [u1, u2, u3]
    g1.routes = [r2]
    g2 = Group()
    g2.name = "test2"
    g2.members = [u1, u3]
    g2.routes = [r1, r2, r3]
    
    db.session.add(g1)
    db.session.add(g2)
    db.session.commit()
    
    g1, g2 = Group.query.all()
    u1 = User.authenticate('u1', 'pwd')
    u2 = User.authenticate('u2', 'pwd')
    u3 = User.authenticate('u3', 'pwd')
    r1, r2, r3 = Route.query.all()

    assert g1.members == [u1, u2, u3]
    assert g2.members == [u1, u3]
    assert u1.groups == [g1, g2]
    assert u2.groups == [g1]
    assert u3.groups == [g1, g2]
    assert g1.routes == [r2]
    # assert g2.routes == [r1, r2, r3]
    assert r1.groups == [g2]
    assert r2.groups == [g1, g2]
    assert r3.groups == [g2]
