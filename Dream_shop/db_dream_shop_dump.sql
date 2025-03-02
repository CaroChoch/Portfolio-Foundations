-- MySQL dump 10.13  Distrib 9.2.0, for macos15.2 (arm64)
--
-- Host: localhost    Database: db_dream_shop
-- ------------------------------------------------------
-- Server version	9.2.0

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
-- Table structure for table `accounts_account`
--

DROP TABLE IF EXISTS `accounts_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_account` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `civility` varchar(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `postal_code` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `city` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `country` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone_number` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `birth_date` date NOT NULL,
  `username` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superadmin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_account`
--

LOCK TABLES `accounts_account` WRITE;
/*!40000 ALTER TABLE `accounts_account` DISABLE KEYS */;
INSERT INTO `accounts_account` VALUES (1,'pbkdf2_sha256$600000$TWEQDMAxJOYm6rbHqT7QK7$26jMutvbdiPm5wV7nvcYwHZg6SjVAGiW+1Kj8dWGWwM=','','Mathieu','Morel','','00000','','','mormth@aol.com','','2025-03-02','Gabana','2025-03-02 15:57:10.260100','2025-03-02 15:57:38.431344',1,1,1,1);
/*!40000 ALTER TABLE `accounts_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add category',6,'add_category'),(22,'Can change category',6,'change_category'),(23,'Can delete category',6,'delete_category'),(24,'Can view category',6,'view_category'),(25,'Can add account',7,'add_account'),(26,'Can change account',7,'change_account'),(27,'Can delete account',7,'delete_account'),(28,'Can view account',7,'view_account'),(29,'Can add product',8,'add_product'),(30,'Can change product',8,'change_product'),(31,'Can delete product',8,'delete_product'),(32,'Can view product',8,'view_product'),(33,'Can add variation',9,'add_variation'),(34,'Can change variation',9,'change_variation'),(35,'Can delete variation',9,'delete_variation'),(36,'Can view variation',9,'view_variation'),(37,'Can add cart',10,'add_cart'),(38,'Can change cart',10,'change_cart'),(39,'Can delete cart',10,'delete_cart'),(40,'Can view cart',10,'view_cart'),(41,'Can add cart item',11,'add_cartitem'),(42,'Can change cart item',11,'change_cartitem'),(43,'Can delete cart item',11,'delete_cartitem'),(44,'Can view cart item',11,'view_cartitem');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carts_cart`
--

DROP TABLE IF EXISTS `carts_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carts_cart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cart_id` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_added` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carts_cart`
--

LOCK TABLES `carts_cart` WRITE;
/*!40000 ALTER TABLE `carts_cart` DISABLE KEYS */;
INSERT INTO `carts_cart` VALUES (2,'f4x1qkb12ydaw37ve1h53h2a353sq7i3','2025-03-02');
/*!40000 ALTER TABLE `carts_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carts_cartitem`
--

DROP TABLE IF EXISTS `carts_cartitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carts_cartitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `cart_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `carts_cartitem_cart_id_9cb0a756_fk_carts_cart_id` (`cart_id`),
  KEY `carts_cartitem_product_id_acd010e4_fk_store_product_id` (`product_id`),
  CONSTRAINT `carts_cartitem_cart_id_9cb0a756_fk_carts_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `carts_cart` (`id`),
  CONSTRAINT `carts_cartitem_product_id_acd010e4_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carts_cartitem`
--

LOCK TABLES `carts_cartitem` WRITE;
/*!40000 ALTER TABLE `carts_cartitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `carts_cartitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carts_cartitem_variations`
--

DROP TABLE IF EXISTS `carts_cartitem_variations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carts_cartitem_variations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cartitem_id` bigint NOT NULL,
  `variation_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `carts_cartitem_variations_cartitem_id_variation_id_5f8efaf5_uniq` (`cartitem_id`,`variation_id`),
  KEY `carts_cartitem_varia_variation_id_ef9f9ee3_fk_store_var` (`variation_id`),
  CONSTRAINT `carts_cartitem_varia_cartitem_id_8be23372_fk_carts_car` FOREIGN KEY (`cartitem_id`) REFERENCES `carts_cartitem` (`id`),
  CONSTRAINT `carts_cartitem_varia_variation_id_ef9f9ee3_fk_store_var` FOREIGN KEY (`variation_id`) REFERENCES `store_variation` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carts_cartitem_variations`
--

LOCK TABLES `carts_cartitem_variations` WRITE;
/*!40000 ALTER TABLE `carts_cartitem_variations` DISABLE KEYS */;
/*!40000 ALTER TABLE `carts_cartitem_variations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category_category`
--

DROP TABLE IF EXISTS `category_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category_online` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `cat_image` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `gender` varchar(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_type` varchar(1) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `category_name` (`category_name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category_category`
--

LOCK TABLES `category_category` WRITE;
/*!40000 ALTER TABLE `category_category` DISABLE KEYS */;
INSERT INTO `category_category` VALUES (1,'Tops & T-shirts Femmes','Tops & T-shirts','tops-t-shirts-femmes','','','F','B'),(2,'Robes Femmes','Robes','robes-femmes','','','F','B'),(3,'Jeans & Pantalons Femmes','Jeans & Pantalons','jeans-pantalons-femmes','','','F','B'),(4,'Ceintures Femmes','Ceintures','ceintures-femmes','','','F','X'),(5,'Chaussures Femmes','Chaussures','chaussures-femmes','','','F','X'),(6,'Vestes & Manteaux Femmes','Vestes & Manteaux','vestes-manteaux-femmes','','','F','B'),(7,'Écharpes & Foulards Femmes','Écharpes & Foulards','echarpes-foulards-femmes','','','F','X'),(8,'T-shirts & Polos Hommes','T-shirts & Polos','t-shirts-polos-hommes','','','H','A'),(9,'Jeans & Pantalons Hommes','Jeans & Pantalons','jeans-pantalons-hommes','','','H','A'),(10,'Chemises Hommes','Chemises','chemises-hommes','','','H','A'),(11,'Ceintures Hommes','Ceintures','ceintures-hommes','','','H','Y'),(12,'Lunettes de soleil Hommes','Lunettes de soleil','lunettes-de-soleil-hommes','','','H','Y');
/*!40000 ALTER TABLE `category_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_account_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_account_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_account` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2025-03-02 16:06:00.685360','1','Tops & T-shirts',1,'[{\"added\": {}}]',6,1),(2,'2025-03-02 16:06:31.973555','2','Robes',1,'[{\"added\": {}}]',6,1),(3,'2025-03-02 16:06:54.420671','3','Jeans & Pantalons',1,'[{\"added\": {}}]',6,1),(4,'2025-03-02 16:07:18.826230','4','Ceintures',1,'[{\"added\": {}}]',6,1),(5,'2025-03-02 16:08:02.807601','5','Chaussures',1,'[{\"added\": {}}]',6,1),(6,'2025-03-02 16:08:41.130586','6','Vestes & Manteaux',1,'[{\"added\": {}}]',6,1),(7,'2025-03-02 16:09:02.522350','7','Écharpes & Foulards',1,'[{\"added\": {}}]',6,1),(8,'2025-03-02 16:09:34.043043','8','T-shirts & Polos',1,'[{\"added\": {}}]',6,1),(9,'2025-03-02 16:10:54.773595','9','Jeans',1,'[{\"added\": {}}]',6,1),(10,'2025-03-02 16:11:15.236490','10','Chemises',1,'[{\"added\": {}}]',6,1),(11,'2025-03-02 16:11:38.649461','11','Ceintures-homme',1,'[{\"added\": {}}]',6,1),(12,'2025-03-02 16:12:21.217741','9','Jeans & Pantalons Homme',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Category online\", \"Slug\"]}}]',6,1),(13,'2025-03-02 16:12:37.499031','12','Lunettes de soleil',1,'[{\"added\": {}}]',6,1),(14,'2025-03-02 16:20:55.716433','1','Robe Évasée Bohème',1,'[{\"added\": {}}]',8,1),(15,'2025-03-02 16:22:38.615637','12','Lunettes de soleil homme',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(16,'2025-03-02 16:22:54.836854','10','Chemises homme',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(17,'2025-03-02 16:22:59.880915','9','Jeans & Pantalons Homme',2,'[]',6,1),(18,'2025-03-02 16:23:11.533808','8','T-shirts & Polos homme',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(19,'2025-03-02 16:23:22.703376','7','Écharpes & Foulards Femme',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(20,'2025-03-02 16:23:32.968599','6','Vestes & Manteaux Femme',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(21,'2025-03-02 16:23:51.820977','5','Chaussures Femme',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(22,'2025-03-02 16:24:13.103008','4','Ceintures Femmes',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(23,'2025-03-02 16:24:21.331200','12','Lunettes de soleil Hommes',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(24,'2025-03-02 16:24:31.151777','11','Ceintures Hommes',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(25,'2025-03-02 16:24:41.387831','10','Chemises Hommes',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(26,'2025-03-02 16:24:54.497046','9','Jeans & Pantalons Hommes',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(27,'2025-03-02 16:25:04.852792','8','T-shirts & Polos Hommes',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(28,'2025-03-02 16:25:12.950392','7','Écharpes & Foulards Femmes',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(29,'2025-03-02 16:25:20.478561','6','Vestes & Manteaux Femmes',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(30,'2025-03-02 16:25:26.224495','5','Chaussures Femmes',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(31,'2025-03-02 16:25:37.485472','3','Jeans & Pantalons Femmes',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(32,'2025-03-02 16:25:45.884965','2','Robes Femmes',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(33,'2025-03-02 16:25:55.572990','1','Tops & T-shirts Femmes',2,'[{\"changed\": {\"fields\": [\"Category name\", \"Slug\"]}}]',6,1),(34,'2025-03-02 16:30:14.215828','1','Corail',1,'[{\"added\": {}}]',9,1),(35,'2025-03-02 16:30:26.895438','2','Vert',1,'[{\"added\": {}}]',9,1),(36,'2025-03-02 16:30:41.877674','3','S',1,'[{\"added\": {}}]',9,1),(37,'2025-03-02 16:31:48.782283','4','L',1,'[{\"added\": {}}]',9,1),(38,'2025-03-02 16:31:58.177359','5','XL',1,'[{\"added\": {}}]',9,1),(39,'2025-03-02 16:32:09.564218','1','f4x1qkb12ydaw37ve1h53h2a353sq7i3',3,'',10,1),(40,'2025-03-02 16:34:46.193255','2','Robe Bohème Fleurie',1,'[{\"added\": {}}]',8,1),(41,'2025-03-02 16:35:06.927647','6','L',1,'[{\"added\": {}}]',9,1),(42,'2025-03-02 16:35:15.380483','7','XL',1,'[{\"added\": {}}]',9,1),(43,'2025-03-02 16:35:29.142095','8','Unique',1,'[{\"added\": {}}]',9,1),(44,'2025-03-02 16:38:27.026872','3','Foulard Imprimé Bohème',1,'[{\"added\": {}}]',8,1),(45,'2025-03-02 16:38:43.512244','9','Unique',1,'[{\"added\": {}}]',9,1),(46,'2025-03-02 16:38:52.296539','10','Unique',1,'[{\"added\": {}}]',9,1),(47,'2025-03-02 16:41:59.652015','4','Sneakers Compensées Bohème',1,'[{\"added\": {}}]',8,1),(48,'2025-03-02 16:42:30.743481','11','Camel',1,'[{\"added\": {}}]',9,1),(49,'2025-03-02 16:42:50.760364','12','Rose',1,'[{\"added\": {}}]',9,1),(50,'2025-03-02 16:43:03.218444','13','36',1,'[{\"added\": {}}]',9,1),(51,'2025-03-02 16:43:11.786481','14','38',1,'[{\"added\": {}}]',9,1),(52,'2025-03-02 16:46:15.020847','5','CEINTURE FEMME EN CUIR NOIR',1,'[{\"added\": {}}]',8,1),(53,'2025-03-02 16:46:48.822481','5','CEINTURE FEMME EN CUIR NOIR',2,'[{\"changed\": {\"fields\": [\"Title online\"]}}]',8,1),(54,'2025-03-02 16:47:04.008843','15','40',1,'[{\"added\": {}}]',9,1),(55,'2025-03-02 16:47:12.581020','16','Noir',1,'[{\"added\": {}}]',9,1),(56,'2025-03-02 16:48:30.436854','4','Sneakers Compensées Bohème',2,'[{\"changed\": {\"fields\": [\"Description\"]}}]',8,1),(57,'2025-03-02 16:52:16.492341','6','T-shirt côtelé à encolure dégagée',1,'[{\"added\": {}}]',8,1),(58,'2025-03-02 16:53:06.053387','17','Bleu',1,'[{\"added\": {}}]',9,1),(59,'2025-03-02 16:53:15.511298','18','Vert',1,'[{\"added\": {}}]',9,1),(60,'2025-03-02 16:53:25.944992','19','Beige',1,'[{\"added\": {}}]',9,1),(61,'2025-03-02 16:53:36.371201','20','M',1,'[{\"added\": {}}]',9,1),(62,'2025-03-02 16:53:45.898345','21','L',1,'[{\"added\": {}}]',9,1),(63,'2025-03-02 16:53:53.212429','22','S',1,'[{\"added\": {}}]',9,1),(64,'2025-03-02 16:58:34.904530','7','Jeans à jambes larges',1,'[{\"added\": {}}]',8,1),(65,'2025-03-02 17:03:12.423653','23','Bleu',1,'[{\"added\": {}}]',9,1),(66,'2025-03-02 17:03:32.795341','24','W25 / L32',1,'[{\"added\": {}}]',9,1),(67,'2025-03-02 17:03:52.025483','25','W26 / L30',1,'[{\"added\": {}}]',9,1),(68,'2025-03-02 17:08:15.218276','8','Veste de costume',1,'[{\"added\": {}}]',8,1),(69,'2025-03-02 17:08:47.702324','26','Bleu Night Sky',1,'[{\"added\": {}}]',9,1),(70,'2025-03-02 17:09:00.907444','27','34',1,'[{\"added\": {}}]',9,1),(71,'2025-03-02 17:09:09.926576','28','36',1,'[{\"added\": {}}]',9,1),(72,'2025-03-02 17:09:18.180940','29','38',1,'[{\"added\": {}}]',9,1),(73,'2025-03-02 17:15:00.055156','9','Polo Homme',1,'[{\"added\": {}}]',8,1),(74,'2025-03-02 17:15:12.556169','30','Vert',1,'[{\"added\": {}}]',9,1),(75,'2025-03-02 17:15:22.841527','31','Bleu',1,'[{\"added\": {}}]',9,1),(76,'2025-03-02 17:15:33.992084','32','M',1,'[{\"added\": {}}]',9,1),(77,'2025-03-02 17:15:41.166309','33','L',1,'[{\"added\": {}}]',9,1),(78,'2025-03-02 17:18:44.187934','10','Jean Relaxed Fit',1,'[{\"added\": {}}]',8,1),(79,'2025-03-02 17:19:13.251031','34','Bleu',1,'[{\"added\": {}}]',9,1),(80,'2025-03-02 17:19:25.867396','35','S',1,'[{\"added\": {}}]',9,1),(81,'2025-03-02 17:19:33.002095','36','L',1,'[{\"added\": {}}]',9,1),(82,'2025-03-02 17:26:25.302122','11','CHEMISE HOMME',1,'[{\"added\": {}}]',8,1),(83,'2025-03-02 17:26:36.340261','37','Noir',1,'[{\"added\": {}}]',9,1),(84,'2025-03-02 17:26:50.169151','38','L',1,'[{\"added\": {}}]',9,1),(85,'2025-03-02 17:26:59.804759','39','XXL',1,'[{\"added\": {}}]',9,1),(86,'2025-03-02 17:33:06.517360','12','Ceinture Cargo',1,'[{\"added\": {}}]',8,1),(87,'2025-03-02 17:33:19.873040','40','Fauve',1,'[{\"added\": {}}]',9,1),(88,'2025-03-02 17:33:36.657447','41','Unique',1,'[{\"added\": {}}]',9,1),(89,'2025-03-02 17:36:37.083658','13','Lunettes de Soleil',1,'[{\"added\": {}}]',8,1),(90,'2025-03-02 17:36:49.368246','42','Noir',1,'[{\"added\": {}}]',9,1),(91,'2025-03-02 17:36:59.155555','43','Unique',1,'[{\"added\": {}}]',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (7,'accounts','account'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(10,'carts','cart'),(11,'carts','cartitem'),(6,'category','category'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(8,'store','product'),(9,'store','variation');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'accounts','0001_initial','2025-03-02 15:56:43.989316'),(2,'contenttypes','0001_initial','2025-03-02 15:56:44.009661'),(3,'admin','0001_initial','2025-03-02 15:56:44.075861'),(4,'admin','0002_logentry_remove_auto_add','2025-03-02 15:56:44.078963'),(5,'admin','0003_logentry_add_action_flag_choices','2025-03-02 15:56:44.081236'),(6,'contenttypes','0002_remove_content_type_name','2025-03-02 15:56:44.107336'),(7,'auth','0001_initial','2025-03-02 15:56:44.172701'),(8,'auth','0002_alter_permission_name_max_length','2025-03-02 15:56:44.197965'),(9,'auth','0003_alter_user_email_max_length','2025-03-02 15:56:44.201495'),(10,'auth','0004_alter_user_username_opts','2025-03-02 15:56:44.204794'),(11,'auth','0005_alter_user_last_login_null','2025-03-02 15:56:44.207803'),(12,'auth','0006_require_contenttypes_0002','2025-03-02 15:56:44.208579'),(13,'auth','0007_alter_validators_add_error_messages','2025-03-02 15:56:44.212174'),(14,'auth','0008_alter_user_username_max_length','2025-03-02 15:56:44.218070'),(15,'auth','0009_alter_user_last_name_max_length','2025-03-02 15:56:44.221824'),(16,'auth','0010_alter_group_name_max_length','2025-03-02 15:56:44.232504'),(17,'auth','0011_update_proxy_permissions','2025-03-02 15:56:44.237844'),(18,'auth','0012_alter_user_first_name_max_length','2025-03-02 15:56:44.242012'),(19,'category','0001_initial','2025-03-02 15:56:44.253388'),(20,'store','0001_initial','2025-03-02 15:56:44.306687'),(21,'carts','0001_initial','2025-03-02 15:56:44.490040'),(22,'sessions','0001_initial','2025-03-02 15:56:44.502587');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('f4x1qkb12ydaw37ve1h53h2a353sq7i3','.eJxVjEEOwiAQRe_C2pBCYaAu3XsGMjCDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwkzgLJU6_W8T04LoDumO9NZlaXZc5yl2RB-3y2oifl8P9OyjYy7dGnRNEM2TUYzLKKcUmkc4D5nHykEYNBJksOKMjMWcLFo3xmsFNqLx4fwDyujgD:1tolhC:xuQ9wQC1K3FoH96SW6qxuWHMjsbGlUR0lUrZCVa0c6U','2025-03-16 15:57:38.432894');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_product`
--

DROP TABLE IF EXISTS `store_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title_online` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` double NOT NULL,
  `images` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `second_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `third_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fourth_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fifth_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `stock` int NOT NULL,
  `is_available` tinyint(1) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_name` (`product_name`),
  UNIQUE KEY `slug` (`slug`),
  KEY `store_product_category_id_574bae65_fk_category_category_id` (`category_id`),
  CONSTRAINT `store_product_category_id_574bae65_fk_category_category_id` FOREIGN KEY (`category_id`) REFERENCES `category_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_product`
--

LOCK TABLES `store_product` WRITE;
/*!40000 ALTER TABLE `store_product` DISABLE KEYS */;
INSERT INTO `store_product` VALUES (1,'Robe Évasée Bohème','Robe Évasée Bohème','robe-evasee-boheme','Robe fluide en coton avec motifs floraux, parfaite pour un look bohème chic.',49.99,'photos/products/robe-boheme1.webp','photos/products/robe-boheme2.webp','photos/products/robe-boheme3.webp','','',15,1,'2025-03-02 16:20:55.714969','2025-03-02 16:20:55.714987',2),(2,'Robe Bohème Fleurie','Robe Bohème Fleurie','robe-boheme-fleurie','La coupe asymétrique casse le côté sage de cette robe bohème à motif floral. Le décolleté cache-cœur enveloppe joliment la poitrine. La taille est marquée et soulignée par des liens à nouer avec des pompons. Cette robe bohème asymétrique, on la porte aussi bien pendant les vacances que pour une occasion spéciale telle qu\'un mariage.',69,'photos/products/robe-fleurie1.webp','photos/products/robe-fleurie2.webp','photos/products/robe-fleurie3.webp','','',4,1,'2025-03-02 16:34:46.192698','2025-03-02 16:34:46.192717',2),(3,'Foulard Imprimé Bohème','Foulard Imprimé Bohème','foulard-imprime-boheme','Pour pimper votre tenue et apportez de la couleur dans votre vie, optez pour cet accessoire bohème ! Ce foulard présente un imprimé intemporel et indémodable. Porté autour du cou ou sur les épaules, il complètera à merveille vos looks de mi-saison et réchauffera vos tenues d\'été.',9.9,'photos/products/foular1.webp','photos/products/fourlard2.webp','photos/products/fourlard3.webp','','',5,1,'2025-03-02 16:38:27.026131','2025-03-02 16:38:27.026149',7),(4,'Sneakers Compensées Bohème','Sneakers Compensées','sneakers-compensees-boheme','Glamour avec leur toile en suédine. Underground avec leur semelle crantée. On tombe sous le charme de ces sneakers compensées à l\'esprit bohème. rose, camel... Toutes les couleurs tendances de la saison sont là.',35,'photos/products/chaussure1.webp','photos/products/chaussure2.webp','photos/products/chaussure3.webp','','',1,1,'2025-03-02 16:41:59.651441','2025-03-02 16:48:30.435954',5),(5,'CEINTURE FEMME EN CUIR NOIR','Ceinture En Cuir Noir','ceinture-femme-en-cuir-noir','Cette boucle arrondie donnera une touche de personnalité à vos vêtements. Fabriquée en France, cette ceinture est réalisée en cuir de haute qualité, et équipée d\'une boucle originale et brillante. Elle peut être portée avec des jeans, mais aussi pour ceinturer des robes ou des manteaux.',59,'photos/products/ceinture1.jpg','photos/products/ceinture2.webp','photos/products/ceinture3.webp','photos/products/ceinture4.webp','',2,1,'2025-03-02 16:46:15.020250','2025-03-02 16:46:48.821800',4),(6,'T-shirt côtelé à encolure dégagée','T-shirt côtelé','t-shirt-cotele-a-encolure-degagee','Adoptez un look raffiné et décontracté avec ce T-shirt côtelé à encolure dégagée. Conçu dans une matière douce et extensible, il épouse parfaitement la silhouette pour un style chic et féminin. Ses manches courtes et sa coupe ajustée en font un basique idéal pour la saison printemps-été. À porter avec un jean taille haute ou une jupe fluide pour un look tendance.',8,'photos/products/tshir1.webp','photos/products/tshir2.webp','photos/products/tshir4.webp','photos/products/tshir5.webp','',5,1,'2025-03-02 16:52:16.490841','2025-03-02 16:52:16.490883',1),(7,'Jeans à jambes larges','Jeans à jambes larges','jeans-a-jambes-larges','Ce jeans large de Street One pour femmes marque des points avec son délavage bleu et son style classique à 5 poches. Le mélange de coton avec une part de stretch le rend particulièrement agréable à porter, tandis que la taille haute et la coupe loose complètent le look.',59.99,'photos/products/jean1.webp','photos/products/jean2.webp','photos/products/jean3.webp','','',4,1,'2025-03-02 16:58:34.903830','2025-03-02 16:58:34.903848',3),(8,'Veste de costume','Veste de costume','veste-de-costume','Apportez une touche d\'élégance à votre garde-robe avec cette veste de costume en laine \"Night Sky\". Confectionnée dans un tissu haut de gamme, elle offre une coupe structurée et fluide, parfaite pour un style professionnel ou une tenue habillée. Son coloris bleu nuit profond sublime toutes les silhouettes, tandis que sa doublure soyeuse assure un confort optimal. Idéale pour le bureau, une soirée ou un événement spécial.',145,'photos/products/veste1.webp','photos/products/veste2.webp','photos/products/veste3.webp','photos/products/veste4.webp','',1,1,'2025-03-02 17:08:15.217103','2025-03-02 17:08:15.217121',6),(9,'Polo Homme','Polo Iconique','polo-homme','C\'est le polo classique parfait ! La coupe est intemporelle. En maille piquée, sa double structure apporte douceur et résistance au tissu. La patte de boutonnage à deux boutons a été spécialement conçue pour allier solidité et harmonie ! Ses manches longues en feront un compagnon idéal pour l\'automne hiver.',29.9,'photos/products/polo1.webp','photos/products/polo3.webp','photos/products/polo4.webp','','',2,1,'2025-03-02 17:15:00.053827','2025-03-02 17:15:00.053843',8),(10,'Jean Relaxed Fit','Jean Relaxed Fit','jean-relaxed-fit','Ce jean relaxed à finition délavée est l’allié parfait pour un style décontracté et moderne. Sa coupe ample et confortable assure une liberté de mouvement optimale tout en apportant une touche urbaine tendance.',99.99,'photos/products/jeansH1.webp','photos/products/jeansH2.webp','photos/products/jeansH3.webp','','',2,1,'2025-03-02 17:18:44.186930','2025-03-02 17:18:44.186946',9),(11,'CHEMISE HOMME','Chemise Homme','chemise-homme','Cette chemise noire pour homme est un essentiel du dressing masculin. Son tissu doux et respirant assure un confort optimal, tandis que sa coupe ajustée ou regular met en valeur la silhouette. Que ce soit pour une tenue professionnelle, une soirée élégante ou un look décontracté, elle s’adapte à toutes les occasions. Ses finitions soignées, son col structuré et ses boutons discrets en font une pièce intemporelle et raffinée.',31.99,'photos/products/chemise1.jpg','photos/products/chemise2.jpg','photos/products/chemise3.jpg','','',1,1,'2025-03-02 17:26:25.301383','2025-03-02 17:26:25.301398',10),(12,'Ceinture Cargo','Ceinture Cargo','ceinture-cargo','Cuir foulonné, souple et très confortable. Parfait pour les petits tours de taille.',55,'photos/products/ceintu1.webp','photos/products/ceintu2.webp','','','',1,1,'2025-03-02 17:33:06.516509','2025-03-02 17:33:06.516525',11),(13,'Lunettes de Soleil','Lunettes de Soleil','lunettes-de-soleil','Lunettes de soleil polarisées pour hommes - Savourez une clarté impeccable avec nos lunettes de soleil polarisées conçues pour les hommes et les femmes. Arborant une monture en PC souple et robuste, ces lunettes de soleil sont ultra-légères et confortables à porter. Suffisamment robustes pour surmonter tous les obstacles que vous rencontrez, garantissant un confort optimal en tout temps.',14.99,'photos/products/lunette1.jpg','photos/products/lunette2.jpg','photos/products/lunette3.jpg','','',1,1,'2025-03-02 17:36:37.083041','2025-03-02 17:36:37.083056',12);
/*!40000 ALTER TABLE `store_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `store_variation`
--

DROP TABLE IF EXISTS `store_variation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_variation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `variation_category` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `variation_value` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `store_variation_product_id_e4f08cbc_fk_store_product_id` (`product_id`),
  CONSTRAINT `store_variation_product_id_e4f08cbc_fk_store_product_id` FOREIGN KEY (`product_id`) REFERENCES `store_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_variation`
--

LOCK TABLES `store_variation` WRITE;
/*!40000 ALTER TABLE `store_variation` DISABLE KEYS */;
INSERT INTO `store_variation` VALUES (1,'color','Corail',1,'2025-03-02 16:30:14.214887',1),(2,'color','Vert',1,'2025-03-02 16:30:26.894671',1),(3,'size','S',1,'2025-03-02 16:30:41.877043',1),(4,'size','L',1,'2025-03-02 16:31:48.781594',1),(5,'size','XL',1,'2025-03-02 16:31:58.176724',1),(6,'size','L',1,'2025-03-02 16:35:06.926996',2),(7,'size','XL',1,'2025-03-02 16:35:15.379866',2),(8,'color','Unique',1,'2025-03-02 16:35:29.141456',2),(9,'size','Unique',1,'2025-03-02 16:38:43.511400',3),(10,'color','Unique',1,'2025-03-02 16:38:52.295880',3),(11,'color','Camel',1,'2025-03-02 16:42:30.742555',4),(12,'color','Rose',1,'2025-03-02 16:42:50.759682',4),(13,'size','36',1,'2025-03-02 16:43:03.217798',4),(14,'size','38',1,'2025-03-02 16:43:11.785792',4),(15,'size','40',1,'2025-03-02 16:47:04.008172',5),(16,'color','Noir',1,'2025-03-02 16:47:12.580400',5),(17,'color','Bleu',1,'2025-03-02 16:53:06.052436',6),(18,'color','Vert',1,'2025-03-02 16:53:15.510628',6),(19,'color','Beige',1,'2025-03-02 16:53:25.944347',6),(20,'size','M',1,'2025-03-02 16:53:36.370564',6),(21,'size','L',1,'2025-03-02 16:53:45.897909',6),(22,'size','S',1,'2025-03-02 16:53:53.211810',6),(23,'color','Bleu',1,'2025-03-02 17:03:12.422815',7),(24,'size','W25 / L32',1,'2025-03-02 17:03:32.794658',7),(25,'size','W26 / L30',1,'2025-03-02 17:03:52.025066',7),(26,'color','Bleu Night Sky',1,'2025-03-02 17:08:47.701535',8),(27,'size','34',1,'2025-03-02 17:09:00.906734',8),(28,'size','36',1,'2025-03-02 17:09:09.925893',8),(29,'size','38',1,'2025-03-02 17:09:18.180164',8),(30,'color','Vert',1,'2025-03-02 17:15:12.555448',9),(31,'color','Bleu',1,'2025-03-02 17:15:22.840881',9),(32,'size','M',1,'2025-03-02 17:15:33.991379',9),(33,'size','L',1,'2025-03-02 17:15:41.165608',9),(34,'color','Bleu',1,'2025-03-02 17:19:13.250273',10),(35,'size','S',1,'2025-03-02 17:19:25.866697',10),(36,'size','L',1,'2025-03-02 17:19:33.001455',10),(37,'color','Noir',1,'2025-03-02 17:26:36.339489',11),(38,'size','L',1,'2025-03-02 17:26:50.168497',11),(39,'size','XXL',1,'2025-03-02 17:26:59.803978',11),(40,'color','Fauve',1,'2025-03-02 17:33:19.872278',12),(41,'size','Unique',1,'2025-03-02 17:33:36.656801',12),(42,'color','Noir',1,'2025-03-02 17:36:49.367522',13),(43,'size','Unique',1,'2025-03-02 17:36:59.154926',13);
/*!40000 ALTER TABLE `store_variation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-02 18:46:17
