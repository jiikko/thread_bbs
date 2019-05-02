import pytest
import application


def test_get_topics_new(client):
    response = client.get('/topics/new')
    assert response.status_code == 200

# TODO be impliment validation
def test_post_topics_new_when_invalid():
    pass

def test_post_topics_new(client):
    expected = "nodogaitai_11"
    response = client.post('/topics/new', data={ 'title': expected, 'body': expected })
    assert response.status_code == 302
    response = client.get('/topics/')
    actual = response.get_data()
    assert expected in actual

def test_get_topics_index(client):
    response = client.get('/topics/')
    assert response.status_code == 200
