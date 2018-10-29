/*
 Navicat Premium Data Transfer

 Source Server         : TopGus
 Source Server Type    : MySQL
 Source Server Version : 50535
 Source Host           : pbbf0v0d.2320.dnstoo.com:5511
 Source Schema         : topgus

 Target Server Type    : MySQL
 Target Server Version : 50535
 File Encoding         : 65001

 Date: 29/10/2018 10:50:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `admin` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `pwd` varchar(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (2, '13302967280', 'Topgus001');

-- ----------------------------
-- Table structure for code
-- ----------------------------
DROP TABLE IF EXISTS `code`;
CREATE TABLE `code`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `phone` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` int(11) NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 45 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of code
-- ----------------------------
INSERT INTO `code` VALUES (20, '13414910014', 973411, '2018-09-30 22:21:08');
INSERT INTO `code` VALUES (21, '18173329631', 853236, '2018-10-09 16:51:54');
INSERT INTO `code` VALUES (22, '13418558197', 353580, '2018-10-04 14:52:38');
INSERT INTO `code` VALUES (23, '18721310898', 274689, '2018-10-11 15:55:48');
INSERT INTO `code` VALUES (24, '13600100862', 594026, '2018-10-08 19:22:02');
INSERT INTO `code` VALUES (25, '15891082033', 610348, '2018-10-09 16:03:05');
INSERT INTO `code` VALUES (26, '18660960278', 112691, '2018-10-10 15:57:36');
INSERT INTO `code` VALUES (27, '15060091067', 326667, '2018-10-10 17:35:28');
INSERT INTO `code` VALUES (28, '15842629720', 211219, '2018-10-10 18:00:00');
INSERT INTO `code` VALUES (29, '15026436157', 956339, '2018-10-10 18:37:16');
INSERT INTO `code` VALUES (30, '18566787220', 143860, '2018-10-10 19:35:35');
INSERT INTO `code` VALUES (31, '13602432917', 559234, '2018-10-10 20:17:16');
INSERT INTO `code` VALUES (32, '13080551542', 389807, '2018-10-10 21:37:59');
INSERT INTO `code` VALUES (33, '18818543001', 995063, '2018-10-11 07:48:14');
INSERT INTO `code` VALUES (34, '13760637646', 863145, '2018-10-11 15:54:12');
INSERT INTO `code` VALUES (35, '17722810272', 987736, '2018-10-11 23:57:17');
INSERT INTO `code` VALUES (36, '17771735093', 937183, '2018-10-12 09:52:41');
INSERT INTO `code` VALUES (37, '15014230970', 392996, '2018-10-12 09:54:45');
INSERT INTO `code` VALUES (38, '13641413155', 520446, '2018-10-13 01:38:47');
INSERT INTO `code` VALUES (39, '17315400297', 648814, '2018-10-13 14:25:23');
INSERT INTO `code` VALUES (40, '15837452530', 494833, '2018-10-20 10:16:30');
INSERT INTO `code` VALUES (41, '15874828147', 309912, '2018-10-22 11:20:36');
INSERT INTO `code` VALUES (42, '18371969646', 398763, '2018-10-25 09:31:01');
INSERT INTO `code` VALUES (43, '18825271586', 507932, '2018-10-25 10:39:39');
INSERT INTO `code` VALUES (44, '15882223314', 403359, '2018-10-28 10:43:18');

-- ----------------------------
-- Table structure for name
-- ----------------------------
DROP TABLE IF EXISTS `name`;
CREATE TABLE `name`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `open_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `nickname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `sex` int(1) NULL DEFAULT NULL,
  `headimgurl` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pwd` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `open`(`open_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 83 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of name
-- ----------------------------
INSERT INTO `name` VALUES (55, '62857846616', NULL, NULL, NULL, '13414910014', '123@123.com', '123456', '');
INSERT INTO `name` VALUES (57, '50770552149', NULL, NULL, NULL, '13418558197', 'daniel@topgus.com', '1586420862', '');
INSERT INTO `name` VALUES (59, '10644230394', NULL, NULL, NULL, '13600100862', '407711204@qq.com', 'abbie13', '');
INSERT INTO `name` VALUES (60, '57953892648', NULL, NULL, NULL, '15891082033', '451253508@qq.com', '123456', 'yan_bg');
INSERT INTO `name` VALUES (62, '33316946599', NULL, NULL, NULL, '18173329631', '1602331859@qq.com', '123456', 'yan_bg');
INSERT INTO `name` VALUES (63, '75367157633', NULL, NULL, NULL, '18660960278', '422547118@qq.com', '4806031', 'theonegxc');
INSERT INTO `name` VALUES (64, '84561565570', NULL, NULL, NULL, '15060091067', '344937278@qq.com', 'abc123456', '1317506165');
INSERT INTO `name` VALUES (65, '46270455875', NULL, NULL, NULL, '15842629720', '424214145@qq.com', '424214145', '林大鱼');
INSERT INTO `name` VALUES (66, '88383038389', NULL, NULL, NULL, '15026436157', 'hui8712@126.com', '123456', 'Nicole lee');
INSERT INTO `name` VALUES (67, '40711175215', NULL, NULL, NULL, '18566787220', '584676121@qq.com', 'liu584676121', '祥子');
INSERT INTO `name` VALUES (68, '69095905327', NULL, NULL, NULL, '13602432917', '3274582340@qq.com', 'shuju666', '婕利');
INSERT INTO `name` VALUES (69, '43171161752', NULL, NULL, NULL, '13080551542', '573684330@qq.com', 'aa123456', 'zkq55667788');
INSERT INTO `name` VALUES (70, '43841020304', NULL, NULL, NULL, '18818543001', 'hilaok@foxmail.com', 'hilaok', 'hilaok');
INSERT INTO `name` VALUES (71, '61133974480', NULL, NULL, NULL, '13760637646', 'lzz001@126.com', '123456*+', 'sssssspp');
INSERT INTO `name` VALUES (72, '20363770617', NULL, NULL, NULL, '18721310898', 'crystal@topgus.com', '3.1415926drym', 'drym917');
INSERT INTO `name` VALUES (73, '23226055760', NULL, NULL, NULL, '17722810272', '1530687747@qq.com', 'zly19910214', '不忘初心');
INSERT INTO `name` VALUES (74, '79956618614', NULL, NULL, NULL, '17771735093', '2920526190@qq.com', '961119ylxd', 'gongzuohaoone');
INSERT INTO `name` VALUES (75, '33483556989', NULL, NULL, NULL, '15014230970', '960940249@qq.com', 'apple199061@', '15014230970');
INSERT INTO `name` VALUES (76, '24642784651', NULL, NULL, NULL, '13641413155', '378575096@qq.com', 'aaa965311', '378575096');
INSERT INTO `name` VALUES (77, '2087439115', NULL, NULL, NULL, '17315400297', '632547819@qq.com', 'ztdwau214', 'zhangchunyan001');
INSERT INTO `name` VALUES (78, '14047764603', NULL, NULL, NULL, '15837452530', '565145393@qq.com', 'cmjkl1314', '陌上花开');
INSERT INTO `name` VALUES (79, '44363392357', NULL, NULL, NULL, '15874828147', '1107578349@qq.com', 'wdy6721430', '15874828147');
INSERT INTO `name` VALUES (80, '19393731193', NULL, NULL, NULL, '18371969646', '7599386@qq.com', 'toto123456', '古');
INSERT INTO `name` VALUES (81, '84631863638', NULL, NULL, NULL, '18825271586', '815161684@qq.com', 'liaoqiuli1314', 'Lilliian');
INSERT INTO `name` VALUES (82, '19589487381', NULL, NULL, NULL, '15882223314', '247110666@qq.com', '2654608ck', '15882223314');

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `orderno` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `open_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `count` int(11) NOT NULL,
  `time` datetime NOT NULL,
  `is_ok` int(1) NULL DEFAULT NULL,
  `note` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`orderno`) USING BTREE,
  INDEX `open_id`(`open_id`) USING BTREE,
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`open_id`) REFERENCES `name` (`open_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES ('201810101737001883', '84561565570', 2, '2018-10-10 17:37:00', 2, NULL);
INSERT INTO `orders` VALUES ('201810101841186348', '88383038389', 3, '2018-10-10 18:41:18', NULL, NULL);
INSERT INTO `orders` VALUES ('201810101946396091', '40711175215', 10, '2018-10-10 19:46:39', 2, NULL);
INSERT INTO `orders` VALUES ('201810102140080336', '43171161752', 1, '2018-10-10 21:40:08', 2, NULL);
INSERT INTO `orders` VALUES ('201810110749549002', '43841020304', 2, '2018-10-11 07:49:54', 2, NULL);
INSERT INTO `orders` VALUES ('201810111612504875', '61133974480', 1, '2018-10-11 16:12:50', 1, NULL);
INSERT INTO `orders` VALUES ('201810112359209773', '23226055760', 1, '2018-10-11 23:59:20', 2, NULL);
INSERT INTO `orders` VALUES ('201810120954279236', '79956618614', 1, '2018-10-12 09:54:27', 2, NULL);
INSERT INTO `orders` VALUES ('201810120957450699', '33483556989', 1, '2018-10-12 09:57:45', 2, NULL);
INSERT INTO `orders` VALUES ('201810130139556217', '24642784651', 1, '2018-10-13 01:39:55', 2, 'None');
INSERT INTO `orders` VALUES ('201810131426223247', '2087439115', 1, '2018-10-13 14:26:22', 2, '1');
INSERT INTO `orders` VALUES ('201810221122318641', '44363392357', 1, '2018-10-22 11:22:31', NULL, 'None');
INSERT INTO `orders` VALUES ('201810250932176770', '19393731193', 1, '2018-10-25 09:32:17', 1, '没有用吗');
INSERT INTO `orders` VALUES ('201810251042011773', '84631863638', 1, '2018-10-25 10:42:01', NULL, '2222');

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderno` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `keyword` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `orderno`(`orderno`) USING BTREE,
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`orderno`) REFERENCES `orders` (`orderno`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 493 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES (436, '201810101737001883', 'card holder');
INSERT INTO `product` VALUES (437, '201810101737001883', 'card case');
INSERT INTO `product` VALUES (444, '201810101841186348', 'Surgical tape');
INSERT INTO `product` VALUES (445, '201810101841186348', 'Kinesiology tape');
INSERT INTO `product` VALUES (446, '201810101841186348', 'Sports tape');
INSERT INTO `product` VALUES (447, '201810101946396091', 'Fitbit charge 2 bands for women');
INSERT INTO `product` VALUES (448, '201810101946396091', 'Fitbit charge 2 bands leather');
INSERT INTO `product` VALUES (449, '201810101946396091', 'Fitbit charge 2 metal bands');
INSERT INTO `product` VALUES (450, '201810101946396091', 'Fitbit charge 2 replacement band');
INSERT INTO `product` VALUES (451, '201810101946396091', 'Fitbit charge 2 rose gold bands');
INSERT INTO `product` VALUES (452, '201810101946396091', 'Fitbit charge 2 silver bands');
INSERT INTO `product` VALUES (453, '201810101946396091', 'charge 2 bands');
INSERT INTO `product` VALUES (454, '201810101946396091', 'fitbit charge 2 bands');
INSERT INTO `product` VALUES (455, '201810101946396091', 'Fitbit charge 2 gold bands');
INSERT INTO `product` VALUES (456, '201810101946396091', 'Fit bit charge 2 bands');
INSERT INTO `product` VALUES (457, '201810102140080336', 'Charging Cable');
INSERT INTO `product` VALUES (458, '201810110749549002', 'led strip connector');
INSERT INTO `product` VALUES (459, '201810110749549002', 'wire connector');
INSERT INTO `product` VALUES (479, '201810111612504875', 'ultraschall physiotherapie');
INSERT INTO `product` VALUES (480, '201810112359209773', 'music downloader');
INSERT INTO `product` VALUES (481, '201810120954279236', 'latex pillow');
INSERT INTO `product` VALUES (482, '201810120957450699', 'Desk cable clips.  Disposable makeup applicators. Nail clip caps. Fake nail cutter. Slime suuplies kit.');
INSERT INTO `product` VALUES (483, '201810130139556217', '学习');
INSERT INTO `product` VALUES (484, '201810131426223247', 'men shirt');
INSERT INTO `product` VALUES (490, '201810221122318641', 'digital photo frame');
INSERT INTO `product` VALUES (491, '201810250932176770', '女鞋');
INSERT INTO `product` VALUES (492, '201810251042011773', 'beside shelf');

SET FOREIGN_KEY_CHECKS = 1;
