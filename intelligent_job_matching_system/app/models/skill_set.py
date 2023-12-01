from app import db

class SkillSet(db.Document):
    name = db.StringField(required=True, unique=True)
    job_postings = db.ListField(db.ReferenceField('JobPosting'))
