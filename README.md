
# 🧑‍💼 Employee Task Tracker API

A modular FastAPI project designed to help organizations manage employees and their assigned tasks efficiently. Built for hands-on learning, this mini project demonstrates real-world backend practices including routing, validation, authentication, and documentation.

---

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Repo Size](https://img.shields.io/github/repo-size/nikhxxt/employee-task-tracker-)
![GitHub Stars](https://img.shields.io/github/stars/nikhxxt/employee-task-tracker-?style=social)
![GitHub Forks](https://img.shields.io/github/forks/nikhxxt/employee-task-tracker-?style=social)

---

## 📚 Table of Contents

- [📚 Project Description](#project-description)
- [🎯 Objectives](#objectives)
- [🔑 Core Features](#core-features)
- [📁 Project Structure](#project-structure)
- [📡 Live Demo](#live-demo)
- [🚀 Getting Started](#getting-started)
- [🔐 Authentication Example](#authentication-example)
- [📝 License](#license)
- [🙌 Author](#author)

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

## 📁 Project Structure

```
task_tracker/
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
├── vercel.json
├── LICENSE
└── README.md
```

---

## 📡 Live Demo

Check out the deployed API on Vercel:  
🔗 [employee-task-tracker.vercel.app](https://employee-task-tracker-gfy4sufrd-niks-projects-20063e2f.vercel.app?_vercel_share=A0f9BFLCHHNf5Pbg1PXZUrd7gfRj9mm8)

---

## 🚀 Getting Started

### Clone & Run Locally

```bash
git clone https://github.com/nikhxxt/employee-task-tracker-.git
cd employee-task-tracker-

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

---

## 🙌 Author

Created by [Malki Shaik Nikhat Naaz](https://github.com/nikhxxt)  
Mini Project for G36 Python — Submitted to Bhargavesh Dakka  
Due: **14 Oct** | Points: **100**

---

© 2025 • Built with FastAPI for real-world backend mastery
```
