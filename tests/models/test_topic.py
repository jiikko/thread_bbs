import pytest
from application.models.topic import Topic

def test_new_topic():
    topic = Topic({ 'title': 'fi', 'body': 'body' })
    assert 'fi', topic.title
    assert 'body', topic.body
