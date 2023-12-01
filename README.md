# Intelligent Job Matching System

This project is a backend system for an intelligent job matching application. It is built using Flask and MongoDB , to facilitate the matching of job seekers with job postings. This project includes features such as managing job seekers, job postings, applications, and skill sets.


## Project Structure

The project structure is organized as follows:
```bash
intelligent_job_matching_system/
│
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── job_seeker.py
│   │   ├── job_posting.py
│   │   ├── application.py
│   │   └── skill_set.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── job_seeker_routes.py
│   │   ├── job_posting_routes.py
│   │   ├── application_routes.py
│   │   └── skill_set_routes.py
│   └── main.py
│
├── config/
│   ├── __init__.py
│   ├── config.py
│   └── database.py
│
├── tests/
│   ├── __init__.py
│   ├── test_job_seeker.py
│   ├── test_job_posting.py
│   ├── test_application.py
│   └── test_skill_set.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── run.py

```

## Project Structure

- `app/`: Contains the main application code.
  - `__init__.py`: Initializes the Flask application.
  - `models/`: Defines data models.
  - `routes/`: Defines API routes for CRUD operations.
  - `main.py`: Entry point for running the Flask application.
- `config/`: Configuration files.
  - `__init__.py`: Empty file.
  - `config.py`: General configuration settings.
  - `database.py`: MongoDB configuration settings.
- `tests/`: Unit tests for different components of the application.
- `requirements.txt`: Lists project dependencies.
- `README.md`: Project documentation.
- `.gitignore`: Specifies files and directories to be ignored by version control.
- `run.py`: Script to run the Flask application.

## ERDiagram 

```bash
+-----------------+        +---------------------+       +-----------------+
|   JobSeeker     |        |   JobPosting        |       |   Application   |
+-----------------+        +---------------------+       +-----------------+
| id: ObjectId    |        | id: ObjectId        |       | id: ObjectId    |
| name: String    |        | job_title: String    |       | status: String  |
| status: Boolean |        | status: String       |       | job_posting: Ref|
| skills: String  |        | start_date: DateTime |       +-----------------+
| experience: Enum|        | end_date: DateTime   |
| bio: String     |        | hiring_manager: Ref  |
| availability:   |        | skill_sets: [Ref]    |
|   DateTime      |        +---------------------+
+-----------------+

+-----------------+
|   SkillSet      |
+-----------------+
| id: ObjectId    |
| name: String    |
| job_postings:   |
|   [Ref]         |
+-----------------+

```


## Setup and Run

1. clone github: `https://github.com/SakthivelMadhu/Job_Matching_System.git`
2. Create and activate a virtual environment: `python -m venv venv`, `.\venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python run.py`

## API Endpoints

- Job Seekers: `/api/job_seekers`
- Job Postings: `/api/job_postings`
- Applications: `/api/applications`
- Skill Sets: `/api/skill_sets`

## Testing

To run tests, use the following command:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

## MongoDB Connections 
MongoDB is used as the database backend in this system. The connection string can be found in the `config/database.py` file.



## API Endpoints

### Job Seekers

- **GET /job_seekers:** Get all job seekers.
- **GET /job_seekers/<job_seeker_id>:** Get a specific job seeker.
- **POST /job_seekers:** Create a new job seeker.
- **PUT /job_seekers/<job_seeker_id>:** Update a job seeker.
- **DELETE /job_seekers/<job_seeker_id>:** Delete a job seeker.

### Skill Sets

- **GET /skill_sets:** Get all skill sets.
- **GET /skill_sets/<skill_set_id>:** Get a specific skill set.
- **POST /skill_sets:** Create a new skill set.
- **PUT /skill_sets/<skill_set_id>:** Update a skill set.
- **DELETE /skill_sets/<skill_set_id>:** Delete a skill set.

### Job Postings

- **GET /job_postings:** Get all job postings.
- **GET /job_postings/<job_posting_id>:** Get a specific job posting.
- **POST /job_postings:** Create a new job posting.
- **PUT /job_postings/<job_posting_id>:** Update a job posting.
- **DELETE /job_postings/<job_posting_id>:** Delete a job posting.

### Applications

- **GET /applications:** Get all applications.
- **GET /applications/<application_id>:** Get a specific application.
- **POST /applications:** Create a new application.
- **PUT /applications/<application_id>:** Update an application.
- **DELETE /applications/<application_id>:** Delete an application.