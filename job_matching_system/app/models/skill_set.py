from app import db

class SkillSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    job_posting_id = db.Column(db.Integer, db.ForeignKey('job_posting.id'))
    job_posting = db.relationship('JobPosting', back_populates='skill_sets')

    def __repr__(self):
        return f"<SkillSet {self.name}>"
