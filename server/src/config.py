import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# Db config
DB_URI = os.environ.get('DB_URI')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI= DB_URI