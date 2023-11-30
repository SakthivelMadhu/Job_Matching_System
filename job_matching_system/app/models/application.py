from app import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), default="Pending")
    job_posting_id = db.Column(db.Integer, db.ForeignKey('job_posting.id'))
    job_posting = db.relationship('JobPosting', back_populates='applications')
    job_seeker_id = db.Column(db.Integer, db.ForeignKey('job_seeker.id'))
    job_seeker = db.relationship('JobSeeker', back_populates='applications')

    def __repr__(self):
        return f"<Application {self.id}>"


