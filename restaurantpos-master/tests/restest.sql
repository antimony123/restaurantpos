--
-- Dumping data for table `ingredients`
--

LOCK TABLES `ingredients` WRITE;
INSERT INTO `ingredients` 
VALUES 
  (1,'Hamburger Bun',0000997.00,'piece',0000000.50, 100),
  (2,'Beef Patty (1/3 Pound)',0000997.00,'piece',0000001.00, 100),
  (3,'Veggie Patty',0000500.00,'piece',0000001.25, 100),
  (4,'American Cheese (slice)',0000499.00,'piece',0000000.25, 100),
  (5,'Cheddar Cheese (slice)',0000500.00,'piece',0000000.25, 100),
  (6,'Swiss Cheese (slice)',0000500.00,'piece',0000000.25, 100),
  (7,'Bacon (slice)',0000498.00,'piece',0000000.50, 100),
  (8,'Lettuce',0000499.50,'oz',0000000.15, 100),
  (9,'Tomato',0000999.00,'oz',0000000.20, 100),
  (10,'Onion',0000499.00,'oz',0000000.20, 100),
  (11,'Pickles',0000748.00,'oz',0000000.25, 100),
  (12,'Ketchup',0000999.00,'oz',0000000.05, 100),
  (13,'Mustard',0001000.00,'oz',0000000.05, 100),
  (14,'Mayo',0001000.00,'oz',0000000.05, 100),
  (15,'Hot Dog Bun',0000998.00,'piece',0000000.40, 100),
  (16,'Beef Hot Dog',0000998.00,'piece',0000000.90, 100),
  (17,'Relish',0000500.00,'oz',0000000.15, 100),
  (18,'Chicken Strips',0000738.00,'piece',0000001.20, 100),
  (19,'French Fries',0001936.00,'oz',0000000.40, 100),
  (20,'Onion Rings',0000742.00,'oz',0000000.50, 100),
  (21,'Coke',0000996.00,'bottle',0000000.75, 100),
  (22,'Diet Coke',0000750.00,'bottle',0000000.75, 100),
  (23,'Root Beer',0000499.00,'bottle',0000000.75, 100),
  (24,'Sprite',0000497.00,'bottle',0000000.75, 100),
  (25,'Ground Coffee Roast',0000749.50,'oz',0000000.75, 100),
  (26,'Sugar',0000749.50,'oz',0000000.02, 100);
UNLOCK TABLES;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
INSERT INTO `menu` 
VALUES 
  (1,'Signature Hamburger',0000009.50,'Food'),
  (2,'Signature Hot Dog',0000007.50,'Food'),
  (3,'Chicken Strips',0000008.50,'Food'),
  (4,'Basket of French Fries',0000003.50,'Side'),
  (5,'Basket of Onion Rings',0000003.50,'Side'),
  (6,'Coke',0000002.25,'Drink'),
  (7,'Diet Coke',0000002.25,'Drink'),
  (8,'Root Beer',0000002.25,'Drink'),
  (9,'Sprite',0000002.25,'Drink'),
  (10,'Coffee',0000002.75,'Drink');
UNLOCK TABLES;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
INSERT INTO `recipes` VALUES 
  (1,1,'Signature Hamburger',1,'Hamburger Bun',0000001.00,0),
  (2,1,'Signature Hamburger',2,'Beef Patty (1/3 pound)',0000001.00,0),
  (4,1,'Signature Hamburger',4,'American Cheese (slice)',0000001.00,1),
  (5,1,'Signature Hamburger',5,'Cheddar Cheese (slice)',0000001.00,1),
  (6,1,'Signature Hamburger',6,'Swiss Cheese (slice)',0000001.00,1),
  (7,1,'Signature Hamburger',7,'Bacon',0000002.00,1),
  (8,1,'Signature Hamburger',8,'Lettuce',0000000.50,1),
  (9,1,'Signature Hamburger',9,'Tomato',0000001.00,1),
  (10,1,'Signature Hamburger',10,'Onion',0000000.50,1),
  (11,1,'Signature Hamburger',11,'Pickles',0000001.00,1),
  (12,1,'Signature Hamburger',12,'Ketchup',0000000.50,1),
  (13,1,'Signature Hamburger',13,'Mustard',0000000.50,1),
  (14,1,'Signature Hamburger',14,'Mayo',0000000.50,1),
  (15,2,'Signature Hot Dog',15,'Hot Dog Bun',0000001.00,0),
  (16,2,'Signature Hot Dog',16,'Beef Hot Dog',0000001.00,0),
  (17,2,'Signature Hot Dog',17,'Relish',0000002.00,1),
  (18,2,'Signature Hot Dog',12,'Ketchup',0000000.50,1),
  (19,2,'Signature Hot Dog',13,'Mustard',0000000.50,1),
  (20,3,'Chicken Strips',18,'Chicken Strips',0000003.00,1),
  (21,4,'French Fries',19,'French Fries',0000008.00,1),
  (22,5,'Onion Rings',20,'Onion Rings',0000008.00,1),
  (23,6,'Coke',21,'Coke',0000001.00,1),
  (24,7,'Diet Coke',22,'Diet Coke',0000001.00,1),
  (25,8,'Root Beer',23,'Root Beer',0000001.00,1),
  (26,9,'Sprite',24,'Sprite',0000001.00,1),
  (27,10,'Coffee',25,'Ground Coffee Roast',0000000.50,1),
  (28,10,'Coffee',26,'Sugar',0000000.50,1),
  (29,1,'Signature Hamburger',27,'Medium Cooked',0000000.00,1),
  (30,1,'Signature Hamburger',28,'Well Done Cooked',0000000.00,1),
  (31,1,'Signature Hamburger',29,'Medium Well Cooked',0000000.00,1);
UNLOCK TABLES;

LOCK TABLES `orders` WRITE;
INSERT INTO `orders` VALUES
  (1, '2019-07-30 17:48:56', 'wynjutgwotxygrggsygv', 'Jimothy McButts', 1,  4,1),
  (2, '2019-07-30 17:48:56', 'wynjutgwotxygrggsygv', 'Jimothy McButts', 1,  5,1),
  (3, '2019-07-30 17:48:56', 'wynjutgwotxygrggsygv', 'Jimothy McButts', 1,  6,1),
  (4, '2019-07-30 17:48:56', 'wynjutgwotxygrggsygv', 'Jimothy McButts', 1,  7,2),
  (5, '2019-07-30 17:48:56', 'wynjutgwotxygrggsygv', 'Jimothy McButts', 1,  1,1),
  (6, '2019-07-30 17:48:56', 'wynjutgwotxygrggsygv', 'Jimothy McButts', 1,  2,1),
  (7, '2019-07-30 17:48:56', 'wynjutgwotxygrggsygv', 'Jimothy McButts', 4, 19,8),
  (8, '2019-07-30 17:48:56', 'wynjutgwotxygrggsygv', 'Jimothy McButts', 6, 21,1)
  (9, '2019-07-30 17:43:56', 'hsdjhgsdsyudsdghsjdh', 'Jim Mothy McButtes', 4, 19,8),
  (10, '2019-07-31 16:48:56', 'ccvbnmcjkvcvhcvjchvc', 'Jimoth E. Mac Butts', 4, 19,8);
UNLOCK TABLE;