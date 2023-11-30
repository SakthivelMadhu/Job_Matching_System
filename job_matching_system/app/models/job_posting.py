from app import db

class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default="Open")
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    hiring_manager_id = db.Column(db.Integer, db.ForeignKey('hiring_manager.id'))
    hiring_manager = db.relationship('HiringManager', back_populates='job_postings')
    skill_sets = db.relationship('SkillSet', back_populates='job_posting', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<JobPosting {self.job_title}>"
