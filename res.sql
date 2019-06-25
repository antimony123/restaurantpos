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
INSERT INTO `ingredients` VALUES (1,'Hamburger Bun',0001000.00,'piece',0000000.50),(2,'Beef Patty (1/3 Pound)',0001000.00,'piece',0000001.00),(3,'Veggie Patty',0000500.00,'piece',0000001.25),(4,'American Cheese (slice)',0000500.00,'piece',0000000.25),(5,'Cheddar Cheese (slice)',0000500.00,'piece',0000000.25),(6,'Swiss Cheese (slice)',0000500.00,'piece',0000000.25),(7,'Bacon (slice)',0000500.00,'piece',0000000.50),(8,'Lettuce',0000500.00,'oz',0000000.15),(9,'Tomato',0001000.00,'oz',0000000.20),(10,'Onion',0000500.00,'oz',0000000.20),(11,'Pickles',0000750.00,'oz',0000000.25),(12,'Ketchup',0001000.00,'oz',0000000.05),(13,'Mustard',0001000.00,'oz',0000000.05),(14,'Mayo',0001000.00,'oz',0000000.05),(15,'Hot Dog Bun',0001000.00,'piece',0000000.40),(16,'Beef Hot Dog',0001000.00,'piece',0000000.90),(17,'Relish',0000500.00,'oz',0000000.15),(18,'Chicken Strips',0000750.00,'piece',0000001.20),(19,'French Fries',0002000.00,'oz',0000000.40),(20,'Onion Rings',0000750.00,'oz',0000000.50),(21,'Coke',0001000.00,'bottle',0000000.75),(22,'Diet Coke',0000750.00,'bottle',0000000.75),(23,'Root Beer',0000500.00,'bottle',0000000.75),(24,'Sprite',0000500.00,'bottle',0000000.75),(25,'Ground Coffee Roast',0000750.00,'oz',0000000.75),(26,'Sugar',0000750.00,'oz',0000000.02);
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
-- Table structure for table `order_details`
--

DROP TABLE IF EXISTS `order_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `menu_id` int(11) NOT NULL,
  `item_price` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_details`
--

LOCK TABLES `order_details` WRITE;
/*!40000 ALTER TABLE `order_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_temp`
--

DROP TABLE IF EXISTS `order_temp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_temp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `guestname` varchar(256) NOT NULL,
  `orderid` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_temp`
--

LOCK TABLES `order_temp` WRITE;
/*!40000 ALTER TABLE `order_temp` DISABLE KEYS */;
INSERT INTO `order_temp` VALUES (23,'eliasd','ykqboefrlurtyjgpdvmy'),(24,'testname','vdsjpkohifhzfanlxupi'),(25,'testname','vdsjpkohifhzfanlxupi'),(26,'testname','vdsjpkohifhzfanlxupi'),(27,'testname','vdsjpkohifhzfanlxupi'),(28,'vassilios','jemauqojizbwjgublecd'),(29,'fotisd','pyzhfkzllmysiyulhejq'),(30,'TesterUno','vzwhsjdgnhoffxpsjbhu'),(31,'debra','oclhsogcppyskuikpudy'),(32,'butts+mcgee','ofkzhvllucwsnnoacejo'),(33,'Sean','plhttwnsbhifoqtvfqnf'),(34,'%27%3B+OR+1%3D%3D1','kmnohbpqyiqzduzurxiv'),(35,'%29%3B+SHOW+TABLES%3B','bzllotivxmqxncccoseh'),(36,'poopy','bcojcdkuvqtipbothvsr'),(37,'yes','mmjoyuujwaofcsoeqkre'),(38,'yes','mmjoyuujwaofcsoeqkre'),(39,'mainorder%3D2','atzmwozrmqplnflycddp');
/*!40000 ALTER TABLE `order_temp` ENABLE KEYS */;
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
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

-- Dump completed on 2019-06-25  0:29:20
