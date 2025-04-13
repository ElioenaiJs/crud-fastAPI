from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models.task import Task
from schemas import TaskCreate, TaskResponse
from db import get_db
from fastapi import HTTPException

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

@app.get("/{id}", response_model=TaskResponse)
async def get_task(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/{id}", response_model=TaskResponse)
async def update_task(id: int, task_data: TaskCreate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.title = task_data.title
    task.description = task_data.description
    task.completed = task_data.completed
    db.commit()
    db.refresh(task)
    return task

@app.delete("/{id}")
async def delete_task(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return {"detail": "Task deleted successfully"}

@app.get("/tasks/", response_model=list[TaskResponse])
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks