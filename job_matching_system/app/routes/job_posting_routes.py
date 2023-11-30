from flask import request
from flask_restful import Resource
from app.models import db, JobPosting

class JobPostingResource(Resource):
    def get(self, job_posting_id):
        job_posting = JobPosting.query.get_or_404(job_posting_id)
        # Serialize the job_posting object to JSON or other desired format
        serialized_job_posting = {
            "id": job_posting.id,
            "job_title": job_posting.job_title,
            "status": job_posting.status,
            "start_date": job_posting.start_date.isoformat() if job_posting.start_date else None,
            "end_date": job_posting.end_date.isoformat() if job_posting.end_date else None,
            # Add more fields as needed
        }
        return {"data": serialized_job_posting}

    def put(self, job_posting_id):
        job_posting = JobPosting.query.get_or_404(job_posting_id)
        data = request.get_json()
        # Update job_posting attributes based on the data
        job_posting.job_title = data.get("job_title", job_posting.job_title)
        job_posting.status = data.get("status", job_posting.status)
        job_posting.start_date = data.get("start_date", job_posting.start_date)
        job_posting.end_date = data.get("end_date", job_posting.end_date)
        # Add more fields as needed

        db.session.commit()
        return {"message": "Job Posting updated successfully"}

    def delete(self, job_posting_id):
        job_posting = JobPosting.query.get_or_404(job_posting_id)
        db.session.delete(job_posting)
        db.session.commit()
        return {"message": "Job Posting deleted successfully"}

class JobPostingListResource(Resource):
    def get(self):
        job_postings = JobPosting.query.all()
        # Serialize the list of job_postings to JSON or other desired format
        serialized_job_postings = [
            {
                "id": job_posting.id,
                "job_title": job_posting.job_title,
                "status": job_posting.status,
                "start_date": job_posting.start_date.isoformat() if job_posting.start_date else None,
                "end_date": job_posting.end_date.isoformat() if job_posting.end_date else None,
                # Add more fields as needed
            }
            for job_posting in job_postings
        ]
        return {"data": serialized_job_postings}

    def post(self):
        data = request.get_json()
        # Create a new job_posting based on the data
        job_posting = JobPosting(
            job_title=data.get("job_title"),
            status=data.get("status"),
            start_date=data.get("start_date"),
            end_date=data.get("end_date")
            # Add more fields as needed
        )

        db.session.add(job_posting)
        db.session.commit()
        return {"message": "Job Posting created successfully"}
