from flask import Flask, render_template, jsonify, request
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


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id= :i"), {"i": id})
        job = result.fetchone()
        if job is None:
            return None
        else:
            return dict(job._mapping)


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) "
            "VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
        )
        conn.execute(
            query,
            {
                "job_id": job_id,
                "full_name": data["full_name"],
                "email": data["email"],
                "linkedin_url": data["linkedin_url"],
                "education": data["education"],
                "work_experience": data["work_experience"],
                "resume_url": data["resume_url"],
            },
        )
        conn.commit()


@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)


@app.route("/job/<id>")
def get_job(id):
    job = load_job_from_db(id)
    if job is None:
        return "Not Found", 404
    return render_template("jobpage.html", job=job)


@app.route("/job/<id>/apply", methods=["post"])
def apply_job(id):
    data = request.form
    job = load_job_from_db(id)
    add_application_to_db(id, data)
    return render_template("application_submitted.html", application=data, job=job)


@app.route("/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)
