from flask import request, jsonify, Blueprint
from app.models import SkillSet

skill_set_bp = Blueprint('skill_set', __name__)

# Get all skill sets
@skill_set_bp.route('/skill_sets', methods=['GET'])
def get_skill_sets():
    skill_sets = SkillSet.objects().to_json()
    return jsonify({'data': skill_sets})

# Get a specific skill set by ID
@skill_set_bp.route('/skill_sets/<id>', methods=['GET'])
def get_skill_set(id):
    skill_set = SkillSet.objects(id=id).to_json()
    return jsonify({'data': skill_set})

# Create a new skill set
@skill_set_bp.route('/skill_sets', methods=['POST'])
def create_skill_set():
    data = request.get_json()
    new_skill_set = SkillSet(**data).save()
    return jsonify({'message': 'Skill Set created successfully!', 'data': new_skill_set.to_json()})

# Update an existing skill set by ID
@skill_set_bp.route('/skill_sets/<id>', methods=['PUT'])
def update_skill_set(id):
    data = request.get_json()
    updated_skill_set = SkillSet.objects(id=id).update(**data)
    return jsonify({'message': 'Skill Set updated successfully!'})

# Delete a skill set by ID
@skill_set_bp.route('/skill_sets/<id>', methods=['DELETE'])
def delete_skill_set(id):
    deleted_skill_set = SkillSet.objects(id=id).delete()
    return jsonify({'message': 'Skill Set deleted successfully!'})
