from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ..config import Config


engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
session_local = sessionmaker(auto_commit=False, autoFlush=False, bind=engine)
Base = declarative_base()


