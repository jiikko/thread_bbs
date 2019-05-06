import MySQLdb
import os
import contextlib
import logging
from flask import g, current_app

# NOTE MySQL connection is closed by @app.teardown_request
@contextlib.contextmanager
def transaction():
    db = get_db()
    db.begin()
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
    import config
    logging.debug('environment: %s', config.current_env())
    MYSQL_CONFIG = {
        'host': config.env.MYSQL_HOST,
        'user': config.env.MYSQL_USER,
        'passwd':  config.env.MYSQL_PASSWD,
        'db': config.env.MYSQL_DB,
        'charset': config.env.MYSQL_CHARSET,
    }
    return MySQLdb.connect(**MYSQL_CONFIG)
