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
        pass

    def is_new_record(self):
        return self.id() == None

    def update(self, attrs={}):
        if self.is_new_record():
            return self

        values = []
        for key in attrs:
            self.attrs[key] = attrs[key]
            values.append('%s = "%s"' % (key, attrs[key]))
        # TODO escape for sql injection
        sql = "update topics set title = %s, body = %s where id = %s"
        sql = "update topics set "
        sql = sql + ', '.join(values)
        sql = sql + '  where id = %s' % self.id()
        with transaction() as cursor:
            cursor.execute(sql)
        return self

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
    def create(cls, attrs):
        instance = cls(attrs)
        columns = []
        values = []
        for key in instance.attrs:
            columns.append(key)
            values.append('"%s"' % instance.attrs[key])
        # TODO escape for sql injection
        sql = 'insert into topics (' + ', '.join(columns) + ') '
        sql = sql + 'values (' + ', '.join(values) + ')'
        with transaction() as cursor:
            cursor.execute(sql)
            instance.attrs['id'] = int(get_db().insert_id())
        return instance

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
        logging.info(cursor._last_executed)
    except:
        import traceback
        traceback.print_exc()
        print 'ocurret error in transaction'
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
