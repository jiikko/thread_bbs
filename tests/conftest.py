import pytest
import application

@pytest.fixture
def client():
    app = application.app
    app.testing = True
    with app.test_client() as client:
        yield client

# TODO before truncate table
