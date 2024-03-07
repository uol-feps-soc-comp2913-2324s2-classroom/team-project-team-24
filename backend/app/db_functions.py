from app.models import *
from app import app, db
import bcrypt
import string, random

def db_add(*args):
    with app.app_context():
        for arg in args:
            db.session.add(arg)
        db.session.commit()

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

def get_routes_by_user_id(id: int) -> list:
    """
    Get all routes belonging to a certain user
    Args:
        id (int): User ID

    Returns:
        (list): list of Routes
    """

    return Route.query.filter_by(user_id=id)