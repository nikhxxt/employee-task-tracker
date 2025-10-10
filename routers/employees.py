from fastapi import APIRouter, HTTPException, Depends
from schemas.employee_schema import Employee, EmployeeCreate
from utils.auth import verify_token

router = APIRouter()
employees_db = {}

@router.post("/employees", response_model=Employee)
def create_employee(emp: EmployeeCreate, token: str = Depends(verify_token)):
    if emp.email in employees_db:
        raise HTTPException(status_code=400, detail="Employee already exists")
    employees_db[emp.email] = emp
    return emp

@router.get("/employees")
def list_employees(token: str = Depends(verify_token)):
    return list(employees_db.values())

@router.get("/employees/{email}", response_model=Employee)
def get_employee(email: str, token: str = Depends(verify_token)):
    emp = employees_db.get(email)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.put("/employees/{email}", response_model=Employee)
def update_employee(email: str, emp: EmployeeCreate, token: str = Depends(verify_token)):
    if email not in employees_db:
        raise HTTPException(status_code=404, detail="Employee not found")
    employees_db[email] = emp
    return emp

@router.delete("/employees/{email}")
def delete_employee(email: str, token: str = Depends(verify_token)):
    if email in employees_db:
        del employees_db[email]
        return {"detail": "Deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")
