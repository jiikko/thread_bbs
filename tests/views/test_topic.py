import pytest
import application

@pytest.fixture
def main():
    pass

def test_get_topics_new():
    app = application.app
    app.testing = True
    client = app.test_client()
    response = client.get('/topics/new')
    assert response.status_code == 200

def test_post_topics_new_when_invalid():
    pass

def test_post_topics_new():
    app = application.app
    app.testing = True
    with app.test_client() as c:
        response = c.post('/topics/new', data={ 'title': "nodogaitai_11", 'body': "nodogaitai_11" })
        assert response.status_code == 302
        response = c.get('/topics/')
        assert 'nodogaitai_11' in str(response.get_data())

def test_get_topics_index():
    app = application.app
    app.testing = True
    client = app.test_client()
    response = client.get('/topics/')
    assert response.status_code == 200
