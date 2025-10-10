from fastapi import FastAPI
from routers import employees, tasks

app = FastAPI(title="Employee Task Tracker API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee Task Tracker API"}

app.include_router(employees.router, tags=["Employees"])
app.include_router(tasks.router, tags=["Tasks"])

