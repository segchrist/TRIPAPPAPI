from mongoengine import StringField, IntField, Document

class PathModel(Document):
    path_id = StringField()
    user_id = StringField()
    name = StringField()
