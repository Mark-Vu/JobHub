from . import db

class Jobs(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    position_name = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)
    job_id = db.Column(db.String, unique=True, nullable=False)
    link = db.Column(db.String, nullable=False)
    
# Function to insert data into the jobs table
def insert_into_jobs(data):
    for entry in data:
        # Check if a job with the same job_id already exists
        existing_job = Jobs.query.filter_by(job_id=entry['id']).first()
        if existing_job is None:
            # If no matching job_id is found, add the new record
            job = Jobs(position_name=entry['position_name'],
                       company=entry['company'],
                       job_id=entry['id'],
                       link=entry['link'])
            db.session.add(job)
    db.session.commit()