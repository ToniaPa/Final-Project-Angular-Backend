import mongoengine as me
from datetime import datetime

class Timesheet(me.Document):    
    dateOfWork = me.DateField(required=True, unique=True)
    workerGivenName = me.StringField(required=True)
    workerSurName = me.StringField(required=True)    
    workerAfm = me.StringField(required=True, unique=True)
    clientBrandName = me.StringField(required=True)    
    clientAfm = me.StringField(required=True, unique=True)    
    typeOfWork = me.StringField(required=True, unique=True)    
    hourFrom = me.DateTimeField(required=True)
    hourTo = me.DateTimeField(required=True)    
    additionalInfo = me.StringField()
    created_at = me.StringField()
    updated_at = me.StringField()
    meta = {"collection": "timesheets", "db_alias": "angular-fp"}

    def save(self, *args, **kwargs):
        if self.created_at:
            self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        super(Timesheet, self).save(*args, **kwargs)


# class HourRecord(me.EmbeddedDocument):
#     hour = me.IntField(required=True)
#     minute = me.IntField(required=True)

# class WorkerClientWorkHours(me.EmbeddedDocument):
#     workerGivenName = me.StringField(required=True)
#     workerSurName = me.StringField(required=True)    
#     workerAfm = me.StringField(required=True, unique=True)
#     clientBrandName = me.StringField(required=True)    
#     clientAfm = me.StringField(required=True, unique=True)    
#     typeOfWork = me.StringField(required=True, unique=True)
#     hourFrom = me.EmbeddedDocumentField(HourRecord)
#     hourTo = me.EmbeddedDocumentField(HourRecord)   
#     additionalInfo = me.StringField()


# class Timesheet(me.Document):
#     dateOfWork = me.DateField(required=True, unique=True)
#     detailsOfWork = me.ListField(me.EmbeddedDocumentField(WorkerClientWorkHours))    
#     created_at = me.StringField()
#     updated_at = me.StringField()
#     meta = {"collection": "timesheets", "db_alias": "angular-fp"}

#     def save(self, *args, **kwargs):
#         if self.created_at:
#             self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         else:
#             self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         super(Timesheet, self).save(*args, **kwargs)
