# import sqlalchemy
# print(sqlalchemy.__version__)
import os
from sqlalchemy import create_engine, text

#connect to localhost database
db_connection_str = os.environ.get('DB_CONNECT')

engine = create_engine(db_connection_str)

def load_jobs():
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs"))
        jobs = []
        for row in result:
            # print(row._mapping)
            jobs.append(row._mapping)
        return jobs


