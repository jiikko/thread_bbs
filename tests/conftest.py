import pytest
import application
from flask import Flask

@pytest.fixture
def client():
    app = application.app
    app.testing = True

    with app.test_request_context():
        clean_tables(application)
        with app.test_client() as client:
            yield client
        clean_tables(application)

def clean_tables(application):
    with application.rdb.get_db() as cursor:
        cursor.execute('truncate table topics')
