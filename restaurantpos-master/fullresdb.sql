-- MySQL dump 10.16  Distrib 10.1.38-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: RESMGTDB
-- ------------------------------------------------------
-- Server version	10.1.38-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ingredients`
--

DROP TABLE IF EXISTS `ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ingredients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(256) NOT NULL,
  `stock` decimal(10,2) unsigned zerofill NOT NULL,
  `unit` varchar(50) NOT NULL,
  `cost` decimal(10,2) unsigned zerofill NOT NULL,
  `low_threshold` int(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredients`
--

LOCK TABLES `ingredients` WRITE;
/*!40000 ALTER TABLE `ingredients` DISABLE KEYS */;
INSERT INTO `ingredients` VALUES (1,'Hamburger Bun',00000997.00,'piece',00000000.50,100),(2,'Beef Patty (1/3 Pound)',00000997.00,'piece',00000001.00,100),(3,'Veggie Patty',00000500.00,'piece',00000001.25,100),(4,'American Cheese (slice)',00000499.00,'piece',00000000.25,100),(5,'Cheddar Cheese (slice)',00000500.00,'piece',00000000.25,100),(6,'Swiss Cheese (slice)',00000500.00,'piece',00000000.25,100),(7,'Bacon (slice)',00000498.00,'piece',00000000.50,100),(8,'Lettuce',00000499.50,'oz',00000000.15,100),(9,'Tomato',00000999.00,'oz',00000000.20,100),(10,'Onion',00000499.00,'oz',00000000.20,100),(11,'Pickles',00000748.00,'oz',00000000.25,100),(12,'Ketchup',00000999.00,'oz',00000000.05,100),(13,'Mustard',00001000.00,'oz',00000000.05,100),(14,'Mayo',00001000.00,'oz',00000000.05,100),(15,'Hot Dog Bun',00000998.00,'piece',00000000.40,100),(16,'Beef Hot Dog',00000998.00,'piece',00000000.90,100),(17,'Relish',00000500.00,'oz',00000000.15,100),(18,'Chicken Strips',00000738.00,'piece',00000001.20,100),(19,'French Fries',00001936.00,'oz',00000000.40,100),(20,'Onion Rings',00000742.00,'oz',00000000.50,100),(21,'Coke',00000996.00,'bottle',00000000.75,100),(22,'Diet Coke',00000750.00,'bottle',00000000.75,100),(23,'Root Beer',00000098.00,'bottle',00000000.75,100),(24,'Sprite',00000497.00,'bottle',00000000.75,100),(25,'Ground Coffee Roast',00000749.50,'oz',00000000.75,100),(26,'Sugar',00000099.00,'oz',00000000.02,100);
/*!40000 ALTER TABLE `ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(256) DEFAULT NULL,
  `price` decimal(10,2) unsigned zerofill NOT NULL,
  `category` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Signature Hamburger',00000009.50,'Food'),(2,'Signature Hot Dog',00000007.50,'Food'),(3,'Chicken Strips',00000008.50,'Food'),(4,'Basket of French Fries',00000003.50,'Side'),(5,'Basket of Onion Rings',00000003.50,'Side'),(6,'Coke',00000002.25,'Drink'),(7,'Diet Coke',00000002.25,'Drink'),(8,'Root Beer',00000002.25,'Drink'),(9,'Sprite',00000002.25,'Drink'),(10,'Coffee',00000002.75,'Drink');
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ordertime` datetime DEFAULT NULL,
  `orderid` varchar(20) NOT NULL,
  `guestname` varchar(256) NOT NULL,
  `mainorder` int(11) NOT NULL,
  `detail` int(11) DEFAULT NULL,
  `quantity` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'2019-07-30 17:48:56','wynjutgwotxygrggsygv','Jimothy McButts',1,4,1.00),(2,'2019-07-30 17:48:56','wynjutgwotxygrggsygv','Jimothy McButts',1,5,1.00),(3,'2019-07-30 17:48:56','wynjutgwotxygrggsygv','Jimothy McButts',1,6,1.00),(4,'2019-07-30 17:48:56','wynjutgwotxygrggsygv','Jimothy McButts',1,7,2.00),(5,'2019-07-30 17:48:56','wynjutgwotxygrggsygv','Jimothy McButts',1,1,1.00),(6,'2019-07-30 17:48:56','wynjutgwotxygrggsygv','Jimothy McButts',1,2,1.00),(7,'2019-07-30 17:48:56','wynjutgwotxygrggsygv','Jimothy McButts',4,19,8.00),(8,'2019-07-30 17:48:56','wynjutgwotxygrggsygv','Jimothy McButts',6,21,1.00),(9,'2019-07-30 17:43:56','hsdjhgsdsyudsdghsjdh','Jim Mothy McButtes',4,19,8.00),(10,'2019-07-31 16:48:56','ccvbnmcjkvcvhcvjchvc','Jimoth E. Mac Butts',4,19,8.00),(11,'2019-08-02 06:52:50','oiwsehvxwsrkpufpqsbq','Barold Jeffefferfields',6,21,1.00),(12,'2019-08-02 06:53:26','oiwsehvxwsrkpufpqsbq','Barold Jeffefferfields',6,21,1.00),(13,'2019-08-02 06:53:45','oiwsehvxwsrkpufpqsbq','dfhj',2,15,1.00),(14,'2019-08-02 06:53:45','oiwsehvxwsrkpufpqsbq','dfhj',2,16,1.00),(15,'2019-08-02 06:53:46','oiwsehvxwsrkpufpqsbq','dfhj',7,22,1.00),(16,'2019-08-02 06:53:52','oiwsehvxwsrkpufpqsbq','dfhj',2,15,1.00),(17,'2019-08-02 06:53:52','oiwsehvxwsrkpufpqsbq','dfhj',2,16,1.00),(18,'2019-08-02 06:53:52','oiwsehvxwsrkpufpqsbq','dfhj',7,22,1.00),(19,'2019-08-02 16:11:00','bfwmeanskxbnlncpigls','Barold Jeffefferfields',1,1,1.00),(20,'2019-08-02 16:11:00','bfwmeanskxbnlncpigls','Barold Jeffefferfields',1,2,1.00),(21,'2019-08-02 16:11:00','bfwmeanskxbnlncpigls','Barold Jeffefferfields',4,19,8.00),(22,'2019-08-02 16:11:00','bfwmeanskxbnlncpigls','Barold Jeffefferfields',7,22,1.00),(23,'2019-08-02 16:13:34','hnswipityysoristfcoe','Barold Jeffefferfields',5,20,8.00),(24,'2019-08-02 16:13:34','hnswipityysoristfcoe','Barold Jeffefferfields',7,22,1.00),(25,'2019-08-02 16:17:23','hvflnzdluflnxdjsipdg','Barold Jeffefferfields',1,1,1.00),(26,'2019-08-02 16:17:23','hvflnzdluflnxdjsipdg','Barold Jeffefferfields',1,2,1.00),(27,'2019-08-02 16:17:23','hvflnzdluflnxdjsipdg','Barold Jeffefferfields',5,20,8.00),(28,'2019-08-02 16:17:23','hvflnzdluflnxdjsipdg','Barold Jeffefferfields',7,22,1.00),(29,'2019-08-02 16:18:34','iqehhzyrtibksmnjgdan','Barold Jeffefferfields',2,15,1.00),(30,'2019-08-02 16:18:34','iqehhzyrtibksmnjgdan','Barold Jeffefferfields',2,16,1.00),(31,'2019-08-02 16:18:34','iqehhzyrtibksmnjgdan','Barold Jeffefferfields',5,20,8.00),(32,'2019-08-02 16:18:34','iqehhzyrtibksmnjgdan','Barold Jeffefferfields',6,21,1.00),(33,'2019-08-02 16:19:29','amldtbtekbvezplrgywj','test',2,15,1.00),(34,'2019-08-02 16:19:29','amldtbtekbvezplrgywj','test',2,16,1.00),(35,'2019-08-02 16:19:29','amldtbtekbvezplrgywj','test',4,19,8.00),(36,'2019-08-02 16:19:29','amldtbtekbvezplrgywj','test',7,22,1.00),(37,'2019-08-02 16:54:10','guxffnoofokvrlirgqvf','Baron Joffhefferfelder',4,19,8.00),(38,'2019-08-02 16:54:10','guxffnoofokvrlirgqvf','Baron Joffhefferfelder',9,24,1.00),(39,'2019-08-02 17:03:00','secoovocxlprjbrtnrsv','nnnnnno',2,15,1.00),(40,'2019-08-02 17:03:00','secoovocxlprjbrtnrsv','nnnnnno',2,16,1.00),(41,'2019-08-02 17:03:00','secoovocxlprjbrtnrsv','nnnnnno',5,20,8.00),(42,'2019-08-02 17:03:00','secoovocxlprjbrtnrsv','nnnnnno',6,21,1.00),(43,'2019-08-02 17:17:45','bidrldafqwpzsqmskaid','confused',1,1,1.00),(44,'2019-08-02 17:17:45','bidrldafqwpzsqmskaid','confused',1,2,1.00),(45,'2019-08-02 17:17:45','bidrldafqwpzsqmskaid','confused',4,19,8.00),(46,'2019-08-02 17:17:45','bidrldafqwpzsqmskaid','confused',8,23,1.00),(47,'2019-08-02 17:35:38','myrutrzjpoyglehcfymu','adfdds',2,15,1.00),(48,'2019-08-02 17:35:38','myrutrzjpoyglehcfymu','adfdds',2,16,1.00),(49,'2019-08-02 17:35:38','myrutrzjpoyglehcfymu','adfdds',5,20,8.00),(50,'2019-08-02 17:35:38','myrutrzjpoyglehcfymu','adfdds',10,25,0.50),(51,'2019-08-02 17:35:39','myrutrzjpoyglehcfymu','adfdds',10,26,0.50),(52,'2019-08-02 17:40:24','skkcxuuolsjmapyshmdx','dfs',2,15,1.00),(53,'2019-08-02 17:40:24','skkcxuuolsjmapyshmdx','dfs',2,16,1.00),(54,'2019-08-02 17:40:24','skkcxuuolsjmapyshmdx','dfs',4,19,8.00),(55,'2019-08-02 17:40:25','skkcxuuolsjmapyshmdx','dfs',6,21,1.00),(56,'2019-08-02 17:42:44','icsdepyjiuqsqmyxdjyw','eyyyyy',2,15,1.00),(57,'2019-08-02 17:42:44','icsdepyjiuqsqmyxdjyw','eyyyyy',2,16,1.00),(58,'2019-08-02 17:42:44','icsdepyjiuqsqmyxdjyw','eyyyyy',4,19,8.00),(59,'2019-08-02 17:42:44','icsdepyjiuqsqmyxdjyw','eyyyyy',7,22,1.00);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recipes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_id` int(11) DEFAULT NULL,
  `menu_description` varchar(256) DEFAULT NULL,
  `ingredient_id` int(11) DEFAULT NULL,
  `ingredient_description` varchar(256) DEFAULT NULL,
  `ingredient_quantity` decimal(10,2) unsigned zerofill DEFAULT NULL,
  `to_show` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (1,1,'Signature Hamburger',1,'Hamburger Bun',00000001.00,0),(2,1,'Signature Hamburger',2,'Beef Patty (1/3 pound)',00000001.00,0),(4,1,'Signature Hamburger',4,'American Cheese (slice)',00000001.00,1),(5,1,'Signature Hamburger',5,'Cheddar Cheese (slice)',00000001.00,1),(6,1,'Signature Hamburger',6,'Swiss Cheese (slice)',00000001.00,1),(7,1,'Signature Hamburger',7,'Bacon',00000002.00,1),(8,1,'Signature Hamburger',8,'Lettuce',00000000.50,1),(9,1,'Signature Hamburger',9,'Tomato',00000001.00,1),(10,1,'Signature Hamburger',10,'Onion',00000000.50,1),(11,1,'Signature Hamburger',11,'Pickles',00000001.00,1),(12,1,'Signature Hamburger',12,'Ketchup',00000000.50,1),(13,1,'Signature Hamburger',13,'Mustard',00000000.50,1),(14,1,'Signature Hamburger',14,'Mayo',00000000.50,1),(15,2,'Signature Hot Dog',15,'Hot Dog Bun',00000001.00,0),(16,2,'Signature Hot Dog',16,'Beef Hot Dog',00000001.00,0),(17,2,'Signature Hot Dog',17,'Relish',00000002.00,1),(18,2,'Signature Hot Dog',12,'Ketchup',00000000.50,1),(19,2,'Signature Hot Dog',13,'Mustard',00000000.50,1),(20,3,'Chicken Strips',18,'Chicken Strips',00000003.00,1),(21,4,'French Fries',19,'French Fries',00000008.00,1),(22,5,'Onion Rings',20,'Onion Rings',00000008.00,1),(23,6,'Coke',21,'Coke',00000001.00,1),(24,7,'Diet Coke',22,'Diet Coke',00000001.00,1),(25,8,'Root Beer',23,'Root Beer',00000001.00,1),(26,9,'Sprite',24,'Sprite',00000001.00,1),(27,10,'Coffee',25,'Ground Coffee Roast',00000000.50,1),(28,10,'Coffee',26,'Sugar',00000000.50,1),(29,1,'Signature Hamburger',27,'Medium Cooked',00000000.00,1),(30,1,'Signature Hamburger',28,'Well Done Cooked',00000000.00,1),(31,1,'Signature Hamburger',29,'Medium Well Cooked',00000000.00,1);
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(10) NOT NULL,
  `password` varchar(2048) DEFAULT NULL,
  `isadmin` tinyint(4) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (3,'manager','$2b$12$K8aSU.CPHEKOUt1r9hj5cu4Six5ihuhDK0zqXSEswHaE2iwO9EWBq',1),(8,'subman1','$2b$12$4XlJW7muSrHpxt2txz47huMISS54MxlPprVZ8svJH7gbeFnBMp22W',0),(9,'subman2','$2b$12$AKCBFKCzqcPwy2YGBIfn/OsXBRl7ekeLOXEGjWo4gnitaJiP7vUQy',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-02 17:46:32
