import pytest
import application
from tests.helpers import topic as topic_helper
from application.models.topic import Topic

def test_get_topics_index(client):
    response = client.get('/topics/')
    assert response.status_code == 200

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

def test_get_topics_edit(client):
    title = 'test_get_topics_edit_title'
    body = 'test_get_topics_edit_body'
    topic = Topic.create({ 'title': title, 'body': body })

    response = client.get('/topics/%s/edit' % topic.id())
    assert response.status_code == 200
    actual = response.get_data()
    assert title in actual
    assert body in actual

def test_post_topics_edit(client):
    title = 'test_get_topics_edit_title'
    body = 'test_get_topics_edit_body'
    topic = Topic.create({ 'title': title, 'body': body })
    response = client.post('/topics/%s/edit' % topic.id(), data={ 'title': 'titletitle', 'body': 'bodybody' })
    assert response.status_code == 302

    response = client.get('/topics/%s' % topic.id())
    actual = response.get_data()
    assert 'titletitle' in actual
    assert 'bodybody' in actual

def test_post_topics_delete(client):
    topic = Topic.create({ 'title': 'title', 'body': 'body' })
    response = client.post('/topics/%s/delete' % topic.id(), data={ 'id': topic.id() })
    assert response.status_code == 302
    assert(not Topic.find(topic.id()))
