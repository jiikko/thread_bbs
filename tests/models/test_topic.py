import pytest
from application.models.topic import Topic
from tests.helpers import topic as topic_helper

def test_new(client):
    topic = Topic({ 'title': 'fi', 'body': 'body' })
    assert 'fi', topic.title
    assert 'body', topic.body

def test_find(client):
    topic = Topic({ 'title': 'title2', 'body': 'body2' })
    topic.save()
    topic = Topic.find(topic.id())
    assert 'title2', topic.title()
    assert 'body2', topic.body()
    assert type(topic) == Topic

def test_save(client):
    topic = Topic({ 'title': 'fi', 'body': 'body' })
    assert topic.id() == None
    topic.save()
    assert topic.title() == 'fi'
    assert topic.body() == 'body'
    topic = Topic.find(topic.id())
    assert topic.title() == 'fi'
    assert topic.body() == 'body'
