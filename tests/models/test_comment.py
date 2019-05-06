import pytest
from application.models.topic import Topic
from application.models.comment import Comment

def test_destroy(client):
    topic = Topic.create({ 'title': 'title1', 'body': 'body1' })
    comment = Comment.create({ 'topic_id': topic.id(), 'body': 'body1' })
    comment.destroy()
    assert(Topic.is_exists(topic.id()))
    assert(not Comment.is_exists(comment.id()))
