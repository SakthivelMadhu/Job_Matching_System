from flask import Flask
from app.extensions import db

def create_app():
    app = Flask(__name__)

    # Load configuration from the config.py file
    app.config.from_object('app.config')

    # Initialize the database extension
    db.init_app(app)

    # Import and register the routes blueprint
    from app.routes import routes_bp
    app.register_blueprint(routes_bp, url_prefix='/api')

    return app
