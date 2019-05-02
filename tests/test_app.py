import pytest
import application

def test_app(client):
    response = client.get('/')
    assert response.status_code == 200
