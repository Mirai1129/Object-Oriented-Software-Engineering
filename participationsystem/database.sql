-- MySQL dump 10.13  Distrib 8.4.3, for Linux (x86_64)
--
-- Host: localhost    Database: Participation
-- ------------------------------------------------------
-- Server version	8.4.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT = @@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS = @@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION = @@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE = @@TIME_ZONE */;
/*!40103 SET TIME_ZONE = '+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS, UNIQUE_CHECKS = 0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0 */;
/*!40101 SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES = @@SQL_NOTES, SQL_NOTES = 0 */;

--
-- Table structure for table `Course`
--

CREATE SCHEMA `Participation`;


DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User`
(
    `account`  varchar(50)  NOT NULL,
    `password` varchar(255) NOT NULL,
    `role`     int          NOT NULL,
    PRIMARY KEY (`account`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User`
    DISABLE KEYS */;
INSERT INTO `User`
VALUES ('B11023024', '$2b$12$z17x/lP3YmIFLkcEiMEiluCvTePELWUgamX4kVZ29O2eCyJMJmRge', 0),
       ('T12345678', '$2b$12$z17x/lP3YmIFLkcEiMEiluCvTePELWUgamX4kVZ29O2eCyJMJmRge', 1);
/*!40000 ALTER TABLE `User`
    ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `Student`
--

DROP TABLE IF EXISTS `Student`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Student`
(
    `student_id` varchar(20) NOT NULL,
    `user_id`    varchar(20) NOT NULL,
    `name`       varchar(50) NOT NULL,
    PRIMARY KEY (`student_id`),
    KEY `UserID` (`user_id`),
    CONSTRAINT `Student_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`account`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Student`
--

LOCK TABLES `Student` WRITE;
/*!40000 ALTER TABLE `Student`
    DISABLE KEYS */;
INSERT INTO `Student`
VALUES ('B11023024', 'B11023024', '陳仁傑');
/*!40000 ALTER TABLE `Student`
    ENABLE KEYS */;
UNLOCK TABLES;



--
-- Table structure for table `Teacher`
--

DROP TABLE IF EXISTS `Teacher`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Teacher`
(
    `teacher_id`     varchar(20)  NOT NULL,
    `user_id`        varchar(20)  NOT NULL,
    `specialization` varchar(100) NOT NULL,
    `name`           varchar(50)  NOT NULL,
    PRIMARY KEY (`teacher_id`),
    KEY `UserID` (`user_id`),
    CONSTRAINT `Teacher_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`account`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teacher`
--

LOCK TABLES `Teacher` WRITE;
/*!40000 ALTER TABLE `Teacher`
    DISABLE KEYS */;
INSERT INTO `Teacher`
VALUES ('T12345678', 'T12345678', 'OO', '黃昭義');
/*!40000 ALTER TABLE `Teacher`
    ENABLE KEYS */;
UNLOCK TABLES;



DROP TABLE IF EXISTS `Course`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Course`
(
    `course_id`  varchar(20)  NOT NULL,
    `teacher_id` varchar(20)  NOT NULL,
    `name`       varchar(100) NOT NULL,
    `semester`   varchar(20)  NOT NULL,
    PRIMARY KEY (`course_id`),
    KEY `TeacherID` (`teacher_id`),
    CONSTRAINT `Course_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `Teacher` (`teacher_id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Course`
--

LOCK TABLES `Course` WRITE;
/*!40000 ALTER TABLE `Course`
    DISABLE KEYS */;
INSERT INTO `Course`
VALUES ('3137', 'T12345678', '物件導向軟體工程', '1131');
/*!40000 ALTER TABLE `Course`
    ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ParticipationGrade`
--

DROP TABLE IF EXISTS `ParticipationGrade`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ParticipationGrade`
(
    `grade_id`       varchar(20)   NOT NULL,
    `course_id`      varchar(20)   NOT NULL,
    `student_id`     varchar(20)   NOT NULL,
    `grade`          decimal(5, 2) NOT NULL,
    `generated_date` date          NOT NULL,
    `modified_time`  datetime DEFAULT NULL,
    PRIMARY KEY (`grade_id`),
    KEY `CourseID` (`course_id`),
    KEY `StudentID` (`student_id`),
    CONSTRAINT `ParticipationGrade_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `Course` (`course_id`),
    CONSTRAINT `ParticipationGrade_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `Student` (`student_id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ParticipationGrade`
--

LOCK TABLES `ParticipationGrade` WRITE;
/*!40000 ALTER TABLE `ParticipationGrade`
    DISABLE KEYS */;
INSERT INTO `ParticipationGrade`
VALUES ('1', '3137', 'B11023024', 100.00, '2024-11-04', NULL);
/*!40000 ALTER TABLE `ParticipationGrade`
    ENABLE KEYS */;
UNLOCK TABLES;



--
-- Table structure for table `User`
--

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

/*!40103 SET TIME_ZONE = @OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE = @OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT = @OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS = @OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION = @OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES = @OLD_SQL_NOTES */;

-- Dump completed on 2024-12-09 14:07:50
