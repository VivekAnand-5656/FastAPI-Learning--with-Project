from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskComplete, TaskResponseSchema
from src.utills.db import get_db

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema, db = Depends(get_db)): 
    return controller.create_task(body,db)

@task_routes.get("/getalltasks", response_model=list[TaskResponseSchema], status_code=status.HTTP_200_OK)
def get_all_tasks(db = Depends(get_db)):
    return controller.get_all_tasks(db)

@task_routes.get("/gettaskById/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def get_task_by_id(task_id:int,db = Depends(get_db)):
    return controller.get_one_task(task_id, db)

# ----- Update Task By ID -----
@task_routes.put("/updatetask/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def update_task(body:TaskSchema,task_id:int,db=Depends(get_db)):
    return controller.update_task_by_id(body,task_id,db)

# ----- Task Complete -----
@task_routes.patch("/completetask/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def task_complete(body:TaskComplete,task_id:int,db=Depends(get_db)):
    return controller.task_complete(body,task_id,db)

#---------- Delete Task ------------
@task_routes.delete("/deleteTask/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db = Depends(get_db)):
    return controller.delete_task(task_id,db)