# Team Task Manager

## Overview

Team Task Manager is a full-stack web application built using Flask and MySQL for managing projects and team tasks.

The application supports:

* User authentication using JWT
* Role-based access control
* Project creation
* Task assignment and tracking
* Task status updates
* Dashboard management

---

## Tech Stack

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-JWT-Extended
* MySQL

### Frontend

* HTML
* Bootstrap 5
* JavaScript

---

## Features

* User Registration & Login
* JWT Authentication
* Admin & Member Roles
* Create Projects
* Create Tasks
* Assign Tasks to Users
* Update Task Status
* Dashboard with Task Tracking
* MySQL Database Integration

---

## Project Structure

```text
team-task-manager/
│
├── backend/
│   ├── models/
│   ├── app.py
│   ├── config.py
│   └── extensions.py
│
├── frontend/
│   ├── login.html
│   └── dashboard.html
│
├── requirements.txt
└── README.md
```

---

## API Endpoints

| Method | Endpoint         | Description        |
| ------ | ---------------- | ------------------ |
| POST   | /register        | Register User      |
| POST   | /login           | Login User         |
| POST   | /projects        | Create Project     |
| POST   | /tasks           | Create Task        |
| GET    | /tasks           | Get Tasks          |
| PUT    | /tasks/<task_id> | Update Task Status |

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL

Create database:

```sql
CREATE DATABASE task_manager;
```

Update `config.py`:

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:YOUR_PASSWORD@localhost/task_manager"
```

### 6. Run Backend

```bash
cd backend
python app.py
```

### 7. Run Frontend

Open `frontend/login.html` using Live Server.

---

## Test Credentials

```text
Email: test@gmail.com
Password: 123456
```

---

## Author

Chandrakanth
