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
    """
    Create a new route
    Args:
        file_path (str): location of the .gpx file on disk
        name (str): name of the route
        exercise_type (str): exercise type of the route
        user_id (int): user to register the route to

    Returns:
        (int): new route ID
    """

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

def check_for_friendship(user_id: int, friend_id: int):
    friend = User.query.filter_by(id=friend_id).first()
    return friend in User.query.filter_by(id=user_id).first().friends()

def create_friendship(user1_id: int, user2_id: int):
    # check if friendship already exists
    if not check_for_friendship(user1_id, user2_id):
        # create new friendship
        db_add(Friend(user1_id, user2_id))

def check_for_friend_request(from_id: int, to_id: int):
    to_user = User.query.filter_by(id=to_id).first()
    return to_user in User.query.filter_by(id=from_id).first().outgoing_friend_requests()

def create_friend_request(from_id: int, to_id: int):
    # check if friendship already exists
    if not check_for_friend_request(from_id, to_id):
        # create new friendship
        db_add(FriendRequest(from_user=from_id, to_user=to_id))

def remove_friend_request(user1_id: int, user2_id: int):
    if check_for_friend_request(user1_id, user2_id):
        FriendRequest.query.filter_by(from_user_id=user1_id, to_user_id=user2_id).delete()
    if check_for_friend_request(user2_id, user1_id):
        FriendRequest.query.filter_by(from_user_id=user2_id, to_user_id=user1_id).delete()
    db.session.commit()

def accept_friend_request(user1_id: int, user2_id: int):
    create_friendship(user1_id, user2_id)
    remove_friend_request(user1_id, user2_id)

def check_for_user_in_group(user_id: int, group_id: int):
    group = Group.query.filter_by(id=group_id).first()
    user = User.query.filter_by(id=user_id).first()
    return user in group.members

def add_user_to_group(user_id: int, group_id: int):
    if not check_for_user_in_group(user_id, group_id):
        group = Group.query.filter_by(id=group_id).first()
        user = User.query.filter_by(id=user_id).first()
        group.members.append(user)

def create_new_group(user_id: int, name: str):
    group = Group(name=name)
    db.session.add(group)
    db.session.commit()

    add_user_to_group(user_id, Group.query.filter_by(name=name).first().id)
    return group.id

def delete_group(group_id: int):
    Group.query.filter_by(id=group_id).delete()
    db.session.commit()

def reset_groups():
    for group in Group.query.all():
        delete_group(group.id)

def get_user_group_ids(user_id: int) -> list:
    user = User.query.filter_by(id=user_id).first()

    groups = []
    for group in user.groups:
        groups.append(group.id)

    return groups

def get_user_group_names(user_id: int) -> list:
    user = User.query.filter_by(id=user_id).first()

    groups = []
    for group in user.groups:
        groups.append(group.name)

    return groups