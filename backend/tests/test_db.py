import pytest
from app.models import User
from app import app, db
import bcrypt
import string, random

def create_user(username, password):
    u = User()
    u.username = username
    pwd = password
    encode = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    u.password = bcrypt.hashpw(encode, salt)
    
    with app.app_context():
        db.session.add(u)
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

def test_user_creation():
    for i in range(10):
        uname = get_random_string(10)
        pwd = get_random_string(15)
        create_user(uname, pwd)
        u = User.authenticate(uname, pwd)
        print(u)
        assert u.username == uname, f"Expected {uname}, but u is nonetype"
        assert User.authenticate(uname, 'pwd') == None
        delete_user(uname, pwd)