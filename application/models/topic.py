from base_model import BaseModel

class Topic(BaseModel):
    TABLE_NAME = 'topics'

    @classmethod
    def row_to_instance(cls, row):
        return cls({ 'id': row[0], 'title': row[1], 'body': row[2] })

    def __init__(self, attrs={}):
        super(Topic, self).__init__(attrs)

    def title(self):
        return self.attrs['title']

    def body(self):
        return self.attrs['body']
