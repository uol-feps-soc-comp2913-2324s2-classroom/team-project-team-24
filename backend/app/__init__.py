from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

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

# from endpoints import auth

# app.register_blueprint(auth.bp)

from app import views, models
