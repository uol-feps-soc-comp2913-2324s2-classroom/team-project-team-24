from app import db
import bcrypt

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    salt = db.Column(db.String(60))   

class Friend(db.Model):
    fk_user_1 = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    fk_user_2 = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)

class FriendRequest(db.Model):
    fk_from_user = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    fk_to_user = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)

class MembershipPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    cost = db.Column(db.Float)
    payment_regularity = db.Column(db.String(32))
    members = db.relationship("User", backref="membershipplan")

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    salt = db.Column(db.String(60))
    profile_picture = db.Column(db.LargeBinary)
    sex = db.Column(db.String(32))
    date_of_birth = db.Column(db.DateTime)
    friends = db.relationship("Friend", backref="user",
                              primaryjoin="and_(User.id==Friend.fk_user_1 or User.id==Friend.fk_user_2)")
    friendRequests = db.relationship("FriendRequest", backref="user",
                                     primaryjoin="and_(User.id==FriendRequest.fk_to_user)")
    fk_membership = db.Column(db.Integer, db.ForeignKey(MembershipPlan.id))

    @staticmethod
    def authenticate(username, password):
        result = User.query.filter_by(username=username).all()
        if len(result) > 0:
            u = result[0]
            encode = password.encode('utf-8')
            if bcrypt.checkpw(encode, u.password):
                return u

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    name = db.Column(db.String(128))
    exercise_type = db.Column(db.String(64))
    fk_user = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

class UserInGroup(db.Model):
    fk_user = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    fk_group = db.Column(db.Integer, db.ForeignKey("group.id"), primary_key=True)

class RouteInGroup(db.Model):
    fk_route = db.Column(db.Integer, db.ForeignKey("route.id"), primary_key=True)
    fk_group = db.Column(db.Integer, db.ForeignKey("group.id"), primary_key=True)
