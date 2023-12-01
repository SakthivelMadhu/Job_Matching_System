from flask import request, jsonify, Blueprint
from app.models import Application

application_bp = Blueprint('application', __name__)

# Get all applications
@application_bp.route('/applications', methods=['GET'])
def get_applications():
    applications = Application.objects().to_json()
    return jsonify({'data': applications})

# Get a specific application by ID
@application_bp.route('/applications/<id>', methods=['GET'])
def get_application(id):
    application = Application.objects(id=id).to_json()
    return jsonify({'data': application})

# Create a new application
@application_bp.route('/applications', methods=['POST'])
def create_application():
    data = request.get_json()
    new_application = Application(**data).save()
    return jsonify({'message': 'Application created successfully!', 'data': new_application.to_json()})

# Update an existing application by ID
@application_bp.route('/applications/<id>', methods=['PUT'])
def update_application(id):
    data = request.get_json()
    updated_application = Application.objects(id=id).update(**data)
    return jsonify({'message': 'Application updated successfully!'})

# Delete an application by ID
@application_bp.route('/applications/<id>', methods=['DELETE'])
def delete_application(id):
    deleted_application = Application.objects(id=id).delete()
    return jsonify({'message': 'Application deleted successfully!'})
