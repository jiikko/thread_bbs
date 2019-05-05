import application
from application.models.topic import Topic

def create_topic(title=None, body=None):
    title = 'test_get_topics_edit_title'
    body = 'test_get_topics_edit_body'
    application.rdb.insert_topics(title=title, body=body)
    with application.rdb.conn() as cursor:
        cursor.execute("select * from topics where title = %s", [title])
        row = cursor.fetchone()
    topic = { 'id': row[0], 'title': row[1], 'body': row[2] }
    return topic

def is_exists_topic(id):
    return True if Topic.find(id) else False
