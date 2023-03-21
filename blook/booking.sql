CREATE DATABASE IF NOT EXISTS booking DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE booking;

create table booking (
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	customer_id INT NOT NULL,
	activity_id INT NOT NULL,
	booking_datetime DATE NOT NULL,
	datetime DATE NOT NULL,
	total_pax INT NOT NULL,
	payment_amount DECIMAL(6,2) NOT NULL,
    status VARCHAR(3) NOT NULL
);


INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (1,100,'2022-08-22','2022-12-31',1,65,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (2,24,'2022-08-03','2023-01-04',1,56,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (3,101,'2022-08-24','2022-10-28',5,270,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (4,76,'2022-07-04','2022-10-13',3,90,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (5,5,'2022-06-17','2022-11-02',5,255,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (6,52,'2022-08-02','2023-01-25',2,88,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (7,82,'2022-07-23','2022-10-19',1,36,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (8,77,'2022-06-04','2023-02-03',4,148,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (9,35,'2022-06-14','2022-10-13',2,124,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (10,40,'2022-06-30','2022-10-16',5,185,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (11,89,'2022-06-13','2022-11-12',3,132,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (12,89,'2022-07-27','2022-10-19',4,176,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (13,1,'2022-07-20','2023-02-27',5,155,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (14,2,'2022-07-23','2023-01-12',1,30,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (15,37,'2022-07-13','2022-12-19',5,180,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (16,36,'2022-06-24','2023-01-18',3,174,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (17,24,'2022-07-05','2022-11-12',5,280,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (18,5,'2022-07-21','2022-12-15',5,255,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (19,32,'2022-07-16','2022-11-14',2,120,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (20,98,'2022-07-04','2022-09-29',3,102,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (21,25,'2022-06-29','2023-02-03',2,108,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (22,8,'2022-06-19','2022-09-17',4,168,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (23,36,'2022-06-06','2022-11-27',1,58,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (24,92,'2022-06-22','2023-01-01',3,174,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (25,14,'2022-08-14','2022-09-29',4,216,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (26,101,'2022-08-26','2023-01-28',4,216,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (27,83,'2022-06-21','2022-11-06',3,114,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (28,26,'2022-07-21','2023-01-27',4,148,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (29,51,'2022-08-12','2022-12-02',3,93,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (30,84,'2022-07-17','2022-11-13',1,57,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (31,89,'2022-08-03','2023-01-29',1,44,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (32,57,'2022-08-22','2022-11-19',3,132,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (33,73,'2022-06-03','2023-02-03',2,110,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (34,43,'2022-06-17','2022-12-31',3,132,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (35,52,'2022-08-23','2022-09-17',5,220,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (36,60,'2022-08-29','2023-02-04',2,110,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (37,9,'2022-06-27','2023-01-28',1,37,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (38,84,'2022-06-30','2023-01-07',5,285,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (39,101,'2022-06-23','2023-01-24',3,162,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (40,96,'2022-07-14','2023-02-06',4,136,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (41,6,'2022-07-13','2023-01-03',5,300,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (42,42,'2022-06-05','2023-02-18',5,240,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (43,17,'2022-06-18','2022-12-16',3,165,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (44,7,'2022-07-07','2022-11-27',3,168,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (45,90,'2022-06-23','2023-02-04',5,275,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (46,68,'2022-07-27','2022-12-19',5,300,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (47,35,'2022-08-20','2023-02-15',1,62,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (48,11,'2022-07-28','2022-10-22',3,174,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (49,59,'2022-06-17','2023-02-14',1,65,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (50,37,'2022-07-06','2022-10-02',1,36,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (51,53,'2022-07-31','2022-10-16',4,144,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (52,68,'2022-07-12','2023-01-12',1,60,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (53,42,'2022-06-20','2023-01-13',3,144,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (54,25,'2022-07-27','2022-09-19',3,162,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (55,53,'2022-06-13','2022-10-28',3,108,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (56,67,'2022-06-13','2022-10-14',1,60,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (57,12,'2022-06-19','2022-11-04',3,159,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (58,39,'2022-07-03','2023-01-16',1,59,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (59,28,'2022-07-09','2022-09-05',5,265,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (60,22,'2022-06-22','2022-10-03',3,165,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (61,11,'2022-06-04','2022-12-18',4,232,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (62,2,'2022-07-14','2023-02-05',2,60,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (63,61,'2022-07-15','2023-02-19',1,61,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (64,101,'2022-08-25','2022-09-18',4,216,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (65,64,'2022-07-25','2022-11-12',5,325,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (66,54,'2022-08-10','2022-10-26',5,305,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (67,44,'2022-07-13','2023-01-27',4,152,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (68,23,'2022-07-06','2022-09-02',4,140,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (69,31,'2022-06-13','2022-09-05',1,53,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (70,40,'2022-06-20','2022-12-13',5,185,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (71,74,'2022-08-11','2022-10-18',4,140,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (72,5,'2022-07-30','2022-12-04',1,51,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (73,14,'2022-07-06','2023-01-07',4,216,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (74,27,'2022-06-28','2022-12-05',4,200,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (75,53,'2022-06-28','2022-11-13',1,36,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (76,88,'2022-07-17','2023-01-20',1,34,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (77,27,'2022-07-22','2023-01-05',1,50,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (78,80,'2022-07-07','2022-09-16',1,37,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (79,11,'2022-06-20','2022-10-02',2,116,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (80,30,'2022-08-01','2023-02-11',3,174,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (81,19,'2022-08-12','2022-09-10',4,192,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (82,31,'2022-06-19','2022-11-18',4,212,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (83,34,'2022-07-12','2022-12-19',1,48,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (84,36,'2022-07-16','2022-10-14',5,290,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (85,58,'2022-08-04','2023-01-23',5,325,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (86,98,'2022-08-04','2023-01-05',5,170,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (87,95,'2022-08-09','2022-09-15',4,140,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (88,4,'2022-08-12','2022-09-08',1,37,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (89,37,'2022-06-24','2023-02-16',2,72,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (90,73,'2022-06-19','2022-09-25',3,165,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (91,24,'2022-06-07','2022-12-13',4,224,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (92,86,'2022-08-02','2022-10-20',3,180,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (93,7,'2022-07-01','2022-12-01',5,280,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (94,33,'2022-08-08','2022-10-09',2,104,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (95,55,'2022-07-07','2022-12-26',2,74,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (96,31,'2022-08-17','2022-11-10',5,265,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (97,72,'2022-06-13','2022-12-30',2,96,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (98,82,'2022-06-16','2022-12-04',5,180,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (99,19,'2022-07-31','2022-12-12',1,48,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (100,11,'2022-06-25','2022-09-22',2,116,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (1,15,'2022-07-09','2023-01-24',5,210,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (2,25,'2022-06-22','2022-10-23',1,54,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (3,10,'2022-08-09','2023-01-25',4,164,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (4,19,'2022-07-23','2023-01-31',1,48,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (5,29,'2022-08-21','2023-01-10',5,225,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (6,6,'2022-07-10','2022-09-30',5,300,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (7,81,'2022-06-14','2022-12-18',4,132,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (8,101,'2022-08-04','2022-09-18',3,162,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (9,54,'2022-07-31','2023-01-25',3,183,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (10,37,'2022-07-25','2022-09-11',5,180,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (11,66,'2022-07-07','2022-10-17',3,99,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (12,56,'2022-06-14','2023-01-06',3,120,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (13,66,'2022-08-14','2022-09-25',4,132,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (14,87,'2022-07-03','2022-09-16',5,250,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (15,23,'2022-08-03','2022-11-29',1,35,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (16,1,'2022-08-11','2023-01-15',3,93,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (17,63,'2022-07-21','2022-11-20',2,84,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (18,51,'2022-08-23','2022-10-10',2,62,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (19,65,'2022-07-05','2022-09-28',5,200,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (20,66,'2022-07-15','2023-01-20',3,99,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (21,36,'2022-07-27','2022-09-21',1,58,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (22,89,'2022-06-09','2023-01-05',2,88,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (23,68,'2022-06-23','2023-02-22',1,60,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (24,90,'2022-07-19','2022-10-02',5,275,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (25,48,'2022-06-02','2022-09-14',2,124,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (26,77,'2022-06-18','2022-11-05',4,148,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (27,28,'2022-07-09','2023-01-08',2,106,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (28,48,'2022-07-18','2022-10-28',3,186,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (29,63,'2022-07-16','2022-09-15',3,126,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (30,50,'2022-06-08','2023-01-12',1,43,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (31,38,'2022-08-23','2022-12-29',1,46,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (32,37,'2022-08-22','2022-11-16',2,72,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (33,92,'2022-06-24','2022-11-13',1,58,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (34,28,'2022-07-23','2022-11-02',5,265,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (35,27,'2022-08-24','2022-11-15',1,50,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (36,101,'2022-06-04','2022-09-12',4,216,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (37,60,'2022-07-27','2022-10-05',5,275,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (38,49,'2022-06-06','2023-02-04',3,165,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (39,77,'2022-08-13','2022-10-01',2,74,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (40,90,'2022-06-25','2022-12-11',1,55,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (41,12,'2022-07-28','2022-10-16',4,212,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (42,3,'2022-08-13','2022-10-05',1,33,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (43,34,'2022-06-09','2022-12-03',2,96,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (44,28,'2022-07-02','2022-12-17',4,212,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (45,57,'2022-07-02','2022-09-09',2,88,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (46,27,'2022-08-03','2022-09-22',3,150,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (47,27,'2022-08-04','2022-11-06',4,200,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (48,81,'2022-06-15','2022-10-12',3,99,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (49,78,'2022-08-04','2022-09-06',1,33,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (50,90,'2022-07-10','2023-01-16',4,220,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (51,23,'2022-08-27','2022-11-10',5,175,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (52,3,'2022-08-07','2023-01-09',3,99,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (53,5,'2022-06-27','2022-10-21',3,153,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (54,79,'2022-06-14','2023-02-11',4,132,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (55,32,'2022-07-04','2022-09-22',1,60,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (56,26,'2022-07-04','2022-12-20',3,111,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (57,12,'2022-07-03','2022-11-10',2,106,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (58,99,'2022-07-20','2022-10-01',5,310,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (59,29,'2022-06-08','2023-01-01',4,180,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (60,74,'2022-08-11','2023-01-23',1,35,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (61,75,'2022-07-07','2022-09-24',2,94,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (62,44,'2022-06-02','2022-11-12',2,76,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (63,95,'2022-07-06','2022-11-07',2,70,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (64,50,'2022-08-09','2023-02-24',3,129,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (65,44,'2022-06-18','2022-11-25',1,38,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (66,6,'2022-08-11','2023-01-15',3,180,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (67,78,'2022-06-06','2022-12-23',3,99,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (68,20,'2022-08-29','2022-09-07',5,280,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (69,29,'2022-08-13','2023-01-06',5,225,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (70,102,'2022-08-22','2022-09-27',5,270,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (71,14,'2022-08-06','2022-11-16',4,216,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (72,91,'2022-08-18','2022-11-01',2,62,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (73,13,'2022-08-22','2023-02-17',1,31,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (74,22,'2022-07-02','2023-02-13',5,275,'NO');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (75,97,'2022-06-21','2022-10-27',2,128,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (76,81,'2022-06-27','2022-10-11',5,165,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (77,77,'2022-07-01','2022-12-11',2,74,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (78,35,'2022-07-08','2022-10-13',1,62,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (79,64,'2022-06-13','2022-12-10',4,260,'YES');
INSERT INTO booking(customer_id,activity_id,booking_datetime,datetime,total_pax,payment_amount,status) VALUES (80,40,'2022-07-07','2022-10-15',1,37,'YES');