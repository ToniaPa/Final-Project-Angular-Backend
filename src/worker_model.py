import mongoengine as me
from datetime import datetime


class Address(me.EmbeddedDocument):
    street = me.StringField(required=True)
    number = me.StringField(required=True)
    city = me.StringField(required=True)
    country = me.StringField(required=True)
    zipCode = me.StringField(required=True)


class PhoneNumber(me.EmbeddedDocument):
    number = me.StringField(required=True)
    type = me.StringField(required=True)


class Worker(me.Document):
    givenName = me.StringField(required=True)
    surName = me.StringField(required=True)
    email = me.StringField(required=True, unique=True)
    afm = me.StringField(required=True, unique=True)
    phoneNumbers = me.ListField(me.EmbeddedDocumentField(PhoneNumber))
    address = me.EmbeddedDocumentField(Address)
    created_at = me.StringField()
    updated_at = me.StringField()
    meta = {"collection": "workers", "db_alias": "angular-fp"}

    def save(self, *args, **kwargs):
        if (self.created_at):
            self.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        else:
            self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')   
        
        super(Worker, self).save(*args, **kwargs)

