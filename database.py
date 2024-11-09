# import sqlalchemy
# print(sqlalchemy.__version__)
import os
from sqlalchemy import create_engine, text


#connect to localhost database
db_connection_str = os.environ.get('DB_CONNECTION')

engine = create_engine(db_connection_str)

def load_jobs():
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs"))
        jobs = []
        for row in result:
            # print(row._mapping)

            jobs.append(dict(row._mapping))
        # print(type(jobs))
        return jobs
    # print(jobs)

def load_jobs_from_db(id):
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs where id = :val"),{"val":id})
        rows = result.all()
        if len(rows) == 0:
            return None
        
        # print(rows[0]._mapping)
        return dict(rows[0]._mapping)
    
def add_application_to_db(job_id,application):
    with engine.connect() as connection:
        connection.execute(text("insert into applications(job_id,first_name,last_name,email,phone,education,work_experience,linkedin_url,resume_link) values (:job_id,:first_name,:last_name,:email,:phone_number,:education,:work_experience,:linkedin_url,:resume)"),{"job_id":job_id,"first_name":application['first_name'],"last_name":application['last_name'],"email":application['email'],"phone_number":application['phone'],'education':application['education'],'work_experience':application['work_experience'],'linkedin_url':application['linkedin_url'],'resume':application['resume_url']})






