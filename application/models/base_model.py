from flask import g, current_app
import logging
import MySQLdb
import os
import contextlib
from application import rdb

class BaseModel(object):
    def __init__(self, attrs={}):
        self.attrs = attrs

    def id(self):
        return self.attrs.get('id', None)

    def save(self):
        columns = []
        values = []
        for key in self.attrs:
            columns.append(key)
            value = self.attrs[key]
            values.append(key)
        # TODO escape for sql injection
        sql = 'insert into topics (' + ', '.join(columns) + ')'
        sql = sql + 'values (' + ', '.join(values) + ')'
        inserted_id = None
        with transaction() as cursor:
            cursor.execute(sql)
            cursor.execute('select last_insert_id()')
            inserted_id = int(cursor.fetchone()[0])
        self.attrs['id'] = inserted_id

    def is_new_record(self):
        pass

    @classmethod
    def find(cls, id):
        sql = 'select * from %s where id = %s' % (cls.TABLE_NAME, id)
        row = None
        with rdb.transaction() as cursor:
            cursor.execute(sql)
            row = cursor.fetchone()
        if row == None:
            return None
        return cls.row_to_instance(row)

    @classmethod
    def row_to_instance(cls, row):
       pass

    @classmethod
    def column_table():
        pass

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
