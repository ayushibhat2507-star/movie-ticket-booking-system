

DROP TABLE IF EXISTS `lang`;
CREATE TABLE `lang` (
  `lang` varchar(15) DEFAULT NULL,
  `mcode` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `lang` VALUES ('Hindi', 1);
INSERT INTO `lang` VALUES ('Hindi', 2);
INSERT INTO `lang` VALUES ('Hindi', 3);
INSERT INTO `lang` VALUES ('Hindi', 4);
INSERT INTO `lang` VALUES ('Hindi', 5);
INSERT INTO `lang` VALUES ('Hindi', 6);
INSERT INTO `lang` VALUES ('Hindi', 8);
INSERT INTO `lang` VALUES ('Hindi', 9);
INSERT INTO `lang` VALUES ('Hindi', 14);
INSERT INTO `lang` VALUES ('Hindi', 15);
INSERT INTO `lang` VALUES ('Hindi', 18);
INSERT INTO `lang` VALUES ('Hindi', 19);
INSERT INTO `lang` VALUES ('Hindi', 27);
INSERT INTO `lang` VALUES ('English', 2);
INSERT INTO `lang` VALUES ('English', 4);
INSERT INTO `lang` VALUES ('English', 5);
INSERT INTO `lang` VALUES ('English', 6);
INSERT INTO `lang` VALUES ('English', 8);
INSERT INTO `lang` VALUES ('English', 11);
INSERT INTO `lang` VALUES ('English', 13);
INSERT INTO `lang` VALUES ('English', 14);
INSERT INTO `lang` VALUES ('English', 15);
INSERT INTO `lang` VALUES ('English', 16);
INSERT INTO `lang` VALUES ('English', 17);
INSERT INTO `lang` VALUES ('English', 18);
INSERT INTO `lang` VALUES ('English', 19);
INSERT INTO `lang` VALUES ('English', 20);
INSERT INTO `lang` VALUES ('English', 21);
INSERT INTO `lang` VALUES ('English', 23);
INSERT INTO `lang` VALUES ('English', 24);
INSERT INTO `lang` VALUES ('English', 25);
INSERT INTO `lang` VALUES ('English', 26);
INSERT INTO `lang` VALUES ('English', 29);
INSERT INTO `lang` VALUES ('English', 30);
INSERT INTO `lang` VALUES ('Tamil', 2);
INSERT INTO `lang` VALUES ('Tamil', 3);
INSERT INTO `lang` VALUES ('Tamil', 4);
INSERT INTO `lang` VALUES ('Tamil', 5);
INSERT INTO `lang` VALUES ('Tamil', 8);
INSERT INTO `lang` VALUES ('Tamil', 12);
INSERT INTO `lang` VALUES ('Tamil', 15);
INSERT INTO `lang` VALUES ('Tamil', 22);
INSERT INTO `lang` VALUES ('Telugu', 2);
INSERT INTO `lang` VALUES ('Telugu', 3);
INSERT INTO `lang` VALUES ('Telugu', 4);
INSERT INTO `lang` VALUES ('Telugu', 5);
INSERT INTO `lang` VALUES ('Telugu', 8);
INSERT INTO `lang` VALUES ('Telugu', 12);
INSERT INTO `lang` VALUES ('Telugu', 15);
INSERT INTO `lang` VALUES ('Telugu', 22);
INSERT INTO `lang` VALUES ('Punjabi', 4);
INSERT INTO `lang` VALUES ('Punjabi', 7);
INSERT INTO `lang` VALUES ('Assamese', 10);
INSERT INTO `lang` VALUES ('Korean', 28);
INSERT INTO `lang` VALUES ('Urdu', 19);


DROP TABLE IF EXISTS `mallt`;
CREATE TABLE `mallt` (
  `Mno` int(11) DEFAULT NULL,
  `mall` varchar(55) DEFAULT NULL,
  `cancel` varchar(30) DEFAULT NULL,
  `time` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `mallt` VALUES (1, 'PVR: Pacific,Dwarka', 'cancellation available', '1:25 PM,7:10 PM');
INSERT INTO `mallt` VALUES (2, 'INOX: Nehru Place', 'non-cancellable', '4:35 PM');
INSERT INTO `mallt` VALUES (3, 'Cinepolis: Unity One Mall Rohini,Delhi', 'non-cancellable', '12:55 PM');
INSERT INTO `mallt` VALUES (4, 'PVR: Select City Walk,Delhi', 'cancellation available', '8:40 PM,11:45 PM');
INSERT INTO `mallt` VALUES (5, 'Movie Max: Gulshan Noida', 'cancellation available', '4:15 PM');
INSERT INTO `mallt` VALUES (6, 'US CINEMAS: Galaxy Blue Sapphire,Noida Ext', 'non-cancellable', '4:40 PM');
INSERT INTO `mallt` VALUES (7, 'PVR: Logix,Noida', 'cancellation available', '1:35 PM,9:55 PM');
INSERT INTO `mallt` VALUES (8, 'Cinepolis: DLF Avenue,Saket', 'non-cancellable', '12:45 PM');
INSERT INTO `mallt` VALUES (9, 'PVR: Vegas,Dwarka', 'cancellation available', '4:35 PM,10:40 PM');
INSERT INTO `mallt` VALUES (10, 'PVR: Gaur City,Greater Noida', 'cancellation available', '7:30 PM');


DROP TABLE IF EXISTS `mallto`;
CREATE TABLE `mallto` (
  `Mno` int(11) DEFAULT NULL,
  `mall` varchar(55) DEFAULT NULL,
  `cancel` varchar(30) DEFAULT NULL,
  `time` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `mallto` VALUES (1, 'Movie Max: Pacific Mall Ghaziabad', 'cancellation available', '4:00 PM');
INSERT INTO `mallto` VALUES (2, 'PVR: Mahagun,Ghaziabad', 'cancellation available', '7:50 PM,10:55 PM');
INSERT INTO `mallto` VALUES (3, 'PVR: VVIP,Ghaziabad', 'cancellation available', '9:50 PM');
INSERT INTO `mallto` VALUES (4, 'US Cinemas: Aditya Mall,Indirapuram', 'non-cancellable', '7:15 PM');
INSERT INTO `mallto` VALUES (5, 'Wave Cinemas: Gaur Central Mall,RDC', 'cancellation available', '4:35 PM');
INSERT INTO `mallto` VALUES (6, 'US Cinemas: EROS Mall,Indirapuram', 'non-cancellable', '4:20 PM');
INSERT INTO `mallto` VALUES (7, 'Wave: The Wave Mall,Kaushambi', 'cancellation available', '4:20 PM');
INSERT INTO `mallto` VALUES (8, 'PVR: EDM,Ghaziabad', 'cancellation available', '3:55 PM,9:50 PM');
INSERT INTO `mallto` VALUES (9, 'Galaxie Multiplex: Ghaziabad', 'cancellation available', '3:00 PM,5:45 PM');
INSERT INTO `mallto` VALUES (10, 'Miraj Cinemas: M4U,Sahibabad', 'cancellation available', '4:45 PM');


DROP TABLE IF EXISTS `meal`;
CREATE TABLE `meal` (
  `No` int(11) DEFAULT NULL,
  `Item` varchar(100) DEFAULT NULL,
  `Price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `meal` VALUES (1, 'Regular popcorn', 55);
INSERT INTO `meal` VALUES (2, 'Veg Sandwich', 65);
INSERT INTO `meal` VALUES (3, 'Cheese popcorn', 85);
INSERT INTO `meal` VALUES (4, 'Pepsi', 55);
INSERT INTO `meal` VALUES (5, 'Hot Coffee', 40);
INSERT INTO `meal` VALUES (6, 'Veg burger', 75);
INSERT INTO `meal` VALUES (7, 'Hot tea', 35);
INSERT INTO `meal` VALUES (8, 'French fries', 55);
INSERT INTO `meal` VALUES (9, 'Nachos', 95);
INSERT INTO `meal` VALUES (10, 'Masala fries', 70);
INSERT INTO `meal` VALUES (11, 'Veg pasta', 100);
INSERT INTO `meal` VALUES (12, 'Combo 1: 1 large popcorn+2 large pepsi', 350);
INSERT INTO `meal` VALUES (13, 'Combo 2: 1 large popcorn+French fries+Large pepsi', 230);
INSERT INTO `meal` VALUES (14, 'Combo 3: 1 Veg burger+Small pepsi', 230);
INSERT INTO `meal` VALUES (15, 'Combo 4: Nachos+Pepsi', 250);
INSERT INTO `meal` VALUES (16, 'Combo 5: Small popcorn + Masala fries + Hot coffee', 420);
INSERT INTO `meal` VALUES (17, 'Combo 6: Large popcorn + 2 Veg burgers + 2 Small pepsi + Veg sandwich', 660);


DROP TABLE IF EXISTS `movies`;
CREATE TABLE `movies` (
  `Name` varchar(50) DEFAULT NULL,
  `genre` varchar(15) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `mcode` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `movies` VALUES ('Zara Hatke Zara Bachke', 'drama', 7.5, 1);
INSERT INTO `movies` VALUES ('Transformers:Rise of the Beasts', 'sci-fi', 8.8, 2);
INSERT INTO `movies` VALUES ('The Kerala Story', 'drama', 8.8, 3);
INSERT INTO `movies` VALUES ('Spider-Man:Across The Spider-Verse', 'animation', 9.4, 4);
INSERT INTO `movies` VALUES ('Fast X', 'thriller', 8.7, 5);
INSERT INTO `movies` VALUES ('The Little Mermaid', 'fantasy', 7.3, 6);
INSERT INTO `movies` VALUES ('Godday Godday Chaa', 'comedy', 8.9, 7);
INSERT INTO `movies` VALUES ('Guardians of the Galaxy Vol. 3', 'sci-fi', 8.9, 8);
INSERT INTO `movies` VALUES ('IB71', 'thriller', 8.4, 9);
INSERT INTO `movies` VALUES ('Sri Raghupati', 'action', 9.6, 10);
INSERT INTO `movies` VALUES ('The House of Dead Horror', 'horror', 5.9, 11);
INSERT INTO `movies` VALUES ('Custody', 'thriller', 6.9, 12);
INSERT INTO `movies` VALUES ('Ghosted', 'romance', 5.8, 13);
INSERT INTO `movies` VALUES ('The Super Mario Bros.Movie', 'animation', 9.1, 14);
INSERT INTO `movies` VALUES ('John Wick: Chapter 4', 'crime', 7.9, 15);
INSERT INTO `movies` VALUES ('Killers of the Flower Moon', 'history', 9.4, 16);
INSERT INTO `movies` VALUES ('Nefarious', 'mystery', 6.3, 17);
INSERT INTO `movies` VALUES ('Extraction 2', 'action', 8.1, 18);
INSERT INTO `movies` VALUES ('Polite Society', 'comedy', 6.7, 19);
INSERT INTO `movies` VALUES ('The Secret Kingdom', 'fantasy', 4.7, 20);
INSERT INTO `movies` VALUES ('Mending the Line', 'drama', 7.0, 21);
INSERT INTO `movies` VALUES ('Takkar', 'drama', 8.8, 22);
INSERT INTO `movies` VALUES ('The Boogeyman', 'horror', 6.1, 23);
INSERT INTO `movies` VALUES ('About My Father', 'comedy', 6.1, 24);
INSERT INTO `movies` VALUES ('You Hurt My Feelings', 'comedy', 7.2, 25);
INSERT INTO `movies` VALUES ('The Machine', 'adventure', 6.5, 26);
INSERT INTO `movies` VALUES ('Bloody Daddy', 'thriller', 7.3, 27);
INSERT INTO `movies` VALUES ('The Roundup: No Way Out', 'adventure', 6.8, 28);
INSERT INTO `movies` VALUES ('The Starling Girl', 'drama', 7.4, 29);
INSERT INTO `movies` VALUES ('We Have a Ghost', 'fantasy', 6.1, 30);
