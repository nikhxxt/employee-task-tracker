# 🧑‍💼 Employee Task Tracker API

A modular FastAPI backend for managing employees and their assigned tasks. This project demonstrates practical backend concepts including API routing, data validation, CRUD operations, header-based authentication, error handling, and automatic API documentation.

---

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Render Status](https://img.shields.io/badge/Render-Live-blue)
![Repo Size](https://img.shields.io/github/repo-size/nikhxxt/employee-task-tracker)
![GitHub Stars](https://img.shields.io/github/stars/nikhxxt/employee-task-tracker?style=social)
![GitHub Forks](https://img.shields.io/github/forks/nikhxxt/employee-task-tracker?style=social)

---

## 📚 Table of Contents

- [📚 Project Description](#-project-description)
- [🎯 Objectives](#-objectives)
- [🔑 Features](#-features)
- [📡 API Endpoints](#-api-endpoints)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🌐 Live Demo](#-live-demo)
- [🚀 Getting Started](#-getting-started)
- [🔐 Authentication](#-authentication)
- [⚠️ Limitations](#️-limitations)
- [📝 License](#-license)

---

## 📚 Project Description

This API provides a simple backend for managing employees and their assigned tasks.

It demonstrates:

- Modular FastAPI application structure
- CRUD operations
- Pydantic-based data validation
- Request and response schemas
- Path and query parameters
- Error handling
- Header-based token authentication
- Automatic API documentation

The project uses in-memory data storage and is intended as a backend learning and portfolio project.

---

## 🎯 Objectives

- Build a modular FastAPI backend using routers, schemas, and dependencies
- Implement CRUD operations for employees and tasks
- Validate request data using Pydantic
- Handle path and query parameters
- Implement basic authentication using request headers
- Provide structured API responses
- Document the API using Swagger UI and ReDoc
- Deploy the application to Render

---

## 🔑 Features

### 👥 Employee Management

- Add employees
- View all employees
- View an employee by ID
- Update employee information
- Delete employees

### ✅ Task Management

- Create tasks
- Assign tasks to employees
- View tasks
- Update tasks
- Delete tasks
- Filter tasks by status or employee ID
- Track task status:
  - `pending`
  - `in_progress`
  - `done`

### 🔐 Authentication

Protected endpoints use a simple header-based token:

```text
x-token: work123
```

> `work123` is a demonstration token used for this project and is not intended for production authentication.

### 📚 API Documentation

- Swagger UI
- ReDoc
- OpenAPI 3 documentation
- Route grouping and endpoint descriptions

---

## 📡 API Endpoints

### Employees

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/employees/` | Create an employee |
| `GET` | `/employees/` | Get all employees |
| `GET` | `/employees/{employee_id}` | Get an employee by ID |
| `PUT` | `/employees/{employee_id}` | Update an employee |
| `DELETE` | `/employees/{employee_id}` | Delete an employee |

### Tasks

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/tasks/` | Create a task |
| `GET` | `/tasks/` | Get tasks |
| `GET` | `/tasks/{task_id}` | Get a task by ID |
| `PUT` | `/tasks/{task_id}` | Update a task |
| `DELETE` | `/tasks/{task_id}` | Delete a task |

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Pydantic**
- **Uvicorn**
- **Swagger UI**
- **ReDoc**
- **OpenAPI**
- **Render**

---

## 📁 Project Structure

```text
employee_task_tracker/
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

---

## 🌐 Live Demo

The API is deployed on Render.

**Swagger Documentation:**

https://employee-task-tracker-eyac.onrender.com/docs

**ReDoc:**

https://employee-task-tracker-eyac.onrender.com/redoc

You can use Swagger UI to interact with the API and test the available endpoints.

> Note: Free Render services may take some time to wake up after a period of inactivity.

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/nikhxxt/employee-task-tracker.git
cd employee-task-tracker
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## 🔐 Authentication

Protected endpoints require the following header:

```text
x-token: work123
```

### Example

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

The same header can be added to protected requests when using Swagger UI.

---

## ⚠️ Limitations

- Uses in-memory data storage, so data is not persistent across application restarts.
- Authentication uses a static demonstration token.
- No database integration is included.
- No user registration or login system is implemented.
- This project is intended as a learning and portfolio project rather than a production-ready system.

---

## 📝 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.


