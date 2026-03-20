from app.database import Base
from datetime import date
from sqlalchemy import Column, Integer, String, Text, Date

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    company = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    status = Column(String(50), default="applied")
    applied_date = Column(Date, default=date.today)
    notes = Column(Text, nullable=True)

    def __repr__(self):
        return f"<Job {self.company} - {self.role}>"