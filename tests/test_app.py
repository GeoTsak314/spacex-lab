import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_create_resource():
    client = app.test_client()
    response = client.post('/resources', json={"name": "Oxygen", "quantity": 100})
    assert response.status_code == 201

def test_get_resources():
    client = app.test_client()
    client.post('/resources', json={"name": "Food", "quantity": 200})
    response = client.get('/resources')
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)
