from . import bp
import csv
from src.models import Jobs, insert_into_jobs


@bp.route("/")
def index():
    data = read_from_csv()
    # insert_into_jobs(data)
    # Query all jobs from the Jobs table
    jobs = Jobs.query.all()
    
    # Convert the jobs data to a list of dictionaries
    job_list = []
    
    for job in jobs:
        job_data = {
            "position_name": job.position_name,
            "company": job.company,
            "id": job.job_id,
            "link": job.link
        }
        job_list.append(job_data)
    
    return job_list

def read_from_csv():
    return_data = []  # Initialize as a list
    # Open the CSV file for reading
    with open('job_board/indeedscraper.csv', 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        # Skip the header row
        next(csv_reader)
        
        # Extract and append the desired fields as dictionaries to the list
        for row in csv_reader:
            position_name = row[0]
            company = row[4]  # Extract the company name
            job_id = row[8]  # Extract the ID
            link = row[7]
            data = {
                "position_name": position_name,
                "company": company,
                "id": job_id,
                "link": link
            }
            return_data.append(data)
    return return_data


