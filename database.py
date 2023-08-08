from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    column_names = result.keys()
    jobs = []
    for row in result:
      row_dict = {}
      for column_name, value in zip(column_names, row):
        row_dict[column_name] = value
      jobs.append(row_dict)
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :id"),
                          {"id": id})
    row = result.fetchone()  # Fetch a single row
    if row is None:
      return None
    else:
      column_names = result.keys()
      job_dict = {}
      for column_name, value in zip(column_names, row):
        if column_name not in (
            "created_at",
            "updated_at"):  # Exclude "created_at" and "updated_at" keys
          job_dict[column_name] = value
      return job_dict


def add_application_to_db(id, data):
  with engine.connect() as conn:
    stmt = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) "
      "VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    ).bindparams(job_id=id,
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])

    conn.execute(stmt)
