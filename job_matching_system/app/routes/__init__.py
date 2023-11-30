from flask import Blueprint
from flask_restful import Api

# Create a blueprint for the routes
routes_bp = Blueprint('routes', __name__)

# Create an API for the blueprint
api = Api(routes_bp)

# Import your route handler classes and add them to the API
from .job_seeker_routes import JobSeekerResource, JobSeekerListResource
from .job_posting_routes import JobPostingResource, JobPostingListResource
from .application_routes import ApplicationResource, ApplicationListResource
from .skill_set_routes import SkillSetResource, SkillSetListResource

api.add_resource(JobSeekerListResource, '/jobseekers')
api.add_resource(JobSeekerResource, '/jobseekers/<int:job_seeker_id>')

api.add_resource(JobPostingListResource, '/jobpostings')
api.add_resource(JobPostingResource, '/jobpostings/<int:job_posting_id>')

api.add_resource(ApplicationListResource, '/applications')
api.add_resource(ApplicationResource, '/applications/<int:application_id>')

api.add_resource(SkillSetListResource, '/skillsets')
api.add_resource(SkillSetResource, '/skillsets/<int:skill_set_id>')
