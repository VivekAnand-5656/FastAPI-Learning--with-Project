
from src.tasks.dtos import TaskSchema,TaskComplete
from sqlalchemy.orm import Session    # Type of DB
from src.tasks.models import TaskManager
from fastapi import HTTPException 
# ------- Create Tasks --------
def create_task(body:TaskSchema, db:Session):
    data = body.model_dump()
    print(body.model_dump())
    new_task = TaskManager(
        title = data["title"],
        description = data["description"],
        is_completed = data["is_completed"]
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# ------------- Get Tasks --------
def get_all_tasks(db:Session):
    tasks = db.query(TaskManager).all()
    return tasks

# ------ Get Task By Id -----
def get_one_task(task_id:int,db:Session):
    one_task = db.query(TaskManager).get(task_id)
    if not one_task:
        raise HTTPException(404,detail="Task not found")
    return  one_task

# ----------- Update Task By Id ---------
def update_task_by_id(body:TaskSchema,task_id:int,db=Session):
    one_task = db.query(TaskManager).get(task_id)
    if not one_task:
        raise HTTPException(404,detail="Task Not Found")
    one_task.title = body.title
    one_task.description = body.description
    one_task.is_completed = body.is_completed

    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return one_task

# --------- Task Complete -------
def task_complete(body:TaskComplete,task_id:int,db=Session):
    one_task = db.get(TaskManager,task_id)
    if not one_task:
        raise HTTPException(status_code=404,detail="Task not found")
    
    one_task.is_completed = body.is_completed
 
    db.commit()
    db.refresh(one_task)

    return one_task

# ------------- Delete Task --------
def delete_task(task_id:int,db=Session):
    one_task = db.query(TaskManager).get(task_id)
    if not one_task:
        raise HTTPException(status_code=404,detail="Task Not Found")
    
    db.delete(one_task)
    db.commit()

    return {
        "status":"Task Deleted Successfully"
    }