from fastapi import FastAPI
from src.utills.db import Base, engine
from src.tasks.models import TaskManager

app = FastAPI(title="This is my task Management Application")

Base.metadata.create_all(bind=engine)
 