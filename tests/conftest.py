import pytest
import application
from flask import Flask

@pytest.fixture
def client():
    app = application.app
    app.testing = True
    clean_tables(application)

    with app.test_client() as client:
        yield client

    clean_tables(application)

def clean_tables(application):
    with application.rdb.conn() as cursor:
        cursor.execute('truncate table topics')
