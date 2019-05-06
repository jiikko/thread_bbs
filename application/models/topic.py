from base_model import BaseModel
from comment import Comment

class Topic(BaseModel):
    TABLE_NAME = 'topics'
    COLUMNS = {
            'id': 'int',
            'title': 'string',
            'body': 'string',
            }

    @classmethod
    def row_to_instance(cls, row):
        return cls({ 'id': row[0], 'title': row[1], 'body': row[2] })

    def __init__(self, attrs={}):
        super(Topic, self).__init__(attrs)

    def title(self):
        return self.attrs.get('title', None)

    def body(self):
        return self.attrs.get('body', None)

    def comments(self):
        return Comment.all(where='topic_id = %s' % self.id())
