import pytest
import application

@pytest.fixture
def client():
    app = application.app
    app.testing = True
    clean_tables
    with app.test_client() as client:
        yield client

def clean_tables():
    with application.rdb.conn() as cursor:
        cursor.execute('truncate table topics')
