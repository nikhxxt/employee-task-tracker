e Task Tracker API

A modular FastAPI project designed to help organizations manage employees and their assigned tasks efficiently. Built for hands-on learning, this mini project demonstrates real-world backend practices including routing, validation, authentication, and documentation.

---

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Render Status](https://img.shields.io/badge/Render-Live-blue)
![Repo Size](https://img.shields.io/github/repo-size/nikhxxt/employee-task-tracker)
![GitHub Stars](https://img.shields.io/github/stars/nikhxxt/employee-task-tracker?style=social)
![GitHub Forks](https://img.shields.io/github/forks/nikhxxt/employee-task-tracker?style=social)

---

## 📚 Table of Contents

- [📚 Project Description](#project-description)
- [🎯 Objectives](#objectives)
- [🔑 Core Features](#core-features)
- [🛠️ Tech Stack](#tech-stack)
- [📁 Project Structure](#project-structure)
- [📡 Live Demo](#live-demo)
- [🚀 Getting Started](#getting-started)
- [🔐 Authentication Example](#authentication-example)
- [📝 License](#license)

---

## 📚 Project Description

This API simulates a backend system for HR or project managers to:
- Track employee information
- Monitor task progress
- Practice secure, modular API development

It uses **in-memory data storage** and showcases:
- Modular structure
- Input validation
- Response modeling
- Token-based authentication
- Auto-generated documentation

---

## 🎯 Objectives

- Build a modular FastAPI application with routers, schemas, and dependencies  
- Implement CRUD operations for employees and tasks  
- Validate data using Pydantic models  
- Apply path/query parameters, error handling, and response models  
- Add API documentation with tags, summaries, and examples  
- Implement simple token-based authentication  

---

## 🔑 Core Features

### 👥 Employee Management
- Add employees with `name`, `email`, `role`, and `department`
- View all or specific employee details
- Update or delete employee records

### ✅ Task Management
- Create, update, delete tasks
- Assign tasks to employees
- Filter tasks by `status` or `employee_id`
- Track progress: `pending`, `in_progress`, `done`

### 🔐 Authentication
- Header-based token validation:  
  `x-token: work123`

### 📚 Documentation
- Swagger UI: `/docs`  
- ReDoc: `/redoc`  
- Routes grouped with tags, summaries, and examples

---

## 🛠️ Tech Stack

- **FastAPI** – High-performance Python framework for building APIs  
- **Pydantic** – Data validation and serialization using Python type hints  
- **Uvicorn** – ASGI server for running FastAPI apps  
- **Python 3.10+** – Language runtime with async support  
- **Swagger UI & ReDoc** – Auto-generated API documentation  
- **Render** – Cloud platform for deploying web services  

---

## 📁 Project Structure

```
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

## 📡 Live Demo

Deployed on Render:  
🔗 [https://employee-task-tracker.onrender.com](https://employee-task-tracker.onrender.com)

> Note: Free Render services may take 30–60 seconds to wake up after inactivity.

---

## 🚀 Getting Started

### Clone & Run Locally

```bash
git clone https://github.com/nikhxxt/employee-task-tracker.git
cd employee-task-tracker

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

---

## 🔐 Authentication Example

Include this header in secured requests:

```
x-token: work123
```

---

## 📝 License

This project is licensed under the **MIT License** — see [`LICENSE`](LICENSE).
