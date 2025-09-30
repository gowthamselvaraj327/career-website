from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Scientist",
        "location": "Delhi, India",
        "salary": "Rs 15,00,000",
    },
    {
        "id": 2,
        "title": "Data Analyst",
        "location": "Bengaluru, India",
        "salary": "Rs 10,00,000",
    },
    {
        "id": 3,
        "title": "Frontend Engineer",
        "location": "Remote",
    },
    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "San Francisco, USA",
        "salary": "$100,000",
    },
]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)
