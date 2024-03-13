from app import db, app
import bcrypt
from sqlalchemy import or_

# MANY TO MANY RELATIONSHIP TABLES
userInGroup = db.Table('user_in_group', db.Model.metadata,
                        db.Column('user_id', db.Integer, db.ForeignKey("user.id"), primary_key=True),
                        db.Column('group_id', db.Integer, db.ForeignKey("group.id"), primary_key=True))

routeInGroup = db.Table('route_in_group', db.Model.metadata,
                        db.Column('route_id', db.Integer, db.ForeignKey("route.id"), primary_key=True),
                        db.Column('group_id', db.Integer, db.ForeignKey("group.id"), primary_key=True))

# NORMAL ORM CLASSES
class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    salt = db.Column(db.String(60))   

class Friend(db.Model):
    user_1_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    user_2_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    
    user_1 = db.relationship("User", foreign_keys=[user_1_id])
    user_2 = db.relationship("User", foreign_keys=[user_2_id])
    
    def __init__(self, u1=None, u2=None):
        """
        Can be used to more easily define a friendship.
        Either the user ID or the user instance can be passed and it will set those values.

        Args:
            u1 (int/User, optional): The ID or instance of the first user in the friendship. Defaults to None.
            u2 (int/User, optional): The ID or instance of the second user in the friendship. Defaults to None.
        """
        if type(u1) == int:
            self.user_1_id = u1
            self.user_2_id = u2
        else:
            self.user_1 = u1
            self.user_2 = u2

class FriendRequest(db.Model):
    from_user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    to_user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    
    from_user = db.relationship("User", foreign_keys=[from_user_id])
    to_user = db.relationship("User", foreign_keys=[to_user_id])
    
    def __init__(self, from_user=None, to_user=None):
        """
        Can be used to more easily define a friend request.
        Either the user ID or the user instance can be passed and it will set those values.

        Args:
            from_user (int/User, optional): The ID or instance of the FROM user in the request. Defaults to None.
            to_user (int/User, optional): The ID or instance of the TO user in the request. Defaults to None.
        """
        if type(from_user) == int:
            self.from_user_id = from_user
            self.to_user_id = to_user
        else:
            self.from_user = from_user
            self.to_user = to_user

class MembershipPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    cost = db.Column(db.Float)
    payment_regularity = db.Column(db.String(32))
    
    # lazy="dynamic" means that to use this parameter, you need to call methods on it
    # like m.members.all() or m.members.first() etc.
    members = db.relationship("User", back_populates="membership", lazy="dynamic")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    salt = db.Column(db.String(60))
    profile_picture = db.Column(db.LargeBinary)
    sex = db.Column(db.String(32))
    date_of_birth = db.Column(db.DateTime)
    membership_id = db.Column(db.Integer, db.ForeignKey("membership_plan.id"))
    
    membership = db.relationship("MembershipPlan", foreign_keys=[membership_id])
    groups = db.relationship('Group', secondary=userInGroup, back_populates="members")
    
    def __init__(self, username=None, password=None):
        self.username = username
        if password is not None:
            self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def authenticate(username, password):
        """
        Gets the user with the given username and password, none otherwise.
        Is a static method so is called using User.authenticate, not called on an
        instance of the User class.

        Args:
            username (str): Username of the potential user
            password (str): Password of the potential user

        Returns:
            (User): The user if found, None otherwise
        """
        result = User.query.filter_by(username=username).all()
        if len(result) > 0:
            u = result[0]
            encode = password.encode('utf-8')
            if bcrypt.checkpw(encode, u.password):
                return u
        return None
            
    def friends(self):
        """
        Get all the friends of the user.

        Returns:
            (set): A set of all the user's friends (as User objects)
        """
        table = Friend.query.filter(or_(Friend.user_1 == self, Friend.user_2 == self)).all()
        friends = set()
        for entry in table:
            if entry.user_1 == self:
                friends.add(entry.user_2)
            else:
                friends.add(entry.user_1)
        return friends
    
    def outgoint_friend_requests(self):
        table = FriendRequest.query.filter(FriendRequest.from_user == self).all()
        outgoing_requests = set()
        for entry in table:
            outgoing_requests.add(entry.to_user)
            
        return outgoing_requests
    
    def incoming_friend_requests(self):
        table = FriendRequest.query.filter(FriendRequest.to_user == self).all()
        incoming_requests = set()
        for entry in table:
            incoming_requests.add(entry.from_user)
            
        return incoming_requests

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    name = db.Column(db.String(128))
    exercise_type = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    user = db.relationship('User', foreign_keys=[user_id])
    groups = db.relationship('Group', secondary=routeInGroup, back_populates="routes")

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    
    members = db.relationship('User', secondary=userInGroup, back_populates="groups")
    routes = db.relationship('Route', secondary=routeInGroup, back_populates="groups")



