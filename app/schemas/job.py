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