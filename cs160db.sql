-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: RESMGTDB
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
  `stock` float(10,2) unsigned zerofill NOT NULL,
  `unit` varchar(10) NOT NULL DEFAULT 'piece',
  `cost` float(10,2) unsigned zerofill NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredients`
--

LOCK TABLES `ingredients` WRITE;
/*!40000 ALTER TABLE `ingredients` DISABLE KEYS */;
INSERT INTO `ingredients` VALUES (1,'Hamburger Bun',0000997.00,'piece',0000000.50),(2,'Beef Patty (1/3 Pound)',0000997.00,'piece',0000001.00),(3,'Veggie Patty',0000500.00,'piece',0000001.25),(4,'American Cheese (slice)',0000499.00,'piece',0000000.25),(5,'Cheddar Cheese (slice)',0000500.00,'piece',0000000.25),(6,'Swiss Cheese (slice)',0000500.00,'piece',0000000.25),(7,'Bacon (slice)',0000498.00,'piece',0000000.50),(8,'Lettuce',0000499.50,'oz',0000000.15),(9,'Tomato',0000999.00,'oz',0000000.20),(10,'Onion',0000499.00,'oz',0000000.20),(11,'Pickles',0000748.00,'oz',0000000.25),(12,'Ketchup',0000999.00,'oz',0000000.05),(13,'Mustard',0001000.00,'oz',0000000.05),(14,'Mayo',0001000.00,'oz',0000000.05),(15,'Hot Dog Bun',0000998.00,'piece',0000000.40),(16,'Beef Hot Dog',0000998.00,'piece',0000000.90),(17,'Relish',0000500.00,'oz',0000000.15),(18,'Chicken Strips',0000738.00,'piece',0000001.20),(19,'French Fries',0001936.00,'oz',0000000.40),(20,'Onion Rings',0000742.00,'oz',0000000.50),(21,'Coke',0000996.00,'bottle',0000000.75),(22,'Diet Coke',0000750.00,'bottle',0000000.75),(23,'Root Beer',0000499.00,'bottle',0000000.75),(24,'Sprite',0000497.00,'bottle',0000000.75),(25,'Ground Coffee Roast',0000749.50,'oz',0000000.75),(26,'Sugar',0000749.50,'oz',0000000.02);
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
  `price` float(10,2) unsigned zerofill NOT NULL,
  `category` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Signature Hamburger',0000009.50,'Food'),(2,'Signature Hot Dog',0000007.50,'Food'),(3,'Chicken Strips',0000008.50,'Food'),(4,'Basket of French Fries',0000003.50,'Side'),(5,'Basket of Onion Rings',0000003.50,'Side'),(6,'Coke',0000002.25,'Drink'),(7,'Diet Coke',0000002.25,'Drink'),(8,'Root Beer',0000002.25,'Drink'),(9,'Sprite',0000002.25,'Drink'),(10,'Coffee',0000002.75,'Drink');
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `orderid` varchar(20) NOT NULL,
  `guestname` varchar(256) NOT NULL,
  `mainorder` int(11) NOT NULL,
  `detail` int(11) DEFAULT NULL,
  `quantity` float(10,2) DEFAULT NULL,
  `active` tinyint(4) NOT NULL DEFAULT '0',
  `completed` tinyint(4) NOT NULL DEFAULT '0',
  `order_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=165 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (118,'vcrzrjvfeobhilgklsgy','test2',2,12,0.50,1,0,'2019-07-06 00:00:11'),(119,'vcrzrjvfeobhilgklsgy','test2',2,15,1.00,1,0,'2019-07-06 00:00:11'),(120,'vcrzrjvfeobhilgklsgy','test2',2,16,1.00,1,0,'2019-07-06 00:00:11'),(121,'vcrzrjvfeobhilgklsgy','test2',4,19,8.00,1,0,'2019-07-06 00:00:11'),(122,'vcrzrjvfeobhilgklsgy','test2',8,23,1.00,1,0,'2019-07-06 00:00:11'),(123,'vcrzrjvfeobhilgklsgy','test4',2,12,0.50,1,0,'2019-07-06 00:00:11'),(124,'vcrzrjvfeobhilgklsgy','test4',2,15,1.00,1,0,'2019-07-06 00:00:11'),(125,'vcrzrjvfeobhilgklsgy','test4',2,16,1.00,1,0,'2019-07-06 00:00:11'),(126,'vcrzrjvfeobhilgklsgy','test4',5,20,8.00,1,0,'2019-07-06 00:00:11'),(127,'vcrzrjvfeobhilgklsgy','test4',6,21,1.00,1,0,'2019-07-06 00:00:11'),(128,'xtwezaiwnbrzgikasdlm','test5',3,18,3.00,1,0,'2019-07-06 00:00:11'),(129,'xtwezaiwnbrzgikasdlm','test5',4,19,8.00,1,0,'2019-07-06 00:00:11'),(130,'xtwezaiwnbrzgikasdlm','test5',6,21,1.00,1,0,'2019-07-06 00:00:11'),(131,'zxpqiginxajtkczhknvk','test33',1,10,0.50,1,0,'2019-07-06 00:00:11'),(132,'zxpqiginxajtkczhknvk','test33',1,11,1.00,1,0,'2019-07-06 00:00:11'),(133,'zxpqiginxajtkczhknvk','test33',1,29,0.00,1,0,'2019-07-06 00:00:11'),(134,'zxpqiginxajtkczhknvk','test33',1,1,1.00,1,0,'2019-07-06 00:00:11'),(135,'zxpqiginxajtkczhknvk','test33',1,2,1.00,1,0,'2019-07-06 00:00:11'),(136,'zxpqiginxajtkczhknvk','test33',4,19,8.00,1,0,'2019-07-06 00:00:11'),(137,'zxpqiginxajtkczhknvk','test33',10,25,0.50,1,0,'2019-07-06 00:00:11'),(138,'zxpqiginxajtkczhknvk','test33',10,26,0.50,1,0,'2019-07-06 00:00:11'),(139,'zxpqiginxajtkczhknvk','test34',1,7,2.00,1,0,'2019-07-06 00:00:11'),(140,'zxpqiginxajtkczhknvk','test34',1,11,1.00,1,0,'2019-07-06 00:00:11'),(141,'zxpqiginxajtkczhknvk','test34',1,29,0.00,1,0,'2019-07-06 00:00:11'),(142,'zxpqiginxajtkczhknvk','test34',1,1,1.00,1,0,'2019-07-06 00:00:11'),(143,'zxpqiginxajtkczhknvk','test34',1,2,1.00,1,0,'2019-07-06 00:00:11'),(144,'zxpqiginxajtkczhknvk','test34',4,19,8.00,1,0,'2019-07-06 00:00:11'),(145,'zxpqiginxajtkczhknvk','test34',9,24,1.00,1,0,'2019-07-06 00:00:11'),(146,'pqrnksdhbpqhgqqflgtu','timetester',1,4,1.00,1,0,'2019-07-06 00:01:15'),(147,'pqrnksdhbpqhgqqflgtu','timetester',1,8,0.50,1,0,'2019-07-06 00:01:15'),(148,'pqrnksdhbpqhgqqflgtu','timetester',1,9,1.00,1,0,'2019-07-06 00:01:15'),(149,'pqrnksdhbpqhgqqflgtu','timetester',1,10,0.50,1,0,'2019-07-06 00:01:15'),(150,'pqrnksdhbpqhgqqflgtu','timetester',1,28,0.00,1,0,'2019-07-06 00:01:15'),(151,'pqrnksdhbpqhgqqflgtu','timetester',1,1,1.00,1,0,'2019-07-06 00:01:15'),(152,'pqrnksdhbpqhgqqflgtu','timetester',1,2,1.00,1,0,'2019-07-06 00:01:15'),(153,'pqrnksdhbpqhgqqflgtu','timetester',4,19,8.00,1,0,'2019-07-06 00:01:15'),(154,'pqrnksdhbpqhgqqflgtu','timetester',9,24,1.00,1,0,'2019-07-06 00:01:15'),(155,'aifdrkarfykhmctrdgnp','PST%252BTime%252BTest',2,17,2.00,0,0,'2019-07-06 00:05:24'),(156,'aifdrkarfykhmctrdgnp','PST%252BTime%252BTest',2,12,0.50,0,0,'2019-07-06 00:05:24'),(157,'aifdrkarfykhmctrdgnp','PST%252BTime%252BTest',2,13,0.50,0,0,'2019-07-06 00:05:24'),(158,'aifdrkarfykhmctrdgnp','PST%252BTime%252BTest',2,15,1.00,0,0,'2019-07-06 00:05:24'),(159,'aifdrkarfykhmctrdgnp','PST%252BTime%252BTest',2,16,1.00,0,0,'2019-07-06 00:05:24'),(160,'aifdrkarfykhmctrdgnp','PST%252BTime%252BTest',4,19,8.00,0,0,'2019-07-06 00:05:24'),(161,'aifdrkarfykhmctrdgnp','PST%252BTime%252BTest',9,24,1.00,0,0,'2019-07-06 00:05:24'),(162,'dadplvavxsolphtjxjqu','timetest',3,18,3.00,1,0,'2019-07-06 00:10:20'),(163,'dadplvavxsolphtjxjqu','timetest',4,19,8.00,1,0,'2019-07-06 00:10:20'),(164,'dadplvavxsolphtjxjqu','timetest',9,24,1.00,1,0,'2019-07-06 00:10:20');
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
  `menu_desciption` varchar(256) DEFAULT NULL,
  `ingredient_id` int(11) DEFAULT NULL,
  `ingredient_description` varchar(256) DEFAULT NULL,
  `ingredient_quantity` float(10,2) unsigned zerofill DEFAULT NULL,
  `to_show` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (1,1,'Signature Hamburger',1,'Hamburger Bun',0000001.00,0),(2,1,'Signature Hamburger',2,'Beef Patty (1/3 pound)',0000001.00,0),(4,1,'Signature Hamburger',4,'American Cheese (slice)',0000001.00,1),(5,1,'Signature Hamburger',5,'Cheddar Cheese (slice)',0000001.00,1),(6,1,'Signature Hamburger',6,'Swiss Cheese (slice)',0000001.00,1),(7,1,'Signature Hamburger',7,'Bacon',0000002.00,1),(8,1,'Signature Hamburger',8,'Lettuce',0000000.50,1),(9,1,'Signature Hamburger',9,'Tomato',0000001.00,1),(10,1,'Signature Hamburger',10,'Onion',0000000.50,1),(11,1,'Signature Hamburger',11,'Pickles',0000001.00,1),(12,1,'Signature Hamburger',12,'Ketchup',0000000.50,1),(13,1,'Signature Hamburger',13,'Mustard',0000000.50,1),(14,1,'Signature Hamburger',14,'Mayo',0000000.50,1),(15,2,'Signature Hot Dog',15,'Hot Dog Bun',0000001.00,0),(16,2,'Signature Hot Dog',16,'Beef Hot Dog',0000001.00,0),(17,2,'Signature Hot Dog',17,'Relish',0000002.00,1),(18,2,'Signature Hot Dog',12,'Ketchup',0000000.50,1),(19,2,'Signature Hot Dog',13,'Mustard',0000000.50,1),(20,3,'Chicken Strips',18,'Chicken Strips',0000003.00,1),(21,4,'French Fries',19,'French Fries',0000008.00,1),(22,5,'Onion Rings',20,'Onion Rings',0000008.00,1),(23,6,'Coke',21,'Coke',0000001.00,1),(24,7,'Diet Coke',22,'Diet Coke',0000001.00,1),(25,8,'Root Beer',23,'Root Beer',0000001.00,1),(26,9,'Sprite',24,'Sprite',0000001.00,1),(27,10,'Coffee',25,'Ground Coffee Roast',0000000.50,1),(28,10,'Coffee',26,'Sugar',0000000.50,1),(29,1,'Signature Hamburger',27,'Medium Cooked',0000000.00,1),(30,1,'Signature Hamburger',28,'Well Done Cooked',0000000.00,1),(31,1,'Signature Hamburger',29,'Medium Well Cooked',0000000.00,1);
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `username` varchar(10) NOT NULL,
  `password` varchar(2048) DEFAULT NULL,
  `active` int(1) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
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

-- Dump completed on 2019-07-05 17:29:21
