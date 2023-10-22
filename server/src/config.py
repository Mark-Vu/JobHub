import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# Db config
user = os.environ.get('DB_USER')
db_name = os.environ.get("DB_NAME")
password = os.environ.get('DB_PWD')
db_id = os.environ.get('DB_ID')
DB_URI = f'postgresql://jobhub_jlcj_user:WWvWHBKyiqRlgMvpCodBaXqHiEiyFD7d@dpg-ckq54jhrfc9c73evaq7g-a.oregon-postgres.render.com/jobhub_jlcj'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI= DB_URI