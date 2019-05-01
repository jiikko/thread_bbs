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

def insert_topics(title, body):
    conn = connect()
    cur = conn.cursor()
    cur.execute("insert into topics(title, body) values('aaaaaaa', 'bbbbbb')")
    conn.commit()
    cur.close()
    conn.close()

def execute(sql):
    conn = connect()
    cur = conn.cursor()
    result = cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    return result
