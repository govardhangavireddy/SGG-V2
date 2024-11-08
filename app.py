from flask import Flask, render_template, jsonify
from database import load_jobs

app = Flask(__name__)

company = "SGG"

@app.route('/')
def home():
    return render_template('home.html',jobs = load_jobs(),company_name = company)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(load_jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)


    



