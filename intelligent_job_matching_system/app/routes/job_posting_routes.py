from flask import request, jsonify, Blueprint
from app.models import JobPosting

job_posting_bp = Blueprint('job_posting', __name__)

# Get all job postings
@job_posting_bp.route('/job_postings', methods=['GET'])
def get_job_postings():
    job_postings = JobPosting.objects().to_json()
    return jsonify({'data': job_postings})

# Get a specific job posting by ID
@job_posting_bp.route('/job_postings/<id>', methods=['GET'])
def get_job_posting(id):
    job_posting = JobPosting.objects(id=id).to_json()
    return jsonify({'data': job_posting})

# Create a new job posting
@job_posting_bp.route('/job_postings', methods=['POST'])
def create_job_posting():
    data = request.get_json()
    new_job_posting = JobPosting(**data).save()
    return jsonify({'message': 'Job Posting created successfully!', 'data': new_job_posting.to_json()})

# Update an existing job posting by ID
@job_posting_bp.route('/job_postings/<id>', methods=['PUT'])
def update_job_posting(id):
    data = request.get_json()
    updated_job_posting = JobPosting.objects(id=id).update(**data)
    return jsonify({'message': 'Job Posting updated successfully!'})

# Delete a job posting by ID
@job_posting_bp.route('/job_postings/<id>', methods=['DELETE'])
def delete_job_posting(id):
    deleted_job_posting = JobPosting.objects(id=id).delete()
    return jsonify({'message': 'Job Posting deleted successfully!'})
