from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import TaskCreate, TaskResponse
from db.db import get_db
from services.task_service import TaskService

router = APIRouter(prefix="/task/api/v1", tags=["Tasks"])

@router.post("/", summary="Crear nueva tarea")
async def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    new_task = TaskService.create_task(db, task_data)
    return new_task

@router.get("/overdue", response_model=list[TaskResponse], summary="Obtener tareas vencidas")
async def get_overdue_tasks(db: Session = Depends(get_db)):
    overdue_tasks = TaskService.get_overdue_tasks(db)
    return overdue_tasks

@router.get("/{id}", response_model=TaskResponse, summary="Obtener tarea por ID")
async def get_task(id: int, db: Session = Depends(get_db)):
    task = TaskService.get_task(db, id)
    return task

@router.put("/{id}", response_model=TaskResponse, summary="Actualizar tarea por ID")
async def update_task(id: int, task_data: TaskCreate, db: Session = Depends(get_db)):
    task = TaskService.update_task(db, id, task_data)
    return task

@router.delete("/{id}", summary="Eliminar tarea por ID")
async def delete_task(id: int, db: Session = Depends(get_db)):
    TaskService.delete_task(db, id)
    return {"detail": "Task deleted successfully"}

@router.get("/", response_model=list[TaskResponse], summary="Obtener todas las tareas")
async def get_tasks(db: Session = Depends(get_db)):
    tasks = TaskService.get_tasks(db)
    return tasks
