
# Job Matching System

## Description

The Job Matching System is a web application built with Flask, a Python web framework, to facilitate the matching of job seekers with job postings. This project includes features such as managing job seekers, job postings, applications, and skill sets.

## Project Structure

The project structure is organized as follows:

job_matching_system/
|-- app/
|   |-- __init__.py
|   |-- models/
|   |   |-- __init__.py
|   |   |-- job_seeker.py
|   |   |-- job_posting.py
|   |   |-- application.py
|   |   |-- skill_set.py
|   |-- routes/
|   |   |-- __init__.py
|   |   |-- job_seeker_routes.py
|   |   |-- job_posting_routes.py
|   |   |-- application_routes.py
|   |   |-- skill_set_routes.py
|   |-- config.py
|   |-- extensions.py
|   |-- app.py
|-- migrations/
|-- tests/
|-- requirements.txt
|-- README.md
|-- .gitignore



## Installation

1. Clone the repository:

```bash
git clone https://github.com/SakthivelMadhu/Job_Matching_System.git
cd job_matching_system
```
2. Create and activate a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\activate  # For Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
flask run or python app.py
```

## Usage
Visit http://127.0.0.1:5000/ in your web browser to access the application.

## API Endpoints:
# Job Seekers:

GET /job_seekers: Get all job seekers.
GET /job_seekers/<job_seeker_id>: Get a specific job seeker.
POST /job_seekers: Create a new job seeker.
PUT /job_seekers/<job_seeker_id>: Update a job seeker.
DELETE /job_seekers/<job_seeker_id>: Delete a job seeker.

# Skill Sets:

GET /skill_sets: Get all skill sets.
GET /skill_sets/<skill_set_id>: Get a specific skill set.
POST /skill_sets: Create a new skill set.
PUT /skill_sets/<skill_set_id>: Update a skill set.
DELETE /skill_sets/<skill_set_id>: Delete a skill set.

# Job Postings:

GET /job_postings: Get all job postings.
GET /job_postings/<job_posting_id>: Get a specific job posting.
POST /job_postings: Create a new job posting.
PUT /job_postings/<job_posting_id>: Update a job posting.
DELETE /job_postings/<job_posting_id>: Delete a job posting.

# Applications:

GET /applications: Get all applications.
GET /applications/<application_id>: Get a specific application.
POST /applications: Create a new application.
PUT /applications/<application_id>: Update an application.
DELETE /applications/<application_id>: Delete an application.