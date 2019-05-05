import MySQLdb
import os
import contextlib
import logging
from flask import g, current_app

def fetch_all_topics(where=None, limit=None):
    if where:
        sql = "select * from topics where %s" % (where)
    else:
        sql = "select * from topics"
    if limit:
        sql += (' limit %d' % limit)
    result = None
    with transaction() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
    return result

def destroy_topic(id):
    sql = 'delete from topics where id = %s'
    with transaction() as cursor:
        cursor.execute(sql, [id])


# NOTE MySQL connection is closed by @app.teardown_request
@contextlib.contextmanager
def transaction():
    db = get_db()
    try:
        cursor = db.cursor()
        yield(cursor)
    except:
        cursor.close()
        db.rollback()
    else:
        cursor.close()
        db.commit()

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = conn()
    return db

# use `with` when call conn() if don't close in teardown_db!!
# ex) with MySQLdb.connect(**args) as cur:
#        cur.execute("INSERT INTO pokos (id, poko_name) VALUES (%s, %s)", (id, poko_name))
def conn():
    if current_app.config.get('TESTING'):
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
