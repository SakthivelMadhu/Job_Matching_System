
from app import db

class JobSeeker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=True)
    skills = db.Column(db.String(255))
    experience = db.Column(db.String(20))
    bio = db.Column(db.Text)
    availability = db.Column(db.Date)

    def __repr__(self):
        return f"<JobSeeker {self.name}>"
