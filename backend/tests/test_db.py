import pytest
from app.models import *
from app import app, db
import bcrypt
import string, random

"""
CURRENTLY TESTS HAVE NO EDGE CASES/ERROR CHECKING!
"""

# ----------------------------------------------------------------
# Useful functions NOT TESTS
def hash_pwd(password):
    encode = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(encode, salt)

def create_user(username, password):
    u = User()
    u.username = username
    u.password = hash_pwd(password)
    
    with app.app_context():
        db.session.add(u)
        db.session.commit()
        
    return u

def delete_all(c):
    with app.app_context():
        for user in c.query.all():
            db.session.delete(user)
        db.session.commit()

def delete_user(username, password):
    with app.app_context():
        result = User.query.filter_by(username=username).all()
        if len(result) > 0:
            u = result[0]
            encode = password.encode('utf-8')
            if bcrypt.checkpw(encode, u.password):
                db.session.delete(u)
        db.session.commit()
    
def get_random_string(n):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for x in range(n))

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
    
    assert u1.outgoint_friend_requests() == {u2}
    assert u1.incoming_friend_requests() == set()
    assert u2.outgoint_friend_requests() == {u3}
    assert u2.incoming_friend_requests() == {u1}
    assert u3.outgoint_friend_requests() == set()
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
    
