import pytest
import application

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
    application.rdb.insert_topics(title=title, body=body)
    topic_id = None
    with application.rdb.conn() as cursor:
        cursor.execute("select * from topics where title = %s", [title])
        row = cursor.fetchall()[0]
        topic_id = row[0]

    response = client.get('/topics/%s/edit' % topic_id)
    assert response.status_code == 200
    actual = response.get_data()
    assert title in actual
    assert body in actual

def test_post_topics_edit(client):
    title = 'test_get_topics_edit_title'
    body = 'test_get_topics_edit_body'
    application.rdb.insert_topics(title=title, body=body)
    topic_id = None
    with application.rdb.conn() as cursor:
        cursor.execute("select * from topics where title = %s", [title])
        row = cursor.fetchall()[0]
        topic_id = row[0]
    response = client.post('/topics/%s/edit' % topic_id, data={ 'title': 'titletitle', 'body': 'bodybody' })
    assert response.status_code == 302

    row = None
    with application.rdb.conn() as cursor:
        cursor.execute("select * from topics where id = %s", [topic_id])
        row = cursor.fetchall()[0]

    assert 'titletitle' == row[1]
    assert 'bodybody' == row[2]
