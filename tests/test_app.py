import pytest
import application

def test_app(client):
    response = client.get('/')
    assert response.status_code == 200

def test_config_using_db(client):
    import config
    assert config.env.MYSQL_DB == 'thread_bbs_test'
