import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# Db config
user = os.environ.get('DB_USER')
db_name = os.environ.get("DB_NAME")
password = os.environ.get('DB_PWD')
DB_URI = f'postgresql://{user}:{password}@localhost/{db_name}'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI= DB_URI