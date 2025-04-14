from sqlalchemy.orm import Session
from models.task import Task
from schemas.schemas import TaskCreate
from fastapi import HTTPException

class TaskService:
    @staticmethod
    def create_task(db: Session, task_data: TaskCreate) -> Task:
        new_task = Task(
            title=task_data.title,
            description=task_data.description,
            completed=task_data.completed,
            due_date=task_data.due_date 
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task

    @staticmethod
    def get_task(db: Session, task_id: int) -> Task:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    @staticmethod
    def update_task(db: Session, task_id: int, task_data: TaskCreate) -> Task:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        task.title = task_data.title
        task.description = task_data.description
        task.completed = task_data.completed
        task.due_date = task_data.due_date
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def delete_task(db: Session, task_id: int) -> None:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        db.delete(task)
        db.commit()

    @staticmethod
    def get_tasks(db: Session) -> list[Task]:
        return db.query(Task).all()
