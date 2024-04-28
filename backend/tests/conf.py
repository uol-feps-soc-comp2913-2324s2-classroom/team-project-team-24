from app import app, db
import pytest
from app.db_functions import clear_db

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client
    clear_db()