from app import db

class Application(db.Document):
    status = db.StringField(choices=('Pending', 'Reviewed', 'Accepted', 'Rejected'))
    job_posting = db.ReferenceField('JobPosting')
