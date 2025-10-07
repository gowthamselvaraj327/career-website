from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * from jobs"))
        jobs = result.mappings().all()
        return [dict(job) for job in jobs]


@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)


@app.route("/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)
