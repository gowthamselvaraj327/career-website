# Flask Career Portal

A **Flask-based Career Portal** web application where users can browse, and apply for jobs.  
This project demonstrates how to build scalable web applications with **Flask**, integrate with **PostgreSQL** using **SQLAlchemy**, and provide auto-generated API documentation with **Swagger UI** and **ReDoc**.

---

## Why Flask

- **Lightweight & Flexible:** Minimal and highly customizable for all types of projects.  
- **Easy to Learn:** Simple structure and easy to maintain.  
- **Extensible:** Works well with ORMs, authentication, and front-end integration.  
- **Production Ready:** Deployed using **Gunicorn** on **Render** for reliability and scalability.  
- **Auto Documentation:** Integrated **Swagger UI** and **ReDoc** for clear and interactive API docs.

---

## Technologies Used

| Technology | Purpose |
|-------------|----------|
| **Flask** | Main web framework |
| **Python** | Core programming language |
| **Gunicorn** | WSGI HTTP server for production deployment |
| **SQLAlchemy** | ORM for database interactions |
| **Psycopg2** | PostgreSQL adapter for Python |
| **PostgreSQL** | Database for storing job and user data |
| **Swagger UI / ReDoc** | Auto-generated API documentation |
| **Render** | Cloud hosting platform for deployment |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gowthamselvaraj327/career-website.git
cd career-website
```
### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### Database Setup

Make sure PostgreSQL is installed and running.

### 4. Create a database
```bash
CREATE DATABASE career_portal_db;
```

### 5. Create Tables
```bash
CREATE TABLE jobs(
    id SERIAL not null,
    title VARCHAR(250) not null,
    location VARCHAR(250) not null,
    salary INT,
    currency VARCHAR(10),
    responsibilities VARCHAR(2000),
    requirements VARCHAR(2000),
    primary key (id)
);

CREATE TABLE applications (
    id SERIAL PRIMARY KEY,
    job_id INT NOT NULL,
    full_name VARCHAR(250) NOT NULL,
    email VARCHAR(250) NOT NULL,
    linkedin_url VARCHAR(500),
    education VARCHAR(2000),
    work_experience VARCHAR(2000),
    resume_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
### 6. Update your database URL in .env file:
```bash
DATABASE_URL=postgresql+psycopg2://username:password@host/database_name
```
### 7. Running the App
Development Mode
```bash
flask --app app run --debug
```

Production Mode (using Gunicorn)
```bash
gunicorn app:app
```

## API Documentation
Once the app is running, open these URLs:
<br>
- **Application UI:** http://127.0.0.1:5000
- **Swagger UI:** http://127.0.0.1:5000/docs
- **ReDoc:** http://127.0.0.1:5000/redoc

## Deployment
This application is deployed on Render using Gunicorn.
<br>
- **Live Demo:** https://career-website-anvi.onrender.com
