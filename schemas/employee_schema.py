from pydantic import BaseModel, EmailStr

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    role: str
    department: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: str | None = None
    role: str | None = None
    department: str | None = None

class Employee(EmployeeBase):
    id: int
