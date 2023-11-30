# In other files, e.g., routes or app.py
from app.models import JobSeeker, JobPosting, Application, SkillSet
from flask import Flask
from app.extensions import db
from app.routes import routes_bp  # Import the routes_bp blueprint

app = Flask(__name__)

# Configure your app, including the database connection
app.config.from_object('app.config')
db.init_app(app)

# Register the routes blueprint
app.register_blueprint(routes_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True , port=6767)
