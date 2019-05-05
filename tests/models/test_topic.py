import pytest
from application.models.topic import Topic
from tests.helpers import topic as topic_helper

def test_all(client):
    pass

def test_new(client):
    topic = Topic({ 'title': 'fi', 'body': 'body' })
    assert 'fi', topic.title
    assert 'body', topic.body

def test_find(client):
    topic = Topic.create({ 'title': 'title2', 'body': 'body2' })
    topic = Topic.find(topic.id())
    assert 'title2', topic.title()
    assert 'body2', topic.body()
    assert type(topic) == Topic

def test_update(client):
    topic = Topic.create({ 'title': 'title2', 'body': 'body2' })
    assert 'title2', topic.title()
    assert 'body2', topic.body()
    topic.update({ 'title': 'title3', 'body': 'body3' })
    assert 'title3', topic.title()
    assert 'body3', topic.body()
    topic = Topic.find(topic.id())
    assert 'title3', topic.title()
    assert 'body3', topic.body()

def test_save(client):
    # TODO
    return
    topic = Topic({ 'title': 'fi', 'body': 'body' })
    assert topic.id() == None
    topic.save()
    assert topic.title() == 'fi'
    assert topic.body() == 'body'
    topic = Topic.find(topic.id())
    assert topic.title() == 'fi'
    assert topic.body() == 'body'

def test_destroy(client):
    topic = Topic.create({ 'title': 'title2', 'body': 'body2' })
    topic.destroy()
    assert(not Topic.is_exists(topic.id()))
