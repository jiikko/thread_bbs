import MySQLdb
import os
import contextlib
import logging
import application
from flask import g

def fetch_all_topics(where=None, limit=None):
    if where:
        sql = "select * from topics where %s" % (where)
    else:
        sql = "select * from topics"
    if limit:
        sql += (' limit %d' % limit)
    result = None
    with conn() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
    return result

def find_topic(id):
    where_clause = 'id = %s' % id
    return fetch_all_topics(where=where_clause, limit=1)[0]

def insert_topics(title=None, body=None):
    sql = "insert into topics(title, body) values(%s, %s)"
    with conn() as cursor:
        cursor.execute(sql, [title, body])

def update_topic(id, title=None, body=None):
    sql = "update topics set title = %s, body = %s where id = %s"
    with conn() as cursor:
        cursor.execute(sql, [title, body, id])

def destroy_topic(id):
    pass

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = conn()
    return db

# use `with` when call conn()!!
# ex) with MySQLdb.connect(**args) as cur:
#        cur.execute("INSERT INTO pokos (id, poko_name) VALUES (%s, %s)", (id, poko_name))
def conn():
    if application.app.config.get('TESTING'):
        logging.debug('environment: test')
        MYSQL_CONFIG = {
            'host': os.getenv("MYSQL_HOST", "127.0.0.1"),
            'user': 'root',
            'passwd':  '',
            'db': 'thread_bbs_test',
            'charset': 'utf8mb4',
        }
    else:
        logging.debug('environment: development')
        MYSQL_CONFIG = {
            'host': os.getenv("MYSQL_HOST", "127.0.0.1"),
            'user': 'root',
            'passwd':  '',
            'db': 'thread_bbs_development',
            'charset': 'utf8mb4',
        }
    return MySQLdb.connect(**MYSQL_CONFIG)
