from fastapi import APIRouter, HTTPException, Depends
from schemas.task_schema import Task, TaskCreate
from utils.auth import verify_token

router = APIRouter()
tasks_db = {}

@router.post("/tasks", response_model=Task)
def create_task(task: TaskCreate, token: str = Depends(verify_token)):
    if task.id in tasks_db:
        raise HTTPException(status_code=400, detail="Task ID already exists")
    tasks_db[task.id] = task
    return task

@router.get("/tasks")
def list_tasks(token: str = Depends(verify_token)):
    return list(tasks_db.values())

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, token: str = Depends(verify_token)):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskCreate, token: str = Depends(verify_token)):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db[task_id] = task
    return task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, token: str = Depends(verify_token)):
    if task_id in tasks_db:
        del tasks_db[task_id]
        return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
