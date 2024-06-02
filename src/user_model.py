import mongoengine as me
from werkzeug.security import generate_password_hash
from datetime import datetime


class User(me.Document):
    givenName = me.StringField(required=True)
    surName = me.StringField(required=True)
    email = me.StringField(required=True, unique=True)
    password = me.StringField(required=True)
    created_at = me.StringField()
    updated_at = me.StringField()   
    meta = {"collection": "users", "db_alias": "angular-fp"}

    def save(self, *args, **kwargs):
        if (self.created_at):
            self.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        else:
            self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

        self.password = generate_password_hash(self.password)
        
        super(User, self).save(*args, **kwargs)
      