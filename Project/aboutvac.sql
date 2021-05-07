-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: localhost    Database: aboutvac
-- ------------------------------------------------------
-- Server version	8.0.24

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
-- Table structure for table `aboutvac`
--

DROP TABLE IF EXISTS `aboutvac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aboutvac` (
  `vac_name` varchar(30) DEFAULT NULL,
  `vac_detail` varchar(50) DEFAULT NULL,
  `vac_manufacture_place` varchar(30) DEFAULT NULL,
  `vac_manufacture_date` date DEFAULT NULL,
  `vac_expiry` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aboutvac`
--

LOCK TABLES `aboutvac` WRITE;
/*!40000 ALTER TABLE `aboutvac` DISABLE KEYS */;
INSERT INTO `aboutvac` VALUES ('coronil','bypatanjali','india','2020-01-25','2030-12-30');
/*!40000 ALTER TABLE `aboutvac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eachvacdetail`
--

DROP TABLE IF EXISTS `eachvacdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eachvacdetail` (
  `vac_name` varchar(30) DEFAULT NULL,
  `vac_cities` varchar(50) DEFAULT NULL,
  `vac_startdate` date DEFAULT NULL,
  `vac_enddate` date DEFAULT NULL,
  `vac_quantity` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eachvacdetail`
--

LOCK TABLES `eachvacdetail` WRITE;
/*!40000 ALTER TABLE `eachvacdetail` DISABLE KEYS */;
INSERT INTO `eachvacdetail` VALUES ('coronil','Pune','2021-03-01','2021-03-08',2);
/*!40000 ALTER TABLE `eachvacdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'aboutvac'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-24 15:21:56
