from flask import request, jsonify, Blueprint
from app.models import JobSeeker

job_seeker_bp = Blueprint('job_seeker', __name__)

# Get all job seekers
@job_seeker_bp.route('/job_seekers', methods=['GET'])
def get_job_seekers():
    job_seekers = JobSeeker.objects().to_json()
    return jsonify({'data': job_seekers})

# Get a specific job seeker by ID
@job_seeker_bp.route('/job_seekers/<id>', methods=['GET'])
def get_job_seeker(id):
    job_seeker = JobSeeker.objects(id=id).to_json()
    return jsonify({'data': job_seeker})

# Create a new job seeker
@job_seeker_bp.route('/job_seekers', methods=['POST'])
def create_job_seeker():
    data = request.get_json()
    new_job_seeker = JobSeeker(**data).save()
    return jsonify({'message': 'Job Seeker created successfully!', 'data': new_job_seeker.to_json()})

# Update an existing job seeker by ID
@job_seeker_bp.route('/job_seekers/<id>', methods=['PUT'])
def update_job_seeker(id):
    data = request.get_json()
    updated_job_seeker = JobSeeker.objects(id=id).update(**data)
    return jsonify({'message': 'Job Seeker updated successfully!'})

# Delete a job seeker by ID
@job_seeker_bp.route('/job_seekers/<id>', methods=['DELETE'])
def delete_job_seeker(id):
    deleted_job_seeker = JobSeeker.objects(id=id).delete()
    return jsonify({'message': 'Job Seeker deleted successfully!'})
