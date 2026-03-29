from fastapi import FastAPI
from src.utills.db import Base, engine
from src.tasks.models import TaskManager 
from src.tasks.routers import task_routes
from src.users.routers import user_routes

app = FastAPI(title="This is my task Management Application")

Base.metadata.create_all(bind=engine)
app.include_router(task_routes)
app.include_router(user_routes)
 