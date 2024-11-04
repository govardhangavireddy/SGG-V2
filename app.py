from flask import Flask, render_template, jsonify
app = Flask(__name__)

company = "SGG"

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bangalore, India',
        'Salary': 'Rs. 1000000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'Salary': 'Rs. 1200000',
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'location':'Remote',
        # 'Salary': '800000',
    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'location':'Remote',
        'Salary': 'Rs. 900000',
    }
]

@app.route('/')
def home():
    return render_template('home.html',jobs = JOBS,company_name = company)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)


    



