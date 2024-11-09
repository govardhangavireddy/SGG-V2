# import sqlalchemy
# print(sqlalchemy.__version__)
import os
from sqlalchemy import create_engine, text

from flask import jsonify

#connect to localhost database
db_connection_str = os.environ.get('DB_CONNECTION')

engine = create_engine(db_connection_str)

def load_jobs():
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs"))
        jobs = []
        for row in result:
            # print(row._mapping)
            jobs.append(row._mapping)
        # print(type(jobs))
        return jobs
    # print(jobs)

def load_jobs_from_db(id):
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs where id = :val"),{"val":id})
        rows = result.all()
        if len(rows) == 0:
            return None
        return rows[0]._mapping


