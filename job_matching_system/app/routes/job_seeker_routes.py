from flask import request
from flask_restful import Resource
from app.models import db, JobSeeker

class JobSeekerResource(Resource):
    def get(self, job_seeker_id):
        job_seeker = JobSeeker.query.get_or_404(job_seeker_id)
        # Serialize the job_seeker object to JSON or other desired format
        serialized_job_seeker = {
            "id": job_seeker.id,
            "name": job_seeker.name,
            "status": job_seeker.status,
            "skills": job_seeker.skills,
            "experience": job_seeker.experience,
            "bio": job_seeker.bio,
            "availability": job_seeker.availability.isoformat() if job_seeker.availability else None
            # Add more fields as needed
        }
        return {"data": serialized_job_seeker}

    def put(self, job_seeker_id):
        job_seeker = JobSeeker.query.get_or_404(job_seeker_id)
        data = request.get_json()

        # Update job_seeker attributes based on the data
        job_seeker.name = data.get("name", job_seeker.name)
        job_seeker.status = data.get("status", job_seeker.status)
        job_seeker.skills = data.get("skills", job_seeker.skills)
        job_seeker.experience = data.get("experience", job_seeker.experience)
        job_seeker.bio = data.get("bio", job_seeker.bio)
        job_seeker.availability = data.get("availability", job_seeker.availability)

        db.session.commit()
        return {"message": "Job Seeker updated successfully"}

    def delete(self, job_seeker_id):
        job_seeker = JobSeeker.query.get_or_404(job_seeker_id)
        db.session.delete(job_seeker)
        db.session.commit()
        return {"message": "Job Seeker deleted successfully"}

class JobSeekerListResource(Resource):
    def get(self):
        job_seekers = JobSeeker.query.all()
        # Serialize the list of job_seekers to JSON or other desired format
        serialized_job_seekers = [
            {
                "id": job_seeker.id,
                "name": job_seeker.name,
                "status": job_seeker.status,
                "skills": job_seeker.skills,
                "experience": job_seeker.experience,
                "bio": job_seeker.bio,
                "availability": job_seeker.availability.isoformat() if job_seeker.availability else None
                # Add more fields as needed
            }
            for job_seeker in job_seekers
        ]
        return {"data": serialized_job_seekers}

    def post(self):
        data = request.get_json()

        # Create a new job_seeker based on the data
        job_seeker = JobSeeker(
            name=data.get("name"),
            status=data.get("status"),
            skills=data.get("skills"),
            experience=data.get("experience"),
            bio=data.get("bio"),
            availability=data.get("availability")
        )

        db.session.add(job_seeker)
        db.session.commit()
        return {"message": "Job Seeker created successfully"}
