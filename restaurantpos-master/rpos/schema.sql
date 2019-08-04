DROP TABLE IF EXISTS `ingredients`;
DROP TABLE IF EXISTS `menu`;
DROP TABLE IF EXISTS `orders`;
DROP TABLE IF EXISTS `recipes`;
DROP TABLE IF EXISTS `users`;

CREATE TABLE `ingredients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(256) NOT NULL,
  `stock` float(10,2) unsigned zerofill NOT NULL,
  `unit` varchar(10) NOT NULL DEFAULT 'piece',
  `cost` float(10,2) unsigned zerofill NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE `menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(256) DEFAULT NULL,
  `price` float(10,2) unsigned zerofill NOT NULL,
  `category` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE `recipes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_id` int(11) DEFAULT NULL,
  `menu_desciption` varchar(256) DEFAULT NULL,
  `ingredient_id` int(11) DEFAULT NULL,
  `ingredient_description` varchar(256) DEFAULT NULL,
  `ingredient_quantity` float(10,2) unsigned zerofill DEFAULT NULL,
  `to_show` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE `users` (
  `username` varchar(10) NOT NULL,
  `password` varchar(2048) DEFAULT NULL,
  `active` int(1) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB;

--
-- WIP
--

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
) ENGINE=InnoDB;
