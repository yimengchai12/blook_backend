CREATE DATABASE IF NOT EXISTS customer DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE customer;

create table customer (
	ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
	email VARCHAR(255) NOT NULL,
    gender VARCHAR(7) NOT NULL,
	address VARCHAR(50) NOT NULL,
    billing_address VARCHAR(50),
	phone VARCHAR(50) NOT NULL,
	point INT NULL
);


insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Penrod', 'Bony', 'pbony0@dmoz.org', 'Male', '93 Lawn Drive', null, '+86 (166) 208-3670', 100);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Darrelle', 'Rimmer', 'drimmer1@last.fm', 'Female', '172 Pennsylvania Center', null, '+86 (917) 459-8532', 200);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Mitch', 'Redhead', 'mredhead2@github.com', 'Male', '690 Linden Avenue', null, '+351 (847) 794-9904', 0);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Shani', 'Hurdedge', 'shurdedge3@github.com', 'Female', '212 6th Circle', '351 Mcbride Street', '+1 (318) 919-8632', 40);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Maggee', 'Lamberto', 'mlamberto4@ted.com', 'Female', '93620 Rockefeller Place', null, '+55 (261) 375-3977', 20);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Alfie', 'Jaume', 'ajaume5@blogs.com', 'Female', '33010 Spenser Hill', '4 Esch Court', '+63 (464) 166-9286',70);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Matty', 'Bulger', 'mbulger6@last.fm', 'Male', '9617 Marcy Point', '334 Wayridge Circle', '+81 (493) 771-6802', 90);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Addie', 'Radleigh', 'aradleigh7@huffingtonpost.com', 'Male', '8 Maple Wood Point', '47 Atwood Plaza', '+86 (647) 295-2989', 120);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Celesta', 'Maevela', 'cmaevela8@cornell.edu', 'Female', '65 Knutson Center', '937 Declaration Pass', '+234 (562) 104-9126',400);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Enid', 'MacColl', 'emaccoll9@addthis.com', 'Female', '70 Arrowood Lane', '43 Toban Plaza', '+51 (501) 234-7513',500);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Tomasine', 'Hardey', 'thardeya@adobe.com', 'Female', '2 Sachtjen Terrace', null, '+86 (185) 671-6110',2400);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Basil', 'Kimmons', 'bkimmonsb@eventbrite.com', 'Male', '81976 Brickson Park Court', '46 Maple Lane', '+62 (925) 588-4272',2500);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Clarke', 'Croome', 'ccroomec@slate.com', 'Male', '46432 Weeping Birch Lane', null, '+46 (221) 492-7667',500);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone, point) values ('Tremaine', 'Tapply', 'ttapplyd@istockphoto.com', 'Male', '79620 Transport Junction', '05 Farmco Lane', '+62 (482) 456-6399',2000);
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Patrizia', 'Punyer', 'ppunyere@youtu.be', 'Female', '8099 Gulseth Place', '70 Daystar Point', '+250 (908) 131-5407');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Gaelan', 'Larrat', 'glarratf@ebay.com', 'Male', '689 Continental Drive', null, '+98 (639) 905-0850');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Jeromy', 'Pamment', 'jpammentg@live.com', 'Male', '09719 Del Mar Junction', null, '+62 (429) 751-5087');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Marrilee', 'Yeowell', 'myeowellh@pagesperso-orange.fr', 'Female', '90 Randy Avenue', null, '+856 (669) 522-1114');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Orlan', 'Houtbie', 'ohoutbiei@discovery.com', 'Male', '0263 Atwood Way', '26 Mallard Lane', '+351 (993) 598-8268');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Jimmie', 'Garey', 'jgareyj@pinterest.com', 'Male', '22346 Green Ridge Court', '32700 Meadow Valley Plaza', '+977 (676) 715-0567');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Bellina', 'Zelake', 'bzelakek@businessweek.com', 'Female', '439 Old Shore Trail', null, '+62 (937) 823-2048');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Astrid', 'Rothert', 'arothertl@dropbox.com', 'Female', '197 Morrow Center', null, '+86 (875) 404-6079');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Whitby', 'Eddington', 'weddingtonm@go.com', 'Male', '687 Bashford Drive', '006 Memorial Lane', '+94 (533) 660-3644');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Eugenius', 'Kubasiewicz', 'ekubasiewiczn@de.vu', 'Male', '17 Mccormick Parkway', null, '+63 (248) 828-0124');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Grover', 'Coolson', 'gcoolsono@bluehost.com', 'Male', '29 Emmet Plaza', null, '+52 (195) 966-8266');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Colet', 'Scading', 'cscadingp@theatlantic.com', 'Male', '969 Dottie Crossing', null, '+1 (822) 159-2550');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Llewellyn', 'Trivett', 'ltrivettq@blogspot.com', 'Male', '51237 Bonner Hill', null, '+86 (820) 847-5623');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Emlen', 'Mullaney', 'emullaneyr@cargocollective.com', 'Male', '71 Bobwhite Junction', null, '+598 (246) 601-5518');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Neal', 'Hillatt', 'nhillatts@t-online.de', 'Male', '24 Transport Point', '67 Green Ridge Terrace', '+234 (975) 370-9662');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Dina', 'Bazek', 'dbazekt@patch.com', 'Female', '4 Dayton Plaza', '4968 Morrow Trail', '+967 (801) 898-6471');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Keith', 'Hendonson', 'khendonsonu@aol.com', 'Male', '73161 Hanson Alley', null, '+86 (137) 418-6302');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Babara', 'Tottman', 'btottmanv@elpais.com', 'Female', '69 Jenna Terrace', '4166 Messerschmidt Hill', '+86 (939) 532-2157');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Skell', 'Polglase', 'spolglasew@bloglovin.com', 'Male', '00375 Leroy Hill', null, '+86 (783) 999-7179');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Ruthanne', 'Moneti', 'rmonetix@rakuten.co.jp', 'Female', '19 Roth Terrace', null, '+255 (213) 871-4726');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Keeley', 'Bischoff', 'kbischoffy@psu.edu', 'Female', '19 North Point', null, '+62 (191) 115-8996');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Ryun', 'MacCrann', 'rmaccrannz@wikispaces.com', 'Male', '53 Commercial Lane', '29721 Duke Circle', '+86 (648) 220-2305');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Milissent', 'Krzysztof', 'mkrzysztof10@pagesperso-orange.fr', 'Female', '9 Sherman Court', null, '+27 (762) 506-1131');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Gaby', 'Ferrand', 'gferrand11@salon.com', 'Female', '1871 Scofield Terrace', null, '+351 (403) 362-5101');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Claudell', 'McKirdy', 'cmckirdy12@businesswire.com', 'Male', '66622 Haas Park', null, '+63 (890) 492-1426');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Homer', 'Innott', 'hinnott13@mac.com', 'Male', '2 Bowman Street', '6 Village Way', '+48 (104) 572-0941');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Shel', 'Fassman', 'sfassman14@sun.com', 'Female', '96821 Tennyson Drive', '0 Tennessee Court', '+420 (625) 214-6520');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Farah', 'Hadenton', 'fhadenton15@mashable.com', 'Female', '80 Delladonna Trail', null, '+1 (499) 826-4835');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Ruperto', 'Delgadillo', 'rdelgadillo16@nps.gov', 'Male', '9899 Nova Alley', null, '+66 (252) 374-9477');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Johnathan', 'Petrovsky', 'jpetrovsky17@gnu.org', 'Male', '9 Redwing Junction', '107 Hollow Ridge Parkway', '+84 (351) 295-1502');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Lindy', 'Giamitti', 'lgiamitti18@aboutads.info', 'Female', '33 Moose Alley', '7 High Crossing Circle', '+86 (413) 976-9789');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Mathian', 'Arter', 'marter19@weebly.com', 'Male', '7916 Derek Pass', null, '+62 (127) 188-5643');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Kasper', 'Lambersen', 'klambersen1a@hao123.com', 'Male', '9130 Victoria Drive', null, '+55 (180) 729-1415');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Rodge', 'Hedge', 'rhedge1b@amazon.co.jp', 'Male', '34 Nevada Plaza', null, '+7 (449) 889-1288');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Nissy', 'Boxall', 'nboxall1c@freewebs.com', 'Female', '5328 Drewry Center', null, '+255 (727) 359-5545');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Waite', 'Kemshell', 'wkemshell1d@irs.gov', 'Male', '4 2nd Hill', null, '+62 (442) 331-8416');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Marjorie', 'Renols', 'mrenols1e@bizjournals.com', 'Female', '12141 Menomonie Street', null, '+62 (309) 101-2209');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Murvyn', 'Eisikowitz', 'meisikowitz1f@constantcontact.com', 'Male', '4909 Orin Point', '01523 Graceland Park', '+81 (342) 985-5269');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Ringo', 'Wateridge', 'rwateridge1g@fotki.com', 'Male', '2 Mcguire Place', null, '+48 (322) 649-6095');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Delmar', 'Murthwaite', 'dmurthwaite1h@cargocollective.com', 'Male', '21876 Sycamore Court', '61 Sunfield Circle', '+62 (698) 581-5619');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Shelba', 'Liveley', 'sliveley1i@sitemeter.com', 'Female', '0562 Thackeray Road', null, '+86 (864) 422-9734');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Mill', 'Mc Kellen', 'mmckellen1j@answers.com', 'Male', '134 Butternut Hill', null, '+60 (700) 361-1749');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Kristina', 'McAnulty', 'kmcanulty1k@meetup.com', 'Female', '4325 Talmadge Circle', '9 Kim Crossing', '+7 (169) 322-0552');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Derek', 'Chrismas', 'dchrismas1l@marriott.com', 'Male', '1 Meadow Vale Trail', null, '+86 (392) 412-6554');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Gill', 'Selcraig', 'gselcraig1m@reddit.com', 'Male', '53 Garrison Park', null, '+62 (389) 666-3420');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Farrand', 'Corking', 'fcorking1n@gov.uk', 'Female', '1 Atwood Circle', null, '+86 (954) 552-3515');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Dario', 'Dessaur', 'ddessaur1o@samsung.com', 'Male', '8578 Transport Hill', null, '+54 (389) 655-1854');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Cally', 'Kwietak', 'ckwietak1p@chronoengine.com', 'Female', '8292 Union Lane', null, '+86 (783) 884-4611');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Reynard', 'Branson', 'rbranson1q@ucoz.ru', 'Male', '22546 Garrison Point', null, '+1 (682) 969-7564');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Auguste', 'Vasyutkin', 'avasyutkin1r@i2i.jp', 'Female', '98196 Autumn Leaf Center', null, '+86 (935) 955-1512');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Flori', 'Noden', 'fnoden1s@earthlink.net', 'Female', '0 Mcbride Park', null, '+33 (744) 617-2307');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Martino', 'Fenimore', 'mfenimore1t@exblog.jp', 'Male', '8 Portage Pass', null, '+84 (794) 983-5875');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Loy', 'Eddison', 'leddison1u@cargocollective.com', 'Male', '07937 Memorial Plaza', null, '+33 (182) 744-9337');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Carney', 'Heller', 'cheller1v@gmpg.org', 'Male', '52888 Sugar Street', null, '+81 (765) 670-6440');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Garnette', 'McAnulty', 'gmcanulty1w@omniture.com', 'Female', '43 Kingsford Crossing', null, '+502 (965) 677-4633');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Edouard', 'Kline', 'ekline1x@si.edu', 'Male', '26480 Welch Crossing', '8 Michigan Hill', '+31 (459) 454-4303');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Bettine', 'Jouhning', 'bjouhning1y@goo.ne.jp', 'Female', '1 Forest Run Trail', '37 Erie Trail', '+55 (241) 858-1429');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Kelley', 'Waby', 'kwaby1z@howstuffworks.com', 'Female', '1258 Arizona Point', null, '+86 (983) 597-1036');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Tonya', 'Menis', 'tmenis20@studiopress.com', 'Female', '71 Graedel Avenue', null, '+386 (736) 910-4124');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Wakefield', 'MacFarlane', 'wmacfarlane21@gmpg.org', 'Male', '9 Morningstar Lane', '258 Arapahoe Hill', '+86 (973) 457-4433');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Reeba', 'McKimm', 'rmckimm22@mysql.com', 'Female', '99 Porter Court', '71859 Haas Way', '+55 (463) 318-9850');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Willi', 'Maffin', 'wmaffin23@typepad.com', 'Female', '39457 Sunbrook Terrace', null, '+1 (312) 708-5127');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Nikolaos', 'Ivashintsov', 'nivashintsov24@hostgator.com', 'Male', '46318 Hauk Way', '993 Lakewood Parkway', '+86 (698) 199-3098');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Valdemar', 'Tunaclift', 'vtunaclift25@umn.edu', 'Male', '335 Glendale Court', null, '+63 (665) 806-2237');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Heall', 'Tumasian', 'htumasian26@intel.com', 'Male', '759 Shopko Way', null, '+33 (922) 454-9744');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Roderic', 'Mourbey', 'rmourbey27@xing.com', 'Male', '336 Nobel Crossing', null, '+351 (722) 935-0164');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Lindsay', 'Golbourn', 'lgolbourn28@is.gd', 'Male', '8 Sauthoff Parkway', null, '+63 (912) 595-5432');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Darius', 'Anfosso', 'danfosso29@creativecommons.org', 'Male', '42 Kipling Junction', '14 Mayfield Place', '+264 (771) 232-6088');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Donia', 'McKomb', 'dmckomb2a@quantcast.com', 'Female', '885 Granby Crossing', null, '+351 (411) 510-6548');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Ellynn', 'Spur', 'espur2b@phoca.cz', 'Female', '5 Dexter Parkway', '6193 Pawling Park', '+351 (163) 868-9169');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Giselbert', 'Evens', 'gevens2c@google.es', 'Male', '76 Park Meadow Alley', '7 Swallow Way', '+63 (381) 906-2527');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Adolphe', 'Abelovitz', 'aabelovitz2d@ifeng.com', 'Male', '25 Hanover Parkway', '34 Kingsford Hill', '+351 (981) 935-0545');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Simone', 'Jindra', 'sjindra2e@go.com', 'Male', '16 Dunning Park', null, '+504 (254) 774-3374');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Stephan', 'Duddan', 'sduddan2f@example.com', 'Male', '2578 Mccormick Pass', null, '+689 (247) 861-5082');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Betteanne', 'Keaves', 'bkeaves2g@ameblo.jp', 'Female', '5 Briar Crest Way', '38544 Grover Avenue', '+63 (707) 540-1474');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Grata', 'Asquez', 'gasquez2h@google.com.hk', 'Female', '04 Kinsman Trail', null, '+86 (770) 767-7599');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Stephen', 'Geertje', 'sgeertje2i@accuweather.com', 'Male', '8944 Fairfield Way', null, '+86 (881) 434-4801');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Teddi', 'Kruschev', 'tkruschev2j@com.com', 'Female', '37 Schmedeman Hill', null, '+62 (466) 297-0495');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Rolland', 'Witterick', 'rwitterick2k@ucsd.edu', 'Male', '7 Texas Terrace', '2 Badeau Road', '+351 (235) 176-6928');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Nicola', 'Arnull', 'narnull2l@themeforest.net', 'Female', '5025 Service Center', null, '+7 (957) 813-3355');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Layton', 'Ashcroft', 'lashcroft2m@skyrock.com', 'Male', '147 Rowland Terrace', '8266 Claremont Court', '+420 (285) 619-8018');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Brenden', 'Mollene', 'bmollene2n@tmall.com', 'Male', '5 Northfield Street', null, '+1 (214) 587-5952');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Skipp', 'Tregenza', 'stregenza2o@nsw.gov.au', 'Male', '801 Merry Terrace', null, '+62 (762) 872-9821');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Cornall', 'Van den Velden', 'cvandenvelden2p@cam.ac.uk', 'Male', '7934 6th Road', null, '+62 (233) 368-4205');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Koressa', 'Kwietek', 'kkwietek2q@guardian.co.uk', 'Female', '205 Farwell Drive', null, '+55 (784) 680-8865');
insert into customer (first_name, last_name, email, gender, address, billing_address, phone) values ('Ariana', 'O''Downe', 'aodowne2r@tiny.cc', 'Female', '68 Donald Terrace', '302 Carberry Pass', '+86 (456) 959-5511');
