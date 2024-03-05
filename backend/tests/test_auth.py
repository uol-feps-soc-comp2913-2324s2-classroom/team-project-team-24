from tests.conf import client
from flask_jwt_extended import create_access_token

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    
def test_unauthorised_login(client):
    response = client.post('/auth/login', json={'username': 'u1', 'password': 'pwd1'})
    assert response.status_code == 401
    assert response.json['message'] == 'Unauthorized'
    
def test_authorised_login(client):
    response = client.post('/auth/login', json={'username': 'u1', 'password': 'pwd'})
    assert response.status_code == 201
    
def test_unauthorised_logout(client):
    response = client.get('/auth/logout')
    assert response.status_code == 405
