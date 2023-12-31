from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import Config
from flask_cors import CORS

# Initialize database
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    
    # Call all configurations from config.py
    app.config.from_object(config_class)
    CORS(app, supports_credentials=True)

    # Register a Blueprint in flask, blueprint is basically a way to split up api to different folders
    # docs: https://flask.palletsprojects.com/en/3.0.x/blueprints/
    from src.job_board import bp as job_board_blueprint
    app.register_blueprint(job_board_blueprint)

    db.init_app(app)

    with app.app_context():
        # This will create the database cols when we initialize the app, add db later
        db.create_all()
        
    return app
