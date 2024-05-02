from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import stripe

app = Flask(__name__)
CORS(app)

stripe.api_key = "sk_test_51PBedsRq4UQ9omwxmLSrDcG9TL8bmhprG5G7LFiCszpoghpS2QTZjjimEO4571P4h40WQNgv8pOhiVXHvi2wuGq60093lrCCiF"
# Load environment variables from .env file (used for SECRET_KEY)
load_dotenv()

# If I don't include this, I get an error when running db_create.py
# It's about the app running outside of the context of the application instance
app.app_context().push()

app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.endpoints import auth, core, trails, friends, groups, memberships, account, owner

app.register_blueprint(auth.bp)
app.register_blueprint(core.bp)
app.register_blueprint(trails.bp)
app.register_blueprint(friends.bp)
app.register_blueprint(groups.bp)
app.register_blueprint(memberships.bp)
app.register_blueprint(account.bp)
app.register_blueprint(owner.bp)


jwt = JWTManager(app)

from app import views, models

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

# print([x.username for x in models.User.query.all()])
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return models.User.query.filter_by(id=identity).one_or_none()