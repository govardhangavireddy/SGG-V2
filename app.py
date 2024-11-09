from flask import Flask, render_template, jsonify
from database import load_jobs, load_jobs_from_db

app = Flask(__name__)

company = "SGG"

@app.route('/')
def home():
    return render_template('home.html',jobs = load_jobs(),company_name = company)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(load_jobs())

@app.route('/job/<id>')
def specific_job(id):
    job = load_jobs_from_db(id)
    if not job:
        return "Job not found", 404
    return render_template('jobpage.html',job = job,company_name = company)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)


    



