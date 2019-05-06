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
        sql = "update %s set " % type(self).TABLE_NAME
        sql = sql + ', '.join(values)
        sql = sql + '  where id = %s' % self.id()
        with rdb.transaction() as cursor:
            cursor.execute(sql)
        return self

    def destroy(self):
        sql = 'delete from %s where id = %%s' % type(self).TABLE_NAME
        with rdb.transaction() as cursor:
            cursor.execute(sql, [self.id()])
        return True

    @classmethod
    def find(cls, id):
        return cls.all(where=('id = %d' % id), limit=1)[0]

    @classmethod
    def is_exists(cls, id):
        result = cls.all(where=('id = %d' % id), limit=1)
        return len(result) == 1

    @classmethod
    def all(cls, where=None, limit=None):
        sql = "select * from %s" % cls.TABLE_NAME
        if where:
            sql = sql + " where %s" % where
        if limit:
            sql += (' limit %d' % limit)
        result = None
        with rdb.transaction() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            result = map(lambda(row): (cls.row_to_instance(row)), rows)
        return result

    @classmethod
    def create(cls, attrs):
        instance = cls(attrs)
        columns = []
        values = []
        for key in instance.attrs:
            columns.append(key)
            values.append('"%s"' % instance.attrs[key])
        # TODO escape for sql injection
        sql = 'insert into %s (' % cls.TABLE_NAME
        sql = sql + ', '.join(columns) + ') '
        sql = sql + 'values (' + ', '.join(values) + ')'
        with rdb.transaction() as cursor:
            cursor.execute(sql)
            instance.attrs['id'] = int(rdb.get_db().insert_id())
        return instance

    @classmethod
    def row_to_instance(cls, row):
       pass

    @classmethod
    def column_table():
        pass
