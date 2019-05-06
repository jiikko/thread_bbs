from base_model import BaseModel

class Comment(BaseModel):
    TABLE_NAME = 'comments'
    COLUMNS = {
            'id': 'int',
            'topic_id': 'int',
            'body': 'string',
            }

    @classmethod
    def row_to_instance(cls, row):
        return cls({ 'id': row[0], 'topic_id': row[1], 'body': row[2] })

    def body(self):
        return self.attrs.get('body', None)
