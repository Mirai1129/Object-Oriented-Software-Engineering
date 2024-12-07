# Rollcall System

Rollcall is a student attendance management system based on MySQL and FastAPI. This system allows teachers and students
to view and update attendance records, and provides management functions for related data. The system can be used in
schools or other institutions to manage course attendance.

## Table of Contents

- [Introduction](#introduction)
- [Technology Stack](#technology-stack)
- [Installation and Running](#installation-and-running)
- [Feature Description](#feature-description)
- [API Documentation](#api-documentation)
- [Database Backup and Restoration](#database-backup-and-restoration)
- [License](#license)

## Introduction

The Rollcall system provides the following basic functions:

- Student login and attendance record viewing
- Teachers can view and update student attendance records
- Filter attendance records by course, date range, and other conditions

The backend of this system is developed using **FastAPI**, and the frontend can be any application that needs to
interact with the API, whether web or mobile.

## Technology Stack

- **Backend**: FastAPI (Python)
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Authentication Method**: JWT (JSON Web Token)

## Installation and Running

### 1. Clone the Project

```bash
git clone https://github.com/Mirai1129/Object-Oriented-Software-Engineering.git
```

### 2. Install Dependencies

Install Python dependencies using pip:

```bash
pip install -r requirements.txt
```

### 3. Configure Database

Ensure that your MySQL database is installed and running. You can create a new database to store Rollcall system data:

```sql
CREATE
DATABASE rollcall;
```

### 4. Set Environment Variables

Set database configuration and key environment variables. You can configure the following variables in the `.env` file:

```ini
USERNAME = your database username
PASSWORD = your database password
HOST = your database host
PORT = your database port
ROLLCALL_DATABASE = Rollcall
PARTICIPATION_DATABASE = Participation
```

### 5. Start FastAPI Service

Start the FastAPI service, which will run by default at http://127.0.0.1:8000:

```bash
uvicorn main:app --reload
```
