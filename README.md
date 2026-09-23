# 🧑‍💼 Employee Task Tracker API

A modular **FastAPI backend** for managing employees and assigned tasks. The project demonstrates RESTful CRUD operations, Pydantic validation, request authentication, filtering, error handling, and automatic API documentation.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Render Status](https://img.shields.io/badge/Render-Live-blue)

## 🔑 Features

### Employee Management

* Create, retrieve, update, and delete employees
* Retrieve employees by ID
* Request/response validation using Pydantic

### Task Management

* Create, retrieve, update, and delete tasks
* Assign tasks to employees
* Filter tasks by status or employee ID
* Track task status:

  * `pending`
  * `in_progress`
  * `done`

### Authentication

Protected endpoints use a simple header-based token:

```text
x-token: work123
```

> `work123` is a demonstration token for this project and is not intended for production authentication.

### API Documentation

* Swagger UI
* ReDoc
* OpenAPI 3
* Organized route documentation

## 📡 API Endpoints

### Employees

| Method   | Endpoint                   | Description           |
| -------- | -------------------------- | --------------------- |
| `POST`   | `/employees/`              | Create an employee    |
| `GET`    | `/employees/`              | Get all employees     |
| `GET`    | `/employees/{employee_id}` | Get an employee by ID |
| `PUT`    | `/employees/{employee_id}` | Update an employee    |
| `DELETE` | `/employees/{employee_id}` | Delete an employee    |

### Tasks

| Method   | Endpoint           | Description      |
| -------- | ------------------ | ---------------- |
| `POST`   | `/tasks/`          | Create a task    |
| `GET`    | `/tasks/`          | Get all tasks    |
| `GET`    | `/tasks/{task_id}` | Get a task by ID |
| `PUT`    | `/tasks/{task_id}` | Update a task    |
| `DELETE` | `/tasks/{task_id}` | Delete a task    |

## 🛠️ Tech Stack

**Python 3.10+ · FastAPI · Pydantic · Uvicorn · OpenAPI · Swagger UI · ReDoc · Render**

## 📁 Project Structure

```text
employee-task-tracker/
├── main.py
├── routers/
│   ├── employees.py
│   └── tasks.py
├── schemas/
│   ├── employee_schema.py
│   └── task_schema.py
├── utils/
│   └── auth.py
├── requirements.txt
├── LICENSE
└── README.md
```

## 🌐 Live Demo

**Swagger:**
https://employee-task-tracker-eyac.onrender.com/docs

**ReDoc:**
https://employee-task-tracker-eyac.onrender.com/redoc

The API can be tested directly through Swagger UI.

> **Note:** The project uses in-memory data storage. Data may reset when the application restarts or redeploys.

## 🚀 Run Locally

```bash
git clone https://github.com/nikhxxt/employee-task-tracker.git
cd employee-task-tracker
pip install -r requirements.txt
uvicorn main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## 🔐 Example Request

```bash
curl -X POST http://127.0.0.1:8000/employees/ \
  -H "x-token: work123" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Nikhat",
    "email": "nikhat@example.com",
    "role": "Backend Developer",
    "department": "Engineering"
  }'
```

## 📄 License

This project is licensed under the **MIT License**.


