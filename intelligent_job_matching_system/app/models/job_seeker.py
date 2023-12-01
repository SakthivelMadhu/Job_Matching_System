from app import db

class JobSeeker(db.Document):
    name = db.StringField(required=True)
    status = db.BooleanField(default=True)
    skills = db.StringField()
    experience = db.StringField(choices=('Entry Level', 'Mid Level', 'Senior'))
    bio = db.StringField()
    availability = db.DateTimeField()
