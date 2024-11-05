from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, Date
from sqlalchemy.orm import declarative_base

import datetime

engine = create_engine("sqlite:///projects.sqlite")
Base = declarative_base()


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    price = Column("price", Float)
    created_date = Column("create_date", DateTime, default=datetime.datetime.now)


Base.metadata.create_all(engine)
