-- MySQL Conversion of Rollcall Database

-- Create Database
CREATE DATABASE IF NOT EXISTS Rollcall;
USE Rollcall;

-- Create Teacher Table
CREATE TABLE `Teacher`
(
    `TeacherID` VARCHAR(20) NOT NULL,
    `Password`  VARCHAR(50) NOT NULL,
    `Name`      VARCHAR(50) NOT NULL,
    PRIMARY KEY (`TeacherID`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

-- Create Student Table
CREATE TABLE `Student`
(
    `StudentID` VARCHAR(20) NOT NULL,
    `Name`      VARCHAR(50) NOT NULL,
    PRIMARY KEY (`StudentID`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

-- Create Course Table
CREATE TABLE `Course`
(
    `CourseID`   VARCHAR(20)  NOT NULL,
    `TeacherID`  VARCHAR(20)  NOT NULL,
    `CourseName` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`CourseID`),
    FOREIGN KEY (`TeacherID`) REFERENCES `Teacher` (`TeacherID`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

-- Create CourseEnrollment Table
CREATE TABLE `CourseEnrollment`
(
    `EnrollmentID` INT AUTO_INCREMENT NOT NULL,
    `StudentID`    VARCHAR(20)        NOT NULL,
    `CourseID`     VARCHAR(20)        NOT NULL,
    `Semester`     VARCHAR(20)        NOT NULL,
    PRIMARY KEY (`EnrollmentID`),
    FOREIGN KEY (`StudentID`) REFERENCES `Student` (`StudentID`),
    FOREIGN KEY (`CourseID`) REFERENCES `Course` (`CourseID`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

-- Create AttendanceRecord Table
CREATE TABLE `AttendanceRecord`
(
    `RecordID`         INT AUTO_INCREMENT NOT NULL,
    `CourseID`         VARCHAR(20)        NOT NULL,
    `StudentID`        VARCHAR(20)        NOT NULL,
    `AttendanceDate`   DATE               NOT NULL,
    `AttendanceStatus` VARCHAR(10)        NOT NULL,
    `ModifiedTime`     DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`RecordID`),
    FOREIGN KEY (`CourseID`) REFERENCES `Course` (`CourseID`),
    FOREIGN KEY (`StudentID`) REFERENCES `Student` (`StudentID`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

-- Insert data into Teacher
INSERT INTO `Teacher` (`TeacherID`, `Password`, `Name`)
VALUES ('T12345678', '123', '黃昭義');

-- Insert data into Student
INSERT INTO `Student` (`StudentID`, `Name`)
VALUES ('B11023024', '陳仁傑');

-- Insert data into Course
INSERT INTO `Course` (`CourseID`, `TeacherID`, `CourseName`)
VALUES ('3137', 'T12345678', '物件導向軟體工程');

-- Insert data into CourseEnrollment
INSERT INTO `CourseEnrollment` (`StudentID`, `CourseID`, `Semester`)
VALUES ('B11023024', '3137', '1131');

-- Insert data into AttendanceRecord
INSERT INTO `AttendanceRecord` (`CourseID`, `StudentID`, `AttendanceDate`, `AttendanceStatus`)
VALUES ('3137', 'B11023024', '2024-11-04', 'true');
