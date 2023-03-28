CREATE DATABASE IF NOT EXISTS review DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use review;

create table review (
    review_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    customer_id INT NOT NULL,
    activity_id INT NOT NULL,
    rating INT NOT NULL,
    review_text VARCHAR(255) NOT NULL,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- creating review table END --

-- inserting mock reviews START --

INSERT INTO review (customer_id, activity_id, rating, review_text)
VALUES
  (2, 1, 4, 'The airplane tour was amazing! The pilot was very knowledgeable and gave us a great tour of the city from the sky.'),
  (1, 2, 3, 'The cycling tour was good, but the bikes could have been in better condition.'),
  (5, 3, 4, 'Dune bashing was such a thrilling experience! The driver was really skilled and made us feel safe.'),
  (1, 4, 5, 'Glamping was a unique experience that we thoroughly enjoyed. The tents were spacious and comfortable, and the campfire under the stars was magical.'),
  (8, 5, 4, 'The golf course was beautiful and well-maintained. We had a great time playing.'),
  (4, 6, 3, 'Kite surfing was harder than we expected, but the instructor was very patient and helpful.'),
  (7, 4, 4, "The museum tour was very informative and well-organized. We learned a lot about the city\'s history."),
  (10, 8, 3, 'Paintball was fun, but the equipment could have been better.'),
  (20, 9, 5, 'Shark cage diving was an incredible experience! We saw so many different species of sharks up close.'),
  (15, 10, 4, 'Ziplining was a great way to get an adrenaline rush while taking in the beautiful views.'),
  (23, 11, 4, 'Jet skiing was a blast! The water was perfect and we had a great time.'),
  (13, 12, 3, 'Windsurfing was harder than it looked, but the instructor was very patient.'),
  (17, 13, 5, 'Stand-up paddleboarding was a relaxing and enjoyable way to explore the beautiful coastline.'),
  (18, 14, 4, 'Swimming with sharks was an unforgettable experience. It was incredible to be so close to these amazing creatures.'),
  (16, 15, 4, 'Tandem paragliding was a thrilling experience! The views from up high were absolutely breathtaking.'),
  (24, 16, 4, 'The theme park rides were so much fun! There were rides for all ages and we had a blast.'),
  (11, 17, 4, 'The tree top adventures course was challenging, but we had a great time navigating through the obstacles.');
  (15, 3, 4, 'The guided city walking tour was a great way to see the sights and learn about the history of the city. The guide was very knowledgeable.')
(7, 8, 5, 'The snorkeling excursion was amazing! We saw so many colorful fish and the water was crystal clear.')
(22, 1, 3, 'The airplane tour was a bit too short for my liking, but the pilot was very skilled and gave us a great view of the city.')
(31, 5, 2, 'The hiking trail was not well-maintained and we had a difficult time finding the trailhead. The views were nice once we got there though.')
(9, 4, 5, 'The museum tour was excellent! The exhibits were very interesting and the guide was very passionate about the history.')
(26, 10, 4, 'The wine tasting was a great experience. The selection was fantastic and the staff were very friendly and informative.')
(13, 6, 3, 'The beach was beautiful, but it was a bit crowded and noisy.')
(19, 2, 5, 'The hot air balloon ride was absolutely amazing! The views were breathtaking and the pilot was very friendly.')
(2, 11, 2, "The amusement park was very crowded and the lines were extremely long. We didn't have much fun.")
(35, 7, 4, 'The zoo was a great place to spend the afternoon. The animals were well-cared for and the exhibits were very informative.')
(20, 12, 5, 'The boat tour was fantastic! We saw so many beautiful sights and the guide was very knowledgeable.')
(27, 9, 3, 'The food tour was interesting, but some of the stops were a bit underwhelming.')
(10, 3, 5, 'The city bike tour was one of the best parts of our trip! The guide was very friendly and took us to some great hidden spots.')
(16, 1, 4, 'The helicopter tour was amazing! We got to see so many beautiful sights and the pilot was very skilled.')
(33, 5, 2, 'The hiking trail was very difficult and we had a hard time finding our way. The views were nice though.')
(4, 4, 3, 'The museum was interesting, but some of the exhibits were a bit outdated.')
(28, 10, 5, 'The wine tasting was a great experience! The selection was fantastic and the staff were very knowledgeable.')
(14, 6, 4, 'The beach was beautiful and the water was perfect for swimming. It was a bit crowded though.')
(21, 2, 3, 'The hot air balloon ride was a bit too short for my liking, but the views were still very beautiful.')
(38, 11, 2, "The amusement park was very crowded and the lines were extremely long. It wasn't worth the money in my opinion.")