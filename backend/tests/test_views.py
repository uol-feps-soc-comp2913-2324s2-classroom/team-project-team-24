from app import app
import pytest
from tests.conf import client


def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Greetings from the API!'

def test_add_route(client):
    response = client.post('/add', json={'a': 5, 'b': 3})
    assert response.status_code == 201
    assert response.json == {'status': 'success', 'addition': 8}