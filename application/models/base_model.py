from application import rdb

class BaseModel(object):
    def __init__(self, attrs={}):
        self.attrs = attrs

    @classmethod
    def find(cls, id):
        sql = 'select * from %s' % cls.TABLE_NAME
        row = None
        with rdb.transaction() as cursor:
            cursor.execute(sql)
            row = cursor.fetchone()
        return cls(cls.row_to_dict(row))

    @classmethod
    def row_to_dict(cls, row):
       pass
