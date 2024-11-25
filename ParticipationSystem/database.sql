CREATE DATABASE Rollcall;

USE Rollcall;

-- 建立 Teacher 表格
CREATE TABLE Teacher (
                         TeacherID INT AUTO_INCREMENT PRIMARY KEY,  -- 教師 ID，自動遞增
                         Password VARCHAR(255) NOT NULL,             -- 密碼
                         Name VARCHAR(255) NOT NULL                  -- 教師姓名
);

-- 建立 Student 表格
CREATE TABLE Student (
                         StudentID INT AUTO_INCREMENT PRIMARY KEY,  -- 學生 ID，自動遞增
                         Name VARCHAR(255) NOT NULL                  -- 學生姓名
);

-- 建立 Course 表格
CREATE TABLE Course (
                        CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- 課程 ID，自動遞增
                        TeacherID INT NOT NULL,                   -- 教師 ID
                        CourseName VARCHAR(255) NOT NULL,          -- 課程名稱
                        FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID)  -- 外鍵，連接 Teacher 表格
);

-- 建立 CourseEnrollment 表格
CREATE TABLE CourseEnrollment (
                                  EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,  -- 選課 ID，自動遞增
                                  StudentID INT NOT NULL,                       -- 學生 ID
                                  CourseID INT NOT NULL,                        -- 課程 ID
                                  Semester VARCHAR(50) NOT NULL,                -- 學期
                                  FOREIGN KEY (StudentID) REFERENCES Student(StudentID),  -- 外鍵，連接 Student 表格
                                  FOREIGN KEY (CourseID) REFERENCES Course(CourseID)     -- 外鍵，連接 Course 表格
);

-- 建立 AttendanceRecord 表格
CREATE TABLE AttendanceRecord (
                                  RecordID INT AUTO_INCREMENT PRIMARY KEY,  -- 記錄 ID，自動遞增
                                  CourseID INT NOT NULL,                    -- 課程 ID
                                  StudentID INT NOT NULL,                   -- 學生 ID
                                  AttendanceDate DATE NOT NULL,             -- 出席日期
                                  AttendanceStatus VARCHAR(50) NOT NULL,    -- 出席狀態
                                  FOREIGN KEY (CourseID) REFERENCES Course(CourseID),   -- 外鍵，連接 Course 表格
                                  FOREIGN KEY (StudentID) REFERENCES Student(StudentID)  -- 外鍵，連接 Student 表格
);
