from flask import Blueprint

job_seeker_bp = Blueprint('job_seeker', __name__)
job_posting_bp = Blueprint('job_posting', __name__)
application_bp = Blueprint('application', __name__)
skill_set_bp = Blueprint('skill_set', __name__)

from . import job_seeker_routes, job_posting_routes, application_routes, skill_set_routes
