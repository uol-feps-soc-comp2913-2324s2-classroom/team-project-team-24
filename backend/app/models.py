from app import db
import bcrypt
from sqlalchemy import or_

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

class FriendRequest(db.Model):
    from_user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    to_user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    
    from_user = db.relationship("User", foreign_keys=[from_user_id])
    to_user = db.relationship("User", foreign_keys=[to_user_id])

class MembershipPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    cost = db.Column(db.Float)
    payment_regularity = db.Column(db.String(32))
    members = db.relationship("User", backref="membership_plan", lazy="dynamic")

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

    @staticmethod
    def authenticate(username, password):
        result = User.query.filter_by(username=username).all()
        if len(result) > 0:
            u = result[0]
            encode = password.encode('utf-8')
            if bcrypt.checkpw(encode, u.password):
                return u
            
    def friends(self):
        table = Friend.query.filter(or_(Friend.fk_user_1 == self.id, Friend.fk_user_2 == self.id)).all()
        friends = []
        for entry in table:
            if entry.fk_user_1 == self.id:
                friends.append(entry.user_2)
            else:
                friends.append(entry.user_1)
        return friends
    
    def outgoint_friend_requests(self):
        return
    
    def incoming_friend_request(self):
        return

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
