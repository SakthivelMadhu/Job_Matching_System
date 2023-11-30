from flask import request
from flask_restful import Resource
from app.models import db, SkillSet

class SkillSetResource(Resource):
    def get(self, skill_set_id):
        skill_set = SkillSet.query.get_or_404(skill_set_id)
        # Serialize the skill_set object to JSON or other desired format
        serialized_skill_set = {
            "id": skill_set.id,
            "name": skill_set.name,
            # Add more fields as needed
        }
        return {"data": serialized_skill_set}

    def put(self, skill_set_id):
        skill_set = SkillSet.query.get_or_404(skill_set_id)
        data = request.get_json()
        # Update skill_set attributes based on the data
        skill_set.name = data.get("name", skill_set.name)
        # Add more fields as needed

        db.session.commit()
        return {"message": "Skill Set updated successfully"}

    def delete(self, skill_set_id):
        skill_set = SkillSet.query.get_or_404(skill_set_id)
        db.session.delete(skill_set)
        db.session.commit()
        return {"message": "Skill Set deleted successfully"}

class SkillSetListResource(Resource):
    def get(self):
        skill_sets = SkillSet.query.all()
        # Serialize the list of skill_sets to JSON or other desired format
        serialized_skill_sets = [
            {
                "id": skill_set.id,
                "name": skill_set.name,
                # Add more fields as needed
            }
            for skill_set in skill_sets
        ]
        return {"data": serialized_skill_sets}

    def post(self):
        data = request.get_json()
        # Create a new skill_set based on the data
        skill_set = SkillSet(
            name=data.get("name"),
            # Add more fields as needed
        )

        db.session.add(skill_set)
        db.session.commit()
        return {"message": "Skill Set created successfully"}
