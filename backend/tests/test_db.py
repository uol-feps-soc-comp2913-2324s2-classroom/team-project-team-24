import pytest
from app.models import *
from app import app, db
import bcrypt
import string, random

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
    for i in range(1):
        uname = get_random_string(10)
        pwd = get_random_string(15)
        create_user(uname, pwd)
        assert User.authenticate(uname, pwd).username == uname
        assert User.authenticate(uname, 'pwd') == None
        delete_user(uname, pwd)
        
def test_friends():
    u1 = create_user(get_random_string(10), get_random_string(15))
    u2 = create_user(get_random_string(10), get_random_string(15))
    f = Friend(u1, u2)
    with app.app_context():
        db.session.add(f)
        db.session.commit()
        
    print(u1.get_friends())