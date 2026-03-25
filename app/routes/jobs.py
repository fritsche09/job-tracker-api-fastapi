from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.job import Job
from app.schemas.job import JobBase, JobResponse

router = APIRouter()

@router.get("/jobs", response_model=list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    all_jobs = db.query(Job).all()
    return all_jobs

@router.get("/jobs/{id}", response_model=JobResponse)
def get_job(id: int, db: Session = Depends(get_db)):
        job = db.query(Job).filter(Job.id == id).first()
        if job:
            return job
        raise HTTPException(status_code=404, detail="Job not found")
    
@router.post("/jobs", response_model=JobResponse, status_code=201)
def create_job(job: JobBase, db: Session = Depends(get_db)):
    new_job = Job(**job.model_dump())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job
    

@router.put("/jobs/{id}", response_model=JobResponse)
def update_jobs(id: int, job: JobBase, db: Session = Depends(get_db)):
    current_job = db.query(Job).filter(Job.id == id).first()

    if not current_job:
        raise HTTPException(status_code=404, detail="Job not found") 

    for key, value in job.model_dump().items():
            setattr(current_job, key, value)
    db.commit()
    db.refresh(current_job)
    return current_job

    
@router.delete("/jobs/{id}", status_code=204)
def delete_job(id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(job)
    db.commit()
    return ""

    