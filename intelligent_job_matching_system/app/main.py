from flask import Flask
from app.routes import job_seeker_bp, job_posting_bp, application_bp, skill_set_bp
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine(app)

# Register blueprints for each entity
app.register_blueprint(job_seeker_bp, url_prefix='/api')
app.register_blueprint(job_posting_bp, url_prefix='/api')
app.register_blueprint(application_bp, url_prefix='/api')
app.register_blueprint(skill_set_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
