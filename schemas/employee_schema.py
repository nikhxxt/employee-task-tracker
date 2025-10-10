from pydantic import BaseModel, EmailStr

class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    role: str
    department: str

class Employee(EmployeeCreate):
    pass
