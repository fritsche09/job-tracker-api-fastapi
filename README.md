# Job Tracker API 

## Description

A REST API for tracking job applications built with FastAPI, Pydantic and SQLAlchemy. Supports full CRUD operations create, read, update, and delete job applications via JSON endpoints. 

## Tech Stack

- Python
- FastAPI 
- SQLAlchemy
- Pydantic
- PostgreSQL

## How To Run Locally

1. Clone the repository
```bash
   git clone https://github.com/fritsche09/job-tracker-api-fastapi.git
   cd job-tracker-api-fastapi
```

2. Create and activate a virtual environment
```bash
   python3 -m venv .venv
   source .venv/bin/activate
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Create a `.env` file based on `.env.example`

5. Set up a PostgreSQL database and update your `.env` file
   - Create a new database in PostgreSQL 
   - Update your `.env` with your database credentials:
```
   SQLALCHEMY_DATABASE_URI=postgresql://user:password@localhost/your-database-name
```

6. Run the app
```bash
   python main.py
```


## Endpoints

|           | GET                       | POST                             | PUT                  | DELETE             |
|-----------|---------------------------|----------------------------------|----------------------|------------        |
|jobs/      | Returns a list of all jobs|  Creates and saves a new job     |  N/A                 |  N/A               |
|/jobs/{id}| Returns a job by its id   |  N/A                             |  Updates job by id   |  Deletes job by id |

> FastAPI auto-generates interactive API documentation. 
> Run the app and visit `http://127.0.0.1:8000/docs` to explore and test all endpoints in the browser.

## Model 
This code creates a `Job` model with the following attributes:
```python
from app.database import Base
from sqlalchemy import Column, Integer, String, Text, Date
from datetime import date

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    company = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    status = Column(String(50), default="applied")
    applied_date = Column(Date, default=date.today)
    notes = Column(Text, nullable=True)
```

## Schema 
It also uses Pydantic for data serialization:

### JobBase for incoming data serializatoin and JobResponse(JobBase) for outgoing data

```python

from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class JobBase(BaseModel):
    company: str = Field(..., min_length=1, max_length=100)
    role: str = Field(..., min_length=1, max_length=100)
    status: Optional[str] = "applied"
    applied_date: Optional[date] = None
    notes: Optional[str] = None

class JobResponse(JobBase):
    id: int

    class Config:
        from_attributes = True
```

## Example requests for POST & PUT endpoints

### /jobs body (POST):

```json
{
    "applied_date": "2026-03-17",
    "company": "XYZ",
    "notes": "Interview went well",
    "role": "Engineering",
    "status": "Applied"
}
```
### Server response:
```json
{
    "id": 1,
    "company": "XYZ",
    "role": "Engineering",
    "status": "Applied",
    "applied_date": "2026-03-17",
    "notes": "Interview went well"
}
```
status code: `201 CREATED`

### /jobs/{id} body (PUT):
```json
{
    "notes": "Made it to the second round of interviews"
}
```

### Server response:

```json
{
    "applied_date": "2026-03-17",
    "company": "XYZ",
    "id": 3,
    "notes": "Made it to the second round of interviews",
    "role": "Engineering",
    "status": "Applied"
}
```
status code: `200 OK`

## Explore http://127.0.0.1:8000/docs
URL http://127.0.0.1:8000/docs allows you to see the routes and objects utilized for this project. It also allows you to test each route in the browser. Have fun! 
