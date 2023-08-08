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
