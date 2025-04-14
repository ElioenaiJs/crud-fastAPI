from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.task import Task
from schemas.schemas import TaskCreate, TaskResponse
from db.db import get_db

router = APIRouter()

@router.post("/", summary="Crear nueva tarea")
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

@router.get("/{id}", response_model=TaskResponse, summary="Obtener tarea por ID")
async def get_task(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{id}", response_model=TaskResponse, summary="Actualizar tarea por ID")
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

@router.delete("/{id}", summary="Eliminar tarea por ID")
async def delete_task(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return {"detail": "Task deleted successfully"}

@router.get("/", response_model=list[TaskResponse], summary="Obtener todas las tareas")
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks