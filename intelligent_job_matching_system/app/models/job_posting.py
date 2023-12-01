from app import db
from .skill_set import SkillSet

class JobPosting(db.Document):
    job_title = db.StringField(required=True)
    status = db.StringField(choices=('Open', 'In Progress', 'Filled'))
    start_date = db.DateTimeField()
    end_date = db.DateTimeField()
    hiring_manager = db.ReferenceField('JobSeeker')
    skill_sets = db.ListField(db.ReferenceField('SkillSet'))
