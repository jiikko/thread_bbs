from base_model import BaseModel

class Topic(BaseModel):
    def __init__(self, attrs={}):
        super(Topic, self).__init__(attrs)

    def title(self):
        self['title']

    def body(self):
        self['body']
