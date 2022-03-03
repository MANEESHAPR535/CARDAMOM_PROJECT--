/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - cardamom
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`cardamom` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `cardamom`;

/*Table structure for table `auction` */

DROP TABLE IF EXISTS `auction`;

CREATE TABLE `auction` (
  `auction_id` int(11) NOT NULL AUTO_INCREMENT,
  `Stock_id` int(11) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `auction_date` varchar(50) DEFAULT NULL,
  `end_date` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`auction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

/*Data for the table `auction` */

insert  into `auction`(`auction_id`,`Stock_id`,`amount`,`auction_date`,`end_date`,`status`) values (5,8,'120000.0','2022-02-17','2022-02-18','finished'),(6,11,'50000.0','2022-02-18','2022-02-19','finished'),(7,13,'200000.0','2022-02-18','2022-02-19','finished'),(8,14,'170000.0','2022-02-18','2022-02-23','pending');

/*Table structure for table `auctionpayment` */

DROP TABLE IF EXISTS `auctionpayment`;

CREATE TABLE `auctionpayment` (
  `apayment_id` int(11) NOT NULL AUTO_INCREMENT,
  `auction_id` int(11) DEFAULT NULL,
  `amt` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`apayment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `auctionpayment` */

insert  into `auctionpayment`(`apayment_id`,`auction_id`,`amt`,`date`) values (3,5,'120003','2022-02-22 10:14:31');

/*Table structure for table `bid` */

DROP TABLE IF EXISTS `bid`;

CREATE TABLE `bid` (
  `bid_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) DEFAULT NULL,
  `auction_id` int(11) DEFAULT NULL,
  `amt` decimal(18,0) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`bid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4;

/*Data for the table `bid` */

insert  into `bid`(`bid_id`,`User_id`,`auction_id`,`amt`,`date`) values (14,0,7,200000,'2022-02-18'),(13,0,6,50000,'2022-02-18'),(12,6,5,120003,'2022-02-17 22:36:14'),(11,4,5,120002,'2022-02-17 22:30:05'),(10,5,5,120001,'2022-02-17 22:02:14'),(9,0,5,120000,'2022-02-17'),(15,7,7,200001,'2022-02-18 01:25:32'),(16,8,7,200002,'2022-02-18 01:35:03'),(17,7,6,50002,'2022-02-18 09:49:08'),(18,8,6,50010,'2022-02-18 09:50:37'),(19,8,6,50004,'2022-02-18 09:51:29'),(20,0,8,170000,'2022-02-18');

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `Booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `Stock_id` int(11) NOT NULL,
  `User_id` int(11) DEFAULT NULL,
  `Quantity` varchar(100) DEFAULT NULL,
  `Amount` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Booking_id`,`Stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

/*Data for the table `booking` */

insert  into `booking`(`Booking_id`,`Stock_id`,`User_id`,`Quantity`,`Amount`,`Date`) values (6,10,5,'3','2850','2022-02-17'),(7,10,6,'50','47500','2022-02-17'),(8,15,8,'15','15000','2022-02-18'),(9,12,7,'3','3000','2022-02-18'),(10,10,7,'1','950','2022-02-18'),(11,18,8,'1','950','2022-02-19'),(12,10,6,'15','14250','2022-02-22');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `Complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) DEFAULT NULL,
  `Complaint` varchar(100) DEFAULT NULL,
  `Replay` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaint` */

insert  into `complaint`(`Complaint_id`,`User_id`,`Complaint`,`Replay`,`Date`) values (1,4,'good product','thank you for yor comment','2022-02-17'),(2,7,'less sellers ','pending','2022-02-18');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values (1,'admin','admin','admin'),(2,'buyerbuyer','buyerbuyer','user'),(3,'seller1seller1','seller1seller1','seller'),(4,'customer2customer2','customer2customer2','user'),(5,'maneeshapr','maneeshapr','seller'),(6,'arundas','arundaspr','user'),(7,'manju','manju','user'),(8,'joseph','joseph@123','user'),(9,'spicesmart','spicesmart','seller'),(10,'manurk','manu123@manu','seller'),(11,'ridhi','ridhi','user'),(12,'Anagha K','anaghak@1234','seller'),(13,'Abeel V ','abeelv4564@','seller'),(14,'Selvam','selvakumar1234y','seller'),(15,'Usha PR','usha@1234@','user'),(16,'raju PK','Rajupk6758@11','user'),(17,'','','user'),(18,'','','user'),(19,'','','user'),(20,'','','user'),(21,'','','user'),(22,'','','user'),(23,'','','user'),(24,'','','user'),(25,'','','user'),(26,'','','user'),(27,'','','user'),(28,'','','user'),(29,'','','user'),(30,'','','user'),(31,'','','user'),(32,'','','user'),(33,'','','user'),(34,'','','user'),(35,'','','user'),(36,'','','user'),(37,'','','user'),(38,'','','user'),(39,'','','user'),(40,'','','user'),(41,'','','user'),(42,'','','user'),(43,'','','user'),(44,'','','user'),(45,'','','user'),(46,'','','user'),(47,'','','user'),(48,'','','user'),(49,'','','user'),(50,'','','user'),(51,'','','user'),(52,'','','user'),(53,'','','user'),(54,'','','user'),(55,'','','user'),(56,'','','user'),(57,'dsfyyy','df','user'),(58,'szdfs','rr','user'),(59,'szdfs','rr','user'),(60,'tytrh','rrhhhhhh','user'),(61,'tytrh','rrhhhhhh','user'),(62,'tytrh','rrhhhhhh','user'),(63,'tytrh','rrhhhhhh','user'),(64,'hjjjkkk','jjjjjjjj','user');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `Payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `Booking_id` int(11) DEFAULT NULL,
  `Amount` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Data for the table `payment` */

insert  into `payment`(`Payment_id`,`Booking_id`,`Amount`,`Date`) values (4,6,'2850','2022-02-17'),(5,7,'47500','2022-02-17'),(6,8,'15000','2022-02-18'),(7,9,'3000','2022-02-18'),(8,11,'950','2022-02-19'),(9,12,'14250','2022-02-22');

/*Table structure for table `price` */

DROP TABLE IF EXISTS `price`;

CREATE TABLE `price` (
  `Price_id` int(11) NOT NULL AUTO_INCREMENT,
  `Price` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Price_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `price` */

insert  into `price`(`Price_id`,`Price`) values (1,'100'),(2,'1200'),(3,'1000');

/*Table structure for table `quality` */

DROP TABLE IF EXISTS `quality`;

CREATE TABLE `quality` (
  `Quality_id` int(11) NOT NULL AUTO_INCREMENT,
  `Quality` varchar(100) DEFAULT NULL,
  `percent` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Quality_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

/*Data for the table `quality` */

insert  into `quality`(`Quality_id`,`Quality`,`percent`) values (8,'8mm(high)','100'),(9,'7mm(medium)','90'),(10,'6mm(samll)','80'),(11,'7-8mm','85'),(12,'Cardamom Black seed(high)','100');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `Rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `Seller_id` int(11) DEFAULT NULL,
  `User_id` int(11) DEFAULT NULL,
  `Rated` varchar(100) DEFAULT NULL,
  `Date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `rating` */

insert  into `rating`(`Rating_id`,`Seller_id`,`User_id`,`Rated`,`Date`) values (4,4,4,'4','2022-02-17'),(5,4,6,'4','2022-02-17'),(6,7,8,'2','2022-02-18');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `Stock_id` int(11) DEFAULT NULL,
  `amount` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

/*Data for the table `request` */

insert  into `request`(`request_id`,`Stock_id`,`amount`,`status`) values (7,8,'120000.0','finished'),(8,10,'950','For Sell'),(9,11,'50000.0','finished'),(10,12,'1000','For Sell'),(11,13,'200000.0','finished'),(12,14,'170000.0','accept'),(13,17,'pending','pending'),(14,15,'1000','For Sell'),(15,16,'850','For Sell'),(16,18,'950','For Sell');

/*Table structure for table `seller` */

DROP TABLE IF EXISTS `seller`;

CREATE TABLE `seller` (
  `Seller_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `Sellername` varchar(100) DEFAULT NULL,
  `Place` varchar(100) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Seller_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

/*Data for the table `seller` */

insert  into `seller`(`Seller_id`,`login_id`,`Sellername`,`Place`,`Phone`,`Email`,`Address`) values (1,3,'seller','selle','8976543214','seseller1@gamil.com','dfg'),(2,5,'maneesha','idukki','9744598106','maneesha12@gmail.com','pali(h),chemmannar(po),idukki,pin-685554'),(3,9,'spices','mart','8769856478','spicesmart@gmail.com','kerala sepces mart,kallupalam,udumbanchola(po),idukki,pin:685554'),(4,10,'manu','delkhi','7867876789','manu12@gmail.com','spring board,manu bulding,123 street,pin:345654'),(5,12,'Anagha','Malappuram','7867564567','anagha12@gmail.com','mariyath(h),peruthalmanna(po),anjumukk,malappuram(dis)pin:677789'),(6,13,'Abeel','Idukki','7898765677','Abeelv45@gmail.com','cardamom mart,nedumkandam(po),parathodu,idukki(dis),pin:685556'),(7,14,'Selvam','Kattapana','8976785432','Spicekerala@gmail.com','KR estate,kattapana,murugan bulging,idukki(dis),pin:685557');

/*Table structure for table `stock` */

DROP TABLE IF EXISTS `stock`;

CREATE TABLE `stock` (
  `Stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `Quality_id` int(11) DEFAULT NULL,
  `Seller_id` int(11) DEFAULT NULL,
  `Quantity` varchar(100) DEFAULT NULL,
  `sell_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4;

/*Data for the table `stock` */

insert  into `stock`(`Stock_id`,`Quality_id`,`Seller_id`,`Quantity`,`sell_type`) values (7,8,3,'500','Normal Sell'),(8,8,3,'100','Auction'),(9,11,3,'60','Normal Sell'),(10,11,4,'182','Normal Sell'),(11,8,4,'50','Auction'),(12,9,5,'497','Normal Sell'),(13,8,5,'200','Auction'),(14,11,5,'200','Auction'),(15,12,7,'985','Normal Sell'),(16,10,7,'50','Normal Sell'),(17,8,7,'100','Auction'),(18,8,7,'299','Normal Sell');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `Firstname` varchar(100) DEFAULT NULL,
  `Lastname` varchar(100) DEFAULT NULL,
  `Place` varchar(100) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4;

/*Data for the table `user` */

insert  into `user`(`User_id`,`login_id`,`Firstname`,`Lastname`,`Place`,`Phone`,`Email`,`Address`) values (4,7,'manju','rahul','up','8934574567','manjurahul123@gmail.com','kk road,123 bulding,near rp road,up'),(5,8,'joseph','joseph','kolkata','9876546758','joseph1@gmail.com','spices office,ss bulding,kj street,kolkata,pin:678766'),(6,11,'ridhi','rahul','ernakulam','7896756786','ridhirahul@gmail.com','spices office NN buldings,perumbavoor,Ernakulam(dis),pin:678777'),(7,15,'Usha','PR','UP','9526257245','ushausha1@gmail.com','lh bulding,4th floor,mmm(po),UP,pin:566676'),(8,16,'Raju','PK','koyambathoor','9765765432','rajupk56@gmail.com','Pk products,rearNH,koyambathoor,pin:766676'),(9,17,'','','','','',''),(10,18,'','','','','',''),(11,19,'ghjj','','','','',''),(12,20,'ghjj','','','','',''),(13,21,'','','','','',''),(14,22,'set','','','','',''),(15,23,'set','','','','',''),(16,24,'','','','','',''),(17,25,'','','','','',''),(18,26,'','','','','',''),(19,27,'','','','','',''),(20,28,'Hq','','','','',''),(21,29,'Ag','r','','','',''),(22,30,'Hh','gj','','','',''),(23,31,'Hh','gj','','','',''),(24,32,'Rq','sad','','','',''),(25,33,'Rq','sad','','','',''),(26,34,'Ls','dsfs','','sfs','',''),(27,35,'Rg','sfdfg','','','',''),(28,36,'Ag','dff','','','',''),(29,37,'Ag','dff','','','',''),(30,38,'Avb','c','','','',''),(31,39,'Avb','c','','','',''),(32,40,'Aq','gfd','','','',''),(33,41,'Afxdrx','Adsfsr','','44444','',''),(34,42,'Afxdrx','Adsfsr','','44444','',''),(35,43,'Afxdrx','Adsfsr','','44444','',''),(36,44,'Aq','gfd','','','',''),(37,45,'Aq','gfd','','','',''),(38,46,'Aq','gfd','','','',''),(39,47,'Aq','gfd','','','',''),(40,48,'','','','','',''),(41,49,'sdd','','','','',''),(42,50,'sdd','','','','',''),(43,51,'sdd','','','','',''),(44,52,'','','','','',''),(45,53,'','','','','',''),(46,54,'','','','','',''),(47,55,'','','','','',''),(48,56,'','','','','',''),(49,57,'dg','ty','gdffgy','9762345678','a@gmail.com','df'),(50,58,'r','tyyry','sdf','9876543221','a@gmail.com','df'),(51,59,'r','tyyry','sdf','9876543221','a@gmail.com','df'),(52,60,'a','ut','dhf','9876544388','driver@gamil.com','dgg'),(53,61,'a','ut','dhf','9876544388','driver@gamil.com','dgg'),(54,62,'a','ut','dhf','9876544388','driver@gamil.com','dgg'),(55,63,'a','ut','dhf','9876544388','driver@gamil.com','dgg'),(56,64,'d','rty','g','9762345678','a@gmail.com','jj');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
