import pytest
import application

@pytest.fixture
def main():
    pass

def test_app():
    app = application.app
    app.testing = True
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
