-- MySQL dump 10.13  Distrib 8.4.3, for Linux (x86_64)
--
-- Host: localhost    Database: Rollcall
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
-- Table structure for table `AttendanceRecord`
--

DROP TABLE IF EXISTS `AttendanceRecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AttendanceRecord` (
  `record_id` int NOT NULL AUTO_INCREMENT,
  `course_id` varchar(20) NOT NULL,
  `student_id` varchar(20) NOT NULL,
  `attendance_date` date NOT NULL,
  `attendance_status` tinyint(1) NOT NULL,
  `modified_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`record_id`),
  KEY `CourseID` (`course_id`),
  KEY `StudentID` (`student_id`),
  CONSTRAINT `AttendanceRecord_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `Course` (`course_id`),
  CONSTRAINT `AttendanceRecord_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `Student` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AttendanceRecord`
--

LOCK TABLES `AttendanceRecord` WRITE;
/*!40000 ALTER TABLE `AttendanceRecord` DISABLE KEYS */;
INSERT INTO `AttendanceRecord` VALUES (1,'3137','B11023024','2024-11-04',1,'2024-11-27 06:21:21'),(2,'CSE101','S20241129','2024-12-07',1,'2024-12-07 20:57:33'),(3,'CSE202','S20241129','2024-12-07',1,'2024-12-07 21:21:20');
/*!40000 ALTER TABLE `AttendanceRecord` ENABLE KEYS */;
UNLOCK TABLES;

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
  `academic_year` varchar(100) DEFAULT NULL,
  `is_rollcall_opened` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`course_id`),
  KEY `TeacherID` (`teacher_id`),
  CONSTRAINT `Course_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `Teacher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Course`
--

LOCK TABLES `Course` WRITE;
/*!40000 ALTER TABLE `Course` DISABLE KEYS */;
INSERT INTO `Course` VALUES ('1233','T12345678','早安吉祥宣傳隊','2020',0),('3137','T12345678','物件導向軟體工程','2024',0),('CSE101','T12345678','小丑課程','2025',0),('CSE202','T12345678','Introduction to Programming','2024-Fall',1);
/*!40000 ALTER TABLE `Course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CourseEnrollment`
--

DROP TABLE IF EXISTS `CourseEnrollment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CourseEnrollment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` varchar(20) NOT NULL,
  `course_id` varchar(20) NOT NULL,
  `semester` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `StudentID` (`student_id`),
  KEY `CourseID` (`course_id`),
  CONSTRAINT `CourseEnrollment_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `Student` (`id`),
  CONSTRAINT `CourseEnrollment_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `Course` (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CourseEnrollment`
--

LOCK TABLES `CourseEnrollment` WRITE;
/*!40000 ALTER TABLE `CourseEnrollment` DISABLE KEYS */;
INSERT INTO `CourseEnrollment` VALUES (1,'B11023024','3137','1131'),(4,'S12345678','CSE101','2024-Spring'),(5,'S12345678','CSE101','2024-Spring');
/*!40000 ALTER TABLE `CourseEnrollment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Student`
--

DROP TABLE IF EXISTS `Student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Student` (
  `id` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Student`
--

LOCK TABLES `Student` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Student` VALUES ('B11023024','陳仁傑'),('S12345678','小丑'),('S20241129','Mirai');
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Teacher`
--

DROP TABLE IF EXISTS `Teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Teacher` (
  `id` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teacher`
--

LOCK TABLES `Teacher` WRITE;
/*!40000 ALTER TABLE `Teacher` DISABLE KEYS */;
INSERT INTO `Teacher` VALUES ('T12345678','黃昭義');
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
  `password` varchar(255) DEFAULT NULL,
  `role` int DEFAULT NULL,
  PRIMARY KEY (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES ('S20241129','$2b$12$96.DyFAeUajpUXiO5vDDGuSghtFnw3QiLsakvAWBN1QyTWC3/1DSy',0),('T12345678','$2b$12$96.DyFAeUajpUXiO5vDDGuSghtFnw3QiLsakvAWBN1QyTWC3/1DSy',1);
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

-- Dump completed on 2024-12-07 14:05:55
