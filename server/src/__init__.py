from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import Config


# Initialize database
# db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register a Blueprint in flask, blueprint is basically a way to split up api to different folders
    # docs: https://flask.palletsprojects.com/en/3.0.x/blueprints/
    from src.job_board import bp as job_board_blueprint
    app.register_blueprint(job_board_blueprint)

    # db.init_app(app)

    with app.app_context():
        pass
        # This will create the database cols when we initialize the app, add db later
        # db.create_all()
        
    return app
