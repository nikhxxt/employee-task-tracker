from fastapi import APIRouter, Depends, HTTPException, Query
from schemas.task_schema import TaskCreate, TaskUpdate, Task
from utils.auth import token_auth

router = APIRouter(prefix="/tasks", tags=["Tasks"])

tasks_db = {}
task_id_counter = 1

@router.post("/", response_model=Task, summary="Create a new task")
def create_task(task: TaskCreate, token: str = Depends(token_auth)):
    global task_id_counter
    new_task = task.dict()
    new_task["id"] = task_id_counter
    tasks_db[task_id_counter] = new_task
    task_id_counter += 1
    return new_task

@router.get("/", response_model=list[Task], summary="Get all tasks")
def get_tasks(status: str = Query(None), assigned_to: int = Query(None)):
    results = list(tasks_db.values())
    if status:
        results = [t for t in results if t["status"] == status]
    if assigned_to:
        results = [t for t in results if t["assigned_to"] == assigned_to]
    return results

@router.get("/{task_id}", response_model=Task, summary="Get task by ID")
def get_task(task_id: int):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=Task, summary="Update task")
def update_task(task_id: int, update: TaskUpdate, token: str = Depends(token_auth)):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    update_data = update.dict(exclude_unset=True)
    task.update(update_data)
    return task

@router.delete("/{task_id}", summary="Delete task")
def delete_task(task_id: int, token: str = Depends(token_auth)):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks_db[task_id]
    return {"detail": "Task deleted"}
