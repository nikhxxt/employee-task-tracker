# main.py
from fastapi import FastAPI
from routers import employees, tasks

app = FastAPI(
    title="Employee Task Tracker API",
    description="Manage employees and tasks with secure token-based access. Built with FastAPI.",
    version="1.0.0"
)

# Include routers
app.include_router(employees.router)
app.include_router(tasks.router)
