from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models.task import Task
from schemas import TaskCreate
from db import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/tasks/")
async def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        completed=task_data.completed
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"task": {
        "id": new_task.id,
        "title": new_task.title,
        "description": new_task.description,
        "completed": new_task.completed
    }}
