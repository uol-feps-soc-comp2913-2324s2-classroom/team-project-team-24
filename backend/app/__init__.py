from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app)

# Load environment variables from .env file (used for SECRET_KEY)
load_dotenv()

# If I don't include this, I get an error when running db_create.py
# It's about the app running outside of the context of the application instance
app.app_context().push()

app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.endpoints import auth, core, trails, friends, groups, memberships, account

app.register_blueprint(auth.bp)
app.register_blueprint(core.bp)
app.register_blueprint(trails.bp)
app.register_blueprint(friends.bp)
app.register_blueprint(groups.bp)
app.register_blueprint(memberships.bp)
app.register_blueprint(account.bp)


jwt = JWTManager(app)

from app import views, models

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return models.User.query.filter_by(id=identity).one_or_none()