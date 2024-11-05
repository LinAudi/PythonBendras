from sqlalchemy import Column, Integer,String, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///many-to-one.sqlite")
Base = declarative_base()

class Parent(Base):
    __tablename__ = "parent"
    id = Column("Id",Integer,primary_key=True)
    name = Column("Name", String)
    surname = Column("name",String)
    School = Column("name", String)


class Child(Base):
    __tablename__ = "parent"
    id = Column("Id", Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("name", String)
    School = Column("name", String)
