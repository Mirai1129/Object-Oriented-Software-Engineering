-- Create Database
CREATE DATABASE Participation;
USE Participation;

-- Role Table
CREATE TABLE Role
(
    RoleID     VARCHAR(20)  NOT NULL,
    RoleName   VARCHAR(50)  NOT NULL,
    Permission VARCHAR(100) NOT NULL,
    PRIMARY KEY (RoleID)
) ENGINE = InnoDB;

-- Users Table
CREATE TABLE Users
(
    UserID   VARCHAR(20)  NOT NULL,
    Password VARCHAR(100) NOT NULL,
    RoleID   VARCHAR(20)  NOT NULL,
    PRIMARY KEY (UserID),
    FOREIGN KEY (RoleID) REFERENCES Role (RoleID)
) ENGINE = InnoDB;

-- Department Table
CREATE TABLE Department
(
    DeptNo   VARCHAR(20)  NOT NULL,
    DeptName VARCHAR(100) NOT NULL,
    PRIMARY KEY (DeptNo)
) ENGINE = InnoDB;

-- Teacher Table
CREATE TABLE Teacher
(
    TeacherID      VARCHAR(20)  NOT NULL,
    UserID         VARCHAR(20)  NOT NULL,
    Specialization VARCHAR(100) NOT NULL,
    TeacherName    VARCHAR(50)  NOT NULL,
    PRIMARY KEY (TeacherID),
    FOREIGN KEY (UserID) REFERENCES Users (UserID)
) ENGINE = InnoDB;

-- Student Table
CREATE TABLE Student
(
    StudentID VARCHAR(20) NOT NULL,
    UserID    VARCHAR(20) NOT NULL,
    DeptNo    VARCHAR(20) NOT NULL,
    Name      VARCHAR(50) NOT NULL,
    PRIMARY KEY (StudentID),
    FOREIGN KEY (UserID) REFERENCES Users (UserID),
    FOREIGN KEY (DeptNo) REFERENCES Department (DeptNo)
) ENGINE = InnoDB;

-- Course Table
CREATE TABLE Course
(
    CourseID   VARCHAR(20)  NOT NULL,
    TeacherID  VARCHAR(20)  NOT NULL,
    CourseName VARCHAR(100) NOT NULL,
    Semester   VARCHAR(20)  NOT NULL,
    PRIMARY KEY (CourseID),
    FOREIGN KEY (TeacherID) REFERENCES Teacher (TeacherID)
) ENGINE = InnoDB;

-- CourseEnrollment Table
CREATE TABLE CourseEnrollment
(
    EnrollmentID VARCHAR(20) NOT NULL,
    CourseID     VARCHAR(20) NOT NULL,
    StudentID    VARCHAR(20) NOT NULL,
    PRIMARY KEY (EnrollmentID),
    FOREIGN KEY (CourseID) REFERENCES Course (CourseID),
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
) ENGINE = InnoDB;

-- ParticipationGrade Table
CREATE TABLE ParticipationGrade
(
    GradeID   VARCHAR(20)   NOT NULL,
    CourseID  VARCHAR(20)   NOT NULL,
    StudentID VARCHAR(20)   NOT NULL,
    Grade     DECIMAL(5, 2) NOT NULL,
    Date      DATE          NOT NULL,
    PRIMARY KEY (GradeID),
    FOREIGN KEY (CourseID) REFERENCES Course (CourseID),
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID)
) ENGINE = InnoDB;

-- ParticipationRecord Table
CREATE TABLE ParticipationRecord
(
    StudentID    VARCHAR(20) NOT NULL,
    GradeID      VARCHAR(20) NOT NULL,
    Date         DATE        NOT NULL,
    ModifiedTime DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (StudentID, GradeID),
    FOREIGN KEY (StudentID) REFERENCES Student (StudentID),
    FOREIGN KEY (GradeID) REFERENCES ParticipationGrade (GradeID)
) ENGINE = InnoDB;

-- Insert sample data (same as original script)
INSERT INTO Role (RoleID, RoleName, Permission)
VALUES ('1', 'Student', '1'),
       ('2', 'Teacher', '2');

INSERT INTO Users (UserID, Password, RoleID)
VALUES ('B11023024', '123', '1'),
       ('T12345678', '123', '2');

INSERT INTO Department (DeptNo, DeptName)
VALUES ('1111', '資訊管理系');

INSERT INTO Teacher (TeacherID, UserID, Specialization, TeacherName)
VALUES ('T12345678', 'T12345678', 'OO', '黃昭義');

INSERT INTO Student (StudentID, UserID, DeptNo, Name)
VALUES ('B11023024', 'B11023024', '1111', '陳仁傑');

INSERT INTO Course (CourseID, TeacherID, CourseName, Semester)
VALUES ('3137', 'T12345678', '物件導向軟體工程', '1131');

INSERT INTO CourseEnrollment (EnrollmentID, CourseID, StudentID)
VALUES ('1', '3137', 'B11023024');

INSERT INTO ParticipationGrade (GradeID, CourseID, StudentID, Grade, Date)
VALUES ('1', '3137', 'B11023024', 100.00, '2024-11-04');

INSERT INTO ParticipationRecord (StudentID, GradeID, Date)
VALUES ('B11023024', '1', '2024-11-04');
