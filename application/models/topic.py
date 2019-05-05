from base_model import BaseModel

class Topic(BaseModel):
    TABLE_NAME = 'topics'

    @classmethod
    def row_to_dict(cls, row):
        return cls({ 'id': row[0], 'title': row[1], 'body': row[2] })

    def __init__(self, attrs={}):
        super(Topic, self).__init__(attrs)

    def title(self):
        self['title']

    def body(self):
        self['body']
