import pytest
from application.models.topic import Topic
from application.models.comment import Comment
from tests.helpers import topic as topic_helper

def test_all(client):
    topic1 = Topic.create({ 'title': 'title1', 'body': 'body1' })
    topic2 = Topic.create({ 'title': 'title2', 'body': 'body2' })
    topics = Topic.all()
    assert len(topics) == 2
    assert Topic.find(topic1.id()).title() == topic1.title()
    assert Topic.find(topic1.id()).body() == topic1.body()
    assert Topic.find(topic2.id()).title() == topic2.title()
    assert Topic.find(topic2.id()).body() == topic2.body()

    topics = Topic.all(limit=1)
    assert len(topics) == 1

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

def test_destroy(client):
    topic = Topic.create({ 'title': 'title2', 'body': 'body2' })
    topic.destroy()
    assert(not Topic.is_exists(topic.id()))

def test_destroy_with_comment(client):
    topic = Topic.create({ 'title': 'title1', 'body': 'body1' })
    comment1 = Comment.create({ 'topic_id': topic.id(), 'body': 'body1' })
    comment2 = Comment.create({ 'topic_id': topic.id(), 'body': 'body2' })
    topic.destroy()
    assert(not Topic.is_exists(topic.id()))
    assert(not Comment.is_exists(comment1.id()))
    assert(not Comment.is_exists(comment2.id()))
