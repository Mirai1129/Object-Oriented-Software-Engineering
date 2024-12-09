-- MySQL dump 10.13  Distrib 8.4.3, for Linux (x86_64)
--
-- Host: localhost    Database: Participation
-- ------------------------------------------------------
-- Server version	8.4.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Course`
--

DROP TABLE IF EXISTS `Course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Course` (
                          `course_id` varchar(20) NOT NULL,
                          `teacher_id` varchar(20) NOT NULL,
                          `name` varchar(100) NOT NULL,
                          `semester` varchar(20) NOT NULL,
                          PRIMARY KEY (`course_id`),
                          KEY `TeacherID` (`teacher_id`),
                          CONSTRAINT `Course_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `Teacher` (`teacher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Course`
--

LOCK TABLES `Course` WRITE;
/*!40000 ALTER TABLE `Course` DISABLE KEYS */;
INSERT INTO `Course` VALUES ('3137','T12345678','物件導向軟體工程','1131');
/*!40000 ALTER TABLE `Course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CourseEnrollment`
--

DROP TABLE IF EXISTS `CourseEnrollment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CourseEnrollment` (
                                    `enrollment_id` varchar(20) NOT NULL,
                                    `course_id` varchar(20) NOT NULL,
                                    `student_id` varchar(20) NOT NULL,
                                    PRIMARY KEY (`enrollment_id`),
                                    KEY `CourseID` (`course_id`),
                                    KEY `StudentID` (`student_id`),
                                    CONSTRAINT `CourseEnrollment_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `Course` (`course_id`),
                                    CONSTRAINT `CourseEnrollment_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `Student` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CourseEnrollment`
--

LOCK TABLES `CourseEnrollment` WRITE;
/*!40000 ALTER TABLE `CourseEnrollment` DISABLE KEYS */;
INSERT INTO `CourseEnrollment` VALUES ('1','3137','B11023024');
/*!40000 ALTER TABLE `CourseEnrollment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Department`
--

DROP TABLE IF EXISTS `Department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Department` (
                              `dept_num` varchar(20) NOT NULL,
                              `dept_name` varchar(100) NOT NULL,
                              PRIMARY KEY (`dept_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Department`
--

LOCK TABLES `Department` WRITE;
/*!40000 ALTER TABLE `Department` DISABLE KEYS */;
INSERT INTO `Department` VALUES ('1111','資訊管理系');
/*!40000 ALTER TABLE `Department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ParticipationGrade`
--

DROP TABLE IF EXISTS `ParticipationGrade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ParticipationGrade` (
                                      `grade_id` varchar(20) NOT NULL,
                                      `course_id` varchar(20) NOT NULL,
                                      `student_id` varchar(20) NOT NULL,
                                      `grade` decimal(5,2) NOT NULL,
                                      `generated_date` date NOT NULL,
                                      PRIMARY KEY (`grade_id`),
                                      KEY `CourseID` (`course_id`),
                                      KEY `StudentID` (`student_id`),
                                      CONSTRAINT `ParticipationGrade_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `Course` (`course_id`),
                                      CONSTRAINT `ParticipationGrade_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `Student` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ParticipationGrade`
--

LOCK TABLES `ParticipationGrade` WRITE;
/*!40000 ALTER TABLE `ParticipationGrade` DISABLE KEYS */;
INSERT INTO `ParticipationGrade` VALUES ('1','3137','B11023024',100.00,'2024-11-04');
/*!40000 ALTER TABLE `ParticipationGrade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ParticipationRecord`
--

DROP TABLE IF EXISTS `ParticipationRecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ParticipationRecord` (
                                       `student_id` varchar(20) NOT NULL,
                                       `grade_id` varchar(20) NOT NULL,
                                       `date` date NOT NULL,
                                       `modified_time` datetime DEFAULT CURRENT_TIMESTAMP,
                                       PRIMARY KEY (`student_id`,`grade_id`),
                                       KEY `GradeID` (`grade_id`),
                                       CONSTRAINT `ParticipationRecord_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `Student` (`student_id`),
                                       CONSTRAINT `ParticipationRecord_ibfk_2` FOREIGN KEY (`grade_id`) REFERENCES `ParticipationGrade` (`grade_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ParticipationRecord`
--

LOCK TABLES `ParticipationRecord` WRITE;
/*!40000 ALTER TABLE `ParticipationRecord` DISABLE KEYS */;
INSERT INTO `ParticipationRecord` VALUES ('B11023024','1','2024-11-04','2024-11-27 06:26:01');
/*!40000 ALTER TABLE `ParticipationRecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Role`
--

DROP TABLE IF EXISTS `Role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Role` (
                        `id` varchar(20) NOT NULL,
                        `name` varchar(50) NOT NULL,
                        `permission` varchar(100) NOT NULL,
                        PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Role`
--

LOCK TABLES `Role` WRITE;
/*!40000 ALTER TABLE `Role` DISABLE KEYS */;
INSERT INTO `Role` VALUES ('1','Student','1'),('2','Teacher','2');
/*!40000 ALTER TABLE `Role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Student`
--

DROP TABLE IF EXISTS `Student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Student` (
                           `student_id` varchar(20) NOT NULL,
                           `user_id` varchar(20) NOT NULL,
                           `dept_num` varchar(20) NOT NULL,
                           `name` varchar(50) NOT NULL,
                           PRIMARY KEY (`student_id`),
                           KEY `UserID` (`user_id`),
                           KEY `DeptNo` (`dept_num`),
                           CONSTRAINT `Student_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`account`),
                           CONSTRAINT `Student_ibfk_2` FOREIGN KEY (`dept_num`) REFERENCES `Department` (`dept_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Student`
--

LOCK TABLES `Student` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Student` VALUES ('B11023024','B11023024','1111','陳仁傑');
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Teacher`
--

DROP TABLE IF EXISTS `Teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Teacher` (
                           `teacher_id` varchar(20) NOT NULL,
                           `user_id` varchar(20) NOT NULL,
                           `specialization` varchar(100) NOT NULL,
                           `name` varchar(50) NOT NULL,
                           PRIMARY KEY (`teacher_id`),
                           KEY `UserID` (`user_id`),
                           CONSTRAINT `Teacher_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teacher`
--

LOCK TABLES `Teacher` WRITE;
/*!40000 ALTER TABLE `Teacher` DISABLE KEYS */;
INSERT INTO `Teacher` VALUES ('T12345678','T12345678','OO','黃昭義');
/*!40000 ALTER TABLE `Teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
                        `account` varchar(50) NOT NULL,
                        `password` varchar(255) NOT NULL,
                        `role_id` varchar(20) NOT NULL,
                        PRIMARY KEY (`account`),
                        KEY `RoleID` (`role_id`),
                        CONSTRAINT `User_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `Role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES ('B11023024','123','1'),('T12345678','123','2');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-09  1:52:46
