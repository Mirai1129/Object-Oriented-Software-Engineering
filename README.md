# Object-Oriented Software Engineering Course Project: Interactive Classroom Management System

## Project Overview

This project is a comprehensive classroom management system developed as part of an Object-Oriented Software Engineering
course. The system consists of two primary subsystems:

1. Rollcall System: A digital attendance tracking solution for monitoring student presence during classes.
2. Participation System: An interactive classroom engagement platform that allows teachers to ask questions, record
   student
   responses, and track participation grades.

## Key Features

### Rollcall System

* Digital attendance tracking
* Real-time student check-in
* Attendance record management
* Detailed attendance reports

### Participation System

* In-class interactive questioning
* Response tracking
* Participation grade recording
* Performance analytics

### Technology Stack

* Backend Framework: FastAPI
* Database: MySQL
* ORM: SQLAlchemy
* Authentication: JWT (JSON Web Token)
* Password Management: Passlib (bcrypt)
* Environment Configuration: Python-dotenv

### System Architecture

The project follows object-oriented design principles, separating concerns into distinct modules for:

* User management
* Authentication
* Attendance tracking
* Classroom participation
* Grading and reporting

## Installation and Setup

### Prerequisites

* Python 3.8+
* MySQL
* pip (Python package manager)

### Database Initialization
The project includes an `init.sql` script in the root directory for database setup.

### Environment Configuration
Create a `.env` file with the following configuration:

```bash
# Database settings
USERNAME=your mysql username
PASSWORD=your mysql password
HOST=your mysql host
PORT=your mysql port
ROLLCALL_DATABASE=Rollcall
PARTICIPATION_DATABASE=Participation

# Secrets
ROLLCALL_SECRET=RollcallCoolSecret
PARTICIPATION_SECRET=ParticipationCoolSecret
```

### Installation Steps(With Docker)

```bash
docker compose up -d
```

### Installation Steps(Without Docker)

1. Clone the repository

```bash
git clone https://github.com/Mirai1129/Object-Oriented-Software-Engineering.git
cd Object-Oriented-Software-Engineering
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Initialize database

```bash
# Use the provided init.sql script
mysql -u root -p < init.sql
```

4. Start the application

```bash
uvicorn main:app --reload
```

## API Documentation

### Explore the API endpoints via Swagger UI at:
`http://127.0.0.1:8000/docs`
