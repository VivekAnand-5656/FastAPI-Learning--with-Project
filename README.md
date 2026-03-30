# 📘 FastAPI Learning Journey

This repository documents my journey of learning backend development using **FastAPI**.  
The goal of this repo is to understand backend architecture, authentication, database integration, and REST API development step-by-step.

This is **not a production project**, but a structured learning playground where I implement concepts as I learn them.

---

## 🎯 Learning Goals

During this learning phase, I am focusing on:

- Understanding REST API architecture
- Building APIs using FastAPI
- Working with SQL databases using SQLAlchemy
- Implementing JWT Authentication
- Learning project structure used in real backend applications
- Practicing clean code & layered architecture

---

## 🧠 Concepts Covered So Far

### 🔹 FastAPI Basics
- Creating routes
- Request & response handling
- Status codes
- Swagger documentation

### 🔹 Project Architecture
Structured backend using real-world architecture:

src/
- users → user module (register & login)
- tasks → task module (CRUD)
- utils → database & helpers
- main.py → application entry point

This helped me understand:
- Routers
- Controllers
- DTOs (Schemas)
- Models
- Dependency Injection

---

### 🔹 Database Integration
- SQLAlchemy ORM
- Database sessions
- Models & relationships
- CRUD operations

---

### 🔹 Authentication (JWT)
Implemented complete authentication flow:

1️⃣ Register user  
2️⃣ Login user  
3️⃣ Generate JWT token  
4️⃣ Protect routes using authentication middleware  
5️⃣ Access only logged-in user's data  

This was my first real experience building secure APIs 🔐

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT (JSON Web Tokens)
- Uvicorn

---

## ▶️ How to Run This Project

### 1️⃣ Create virtual environment
python -m venv venv

### 2️⃣ Activate environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3️⃣ Install dependencies
pip install fastapi uvicorn sqlalchemy python-jose passlib[bcrypt]

### 4️⃣ Run the server
uvicorn main:app --reload

### 5️⃣ Open Swagger Docs
http://127.0.0.1:8000/docs

---

## 📌 Implemented APIs

### 👤 User APIs
- Register User
- Login User (JWT Token)

### ✅ Task APIs
- Create Task (Protected)
- Get My Tasks (Protected)
- Update Task (Protected)
- Delete Task (Protected)

---

## 🚀 What I Learned From This Repo

- How backend actually works behind frontend apps
- How authentication is implemented in real apps
- How to structure backend like industry projects
- How APIs communicate with database
- How to debug backend errors

---

## 📈 Next Learning Goals

- Refresh tokens
- Role based authorization
- Dockerizing FastAPI app
- PostgreSQL integration
- Deploying FastAPI

---

## 👨‍💻 Author

**Vivek Anand**  
Backend Developer in progress 🚀