import MySQLdb
import os

def connect():
    db = MySQLdb.connect(
            host=os.getenv("MYSQL_HOST", "127.0.0.1"),
            user='root',
            passwd='',
            db='thread_bbs_development',
            charset='utf8mb4')
    return db

def select():
    pass

def fetch_all_topics():
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from topics")
    result = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return result

def insert_topics(title=None, body=None):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
            "insert into topics(title, body) values('%s', '%s')" % (title, body))
    conn.commit()
    cur.close()
    conn.close()

def find_topic(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute('select * from topics where id = %s limit 1' % id)
    result = cur.fetchall()[0]
    conn.commit()
    cur.close()
    conn.close()
    return result

def execute(sql):
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    return result
