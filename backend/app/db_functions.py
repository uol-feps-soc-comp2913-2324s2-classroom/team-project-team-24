from app.models import *
from app import app, db
import bcrypt
import string, random
from flask_jwt_extended import create_access_token

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
    db_add(u)
    return u

def create_route_from_file(file_path, name, exercise_type, user_id):
    # ensure user ID is valid
    if User.query.filter_by(id=user_id).first() == None:
        return None

    # ensure user doesn't already have a route with this name
    for route in Route.query.filter_by(user_id=user_id):
        if route.name == name:
            return None

    with open(file_path, "r") as file:
        db_add(Route(data=file.read(), name=name, exercise_type=exercise_type, user_id=user_id))

    # return route ID
    return Route.query.filter_by(user_id=user_id, name=name).first().id

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

def get_test_user_headers(username, password):
    if User.query.filter_by(username=username).first() == None:
        create_user(username, password)
    
    test_user = User.query.filter_by(username=username).first()
    access_token = create_access_token(identity=test_user)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    return headers