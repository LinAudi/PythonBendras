from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from paskaita import Project

engine = create_engine("sqlite:///projects.sqlite")
Session = sessionmaker(bind=engine)
sesion = Session()

project1 = Project("Projektas 1", 100.11)

sesion.add(project1)
sesion.commit()
