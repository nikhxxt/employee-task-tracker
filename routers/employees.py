from fastapi import APIRouter, Depends, HTTPException
from schemas.employee_schema import EmployeeCreate, EmployeeUpdate, Employee
from utils.auth import token_auth

router = APIRouter(prefix="/employees", tags=["Employees"])

employees_db = {}
employee_id_counter = 1

@router.post("/", response_model=Employee, summary="Add a new employee")
def create_employee(employee: EmployeeCreate, token: str = Depends(token_auth)):
    global employee_id_counter
    new_employee = employee.dict()
    new_employee["id"] = employee_id_counter
    employees_db[employee_id_counter] = new_employee
    employee_id_counter += 1
    return new_employee

@router.get("/", response_model=list[Employee], summary="Get all employees")
def get_employees():
    return list(employees_db.values())

@router.get("/{employee_id}", response_model=Employee, summary="Get employee by ID")
def get_employee(employee_id: int):
    employee = employees_db.get(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.put("/{employee_id}", response_model=Employee, summary="Update employee")
def update_employee(employee_id: int, update: EmployeeUpdate, token: str = Depends(token_auth)):
    employee = employees_db.get(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    update_data = update.dict(exclude_unset=True)
    employee.update(update_data)
    return employee

@router.delete("/{employee_id}", summary="Delete employee")
def delete_employee(employee_id: int, token: str = Depends(token_auth)):
    if employee_id not in employees_db:
        raise HTTPException(status_code=404, detail="Employee not found")
    del employees_db[employee_id]
    return {"detail": "Employee deleted"}

