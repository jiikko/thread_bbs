import pytest
from application.models.topic import Topic
from tests.helpers import topic as topic_helper

def test_new(client):
    topic = Topic({ 'title': 'fi', 'body': 'body' })
    assert 'fi', topic.title
    assert 'body', topic.body

def test_find(client):
    topic_id = topic_helper.create_topic(title='title', body='body')['id']
    topic = Topic.find(topic_id)
    assert 'title', topic.title
    assert 'body', topic.body
    assert type(topic) == Topic

def test_save(client):
    topic = Topic({ 'title': 'fi', 'body': 'body' })
    assert topic.id() == None
    topic.save()
    assert type(topic.id()) == int
    assert type(Topic.find(topic.id())) == Topic
