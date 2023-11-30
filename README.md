
# Job Matching System

## Description

The Job Matching System is a web application built with Flask, a Python web framework, to facilitate the matching of job seekers with job postings. This project includes features such as managing job seekers, job postings, applications, and skill sets.

## Project Structure

The project structure is organized as follows:
```bash
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
```


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

GET /job_seekers: Get all job seekers. <br>
GET /job_seekers/<job_seeker_id>: Get a specific job seeker. <br>
POST /job_seekers: Create a new job seeker. <br>
PUT /job_seekers/<job_seeker_id>: Update a job seeker. <br>
DELETE /job_seekers/<job_seeker_id>: Delete a job seeker. <br>

# Skill Sets:

GET /skill_sets: Get all skill sets. <br>
GET /skill_sets/<skill_set_id>: Get a specific skill set. <br>
POST /skill_sets: Create a new skill set. <br>
PUT /skill_sets/<skill_set_id>: Update a skill set. <br>
DELETE /skill_sets/<skill_set_id>: Delete a skill set. <br>

# Job Postings:

GET /job_postings: Get all job postings. <br>
GET /job_postings/<job_posting_id>: Get a specific job posting. <br>
POST /job_postings: Create a new job posting. <br>
PUT /job_postings/<job_posting_id>: Update a job posting. <br>
DELETE /job_postings/<job_posting_id>: Delete a job posting. <br>

# Applications:

GET /applications: Get all applications. <br>
GET /applications/<application_id>: Get a specific application. <br>
POST /applications: Create a new application. <br>
PUT /applications/<application_id>: Update an application. <br>
DELETE /applications/<application_id>: Delete an application. <br>