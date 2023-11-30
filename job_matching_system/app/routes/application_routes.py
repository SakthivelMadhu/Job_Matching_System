from flask import request
from flask_restful import Resource
from app.models import db, Application

class ApplicationResource(Resource):
    def get(self, application_id):
        application = Application.query.get_or_404(application_id)
        # Serialize the application object to JSON or other desired format
        serialized_application = {
            "id": application.id,
            "job_posting_id": application.job_posting_id,
            "status": application.status,
            # Add more fields as needed
        }
        return {"data": serialized_application}

    def put(self, application_id):
        application = Application.query.get_or_404(application_id)
        data = request.get_json()
        # Update application attributes based on the data
        application.job_posting_id = data.get("job_posting_id", application.job_posting_id)
        application.status = data.get("status", application.status)
        # Add more fields as needed

        db.session.commit()
        return {"message": "Application updated successfully"}

    def delete(self, application_id):
        application = Application.query.get_or_404(application_id)
        db.session.delete(application)
        db.session.commit()
        return {"message": "Application deleted successfully"}

class ApplicationListResource(Resource):
    def get(self):
        applications = Application.query.all()
        # Serialize the list of applications to JSON or other desired format
        serialized_applications = [
            {
                "id": application.id,
                "job_posting_id": application.job_posting_id,
                "status": application.status,
                # Add more fields as needed
            }
            for application in applications
        ]
        return {"data": serialized_applications}

    def post(self):
        data = request.get_json()
        # Create a new application based on the data
        application = Application(
            job_posting_id=data.get("job_posting_id"),
            status=data.get("status")
            # Add more fields as needed
        )

        db.session.add(application)
        db.session.commit()
        return {"message": "Application created successfully"}
