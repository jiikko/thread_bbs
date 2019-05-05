from application import rdb

class BaseModel(object):
    def __init__(self, attrs={}):
        self.attrs = attrs

    def id(self):
        return self.attrs['id']

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
