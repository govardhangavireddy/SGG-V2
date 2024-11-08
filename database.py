# import sqlalchemy
# print(sqlalchemy.__version__)

from sqlalchemy import create_engine, text
#connect to localhost database
engine = create_engine('mysql+pymysql://root:govardhan96@127.0.0.1:3306/applications')

def load_jobs():
    with engine.connect() as connection:
        result = connection.execute(text("select * from jobs"))
        jobs = []
        for row in result:
            # print(row._mapping)
            jobs.append(row._mapping)
        # print(type(result.first()))
        # return result_dict
        return jobs


