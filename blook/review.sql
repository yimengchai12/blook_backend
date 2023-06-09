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

CREATE TABLE pendingReview (
    num INT PRIMARY KEY AUTO_INCREMENT,
    customer_ID INT,
    activity_id INT
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
  (7, 4, 4, "The museum tour was very informative and well-organized. We learned a lot about the city's history."),
  (10, 8, 3, 'Paintball was fun, but the equipment could have been better.'),
  (20, 9, 5, 'Shark cage diving was an incredible experience! We saw so many different species of sharks up close.'),
  (15, 10, 4, 'Ziplining was a great way to get an adrenaline rush while taking in the beautiful views.'),
  (23, 11, 4, 'Jet skiing was a blast! The water was perfect and we had a great time.'),
  (13, 12, 3, 'Windsurfing was harder than it looked, but the instructor was very patient.'),
  (17, 13, 5, 'Stand-up paddleboarding was a relaxing and enjoyable way to explore the beautiful coastline.'),
  (18, 14, 4, 'Swimming with sharks was an unforgettable experience. It was incredible to be so close to these amazing creatures.'),
  (16, 15, 4, 'Tandem paragliding was a thrilling experience! The views from up high were absolutely breathtaking.'),
  (24, 16, 4, 'The theme park rides were so much fun! There were rides for all ages and we had a blast.'),
  (11, 17, 4, 'The tree top adventures course was challenging, but we had a great time navigating through the obstacles.'),
  (15, 3, 4, 'The guided city walking tour was a great way to see the sights and learn about the history of the city. The guide was very knowledgeable.'),
  (7, 8, 5, 'The snorkeling excursion was amazing! We saw so many colorful fish and the water was crystal clear.'),
(22, 1, 3, 'The airplane tour was a bit too short for my liking, but the pilot was very skilled and gave us a great view of the city.'),
(31, 5, 2, 'The hiking trail was not well-maintained and we had a difficult time finding the trailhead. The views were nice once we got there though.'),
(9, 4, 5, 'The museum tour was excellent! The exhibits were very interesting and the guide was very passionate about the history.'),
(26, 10, 4, 'The wine tasting was a great experience. The selection was fantastic and the staff were very friendly and informative.'),
(13, 6, 3, 'The beach was beautiful, but it was a bit crowded and noisy.'),
(19, 2, 5, 'The hot air balloon ride was absolutely amazing! The views were breathtaking and the pilot was very friendly.'),
(2, 11, 2, 'The amusement park was very crowded and the lines were extremely long. We didnt have much fun.'),
(35, 7, 4, 'The zoo was a great place to spend the afternoon. The animals were well-cared for and the exhibits were very informative.'),
(20, 12, 5, 'The boat tour was fantastic! We saw so many beautiful sights and the guide was very knowledgeable.'),
(27, 9, 3, 'The food tour was interesting, but some of the stops were a bit underwhelming.'),
(10, 3, 5, 'The city bike tour was one of the best parts of our trip! The guide was very friendly and took us to some great hidden spots.'),
(16, 1, 4, 'The helicopter tour was amazing! We got to see so many beautiful sights and the pilot was very skilled.'),
(33, 5, 2, 'The hiking trail was very difficult and we had a hard time finding our way. The views were nice though.'),
(4, 4, 3, 'The museum was interesting, but some of the exhibits were a bit outdated.'),
(28, 10, 5, 'The wine tasting was a great experience! The selection was fantastic and the staff were very knowledgeable.'),
(14, 6, 4, 'The beach was beautiful and the water was perfect for swimming. It was a bit crowded though.'),
(21, 2, 3, 'The hot air balloon ride was a bit too short for my liking, but the views were still very beautiful.'),
(38, 11, 2, 'The amusement park was very crowded and the lines were extremely long. It wasnt worth the money in my opinion.'),
(14, 5, 3, 'The hiking trail was challenging but worth it! We saw some amazing views along the way and felt a great sense of accomplishment. Overall, a good experience,'),
(22, 1, 5, 'The airplane tour was an incredible experience! We got to see the city from a whole new perspective, and the pilot was very skilled and knowledgeable. Highly recommend,'),
(5, 10, 2, 'The wine tasting was disappointing. The selection was limited and the staff seemed uninterested in helping us. Not worth the price,'),
(35, 4, 4, 'The museum had a great collection of artifacts and exhibits! The information provided was very interesting and informative, and we learned a lot. Would visit again,'),
(19, 8, 5, 'The snorkeling excursion was the highlight of our trip! The water was clear and we saw some amazing marine life up close. The guides were also very friendly and knowledgeable,'),
(29, 7, 3, 'The zoo was a decent way to spend the afternoon. The animals seemed well-cared for, but some of the exhibits were a bit outdated. Overall, a decent experience,'),
(2, 12, 4, 'The boat tour was a great way to see the city from a different perspective! The guide was very informative and we got to see some beautiful sights along the way,'),
(12, 6, 3, 'The beach was crowded and noisy, but the water was still beautiful and refreshing. Not the best beach weve been to, but still a decent way to spend the day'),
(30, 3, 5, 'The guided city walking tour was amazing! Our guide was very knowledgeable and showed us some hidden gems that we wouldnt have found otherwise. Highly recommend,'),
(16, 9, 2, 'The food tour was disappointing. The selection was limited and the portions were small. Not worth the price'),
(25, 1, 4, 'The helicopter tour was breathtaking! We got to see the city from a whole new perspective, and the pilot was very skilled and knowledgeable. Highly recommend'),
(7, 10, 5, 'The wine tasting was a great experience! The staff were very friendly and knowledgeable, and the selection was fantastic. Would definitely go again'),
(18, 2, 3, 'The hot air balloon ride was a bit too short for our liking, but the views were still beautiful. The pilot was also very friendly and informative'),
(33, 4, 4, 'The museum was very interesting! We learned a lot about the local history and culture, and the exhibits were well-curated. Highly recommend'),
(23, 5, 3, 'The hiking trail was challenging but rewarding! The views were stunning and we felt a great sense of accomplishment after completing the trail. Overall, a good experience'),
(11, 11, 4, 'The amusement park was a lot of fun! There were plenty of rides and attractions to keep us entertained, and the lines were not too long. Overall, a great experience'),
(38, 7, 3, 'The zoo was okay. Some of the exhibits seemed a bit cramped, but the animals seemed well-cared for. Not the best zoo weve been to, but still worth a visit'),
(27, 2, 4, 'The hot air balloon ride was a unique and memorable experience! The views were incredible and the pilot was very knowledgeable. Highly recommend'),
(8, 9, 2, 'The food tour was underwhelming. The selection was limited and the quality was not great. Not worth the price'),
(36, 3, 5, 'The guided city bike tour was fantastic! We got to see so much of the city and our guide was very knowledgeable and friendly. Highly recommend'),
(20, 11, 4, 'The amusement park had a great variety of rides and attractions! We had a lot of fun and would definitely visit again'),
(10, 12, 5, 'The boat tour was a highlight of our trip! The guide was very informative and we got to see some incredible sights. Highly recommend'),
(31, 6, 3, 'The beach was crowded and the water was a bit rough, but still a nice way to spend the day. Not the best beach weve been to, but still enjoyable'),
(13, 4, 4, 'The museum was very well-done! The exhibits were informative and engaging, and we learned a lot about the local history and culture. Highly recommend'),
(26, 1, 5, 'The helicopter tour was absolutely amazing! We got to see the city from a whole new perspective and the pilot was very skilled and informative. Highly recommend'),
(39, 10, 2, 'The wine tasting was a bit disappointing. The selection was limited and the staff seemed disinterested in helping us. Not worth the price'),
(24, 7, 3, 'The zoo was decent. Some of the animals seemed a bit bored or restless, but overall it was a decent way to spend the day. Not the best zoo weve been to, but still worth a visit'),
(40, 2, 4, 'The hot air balloon ride was an unforgettable experience! The views were breathtaking and the pilot was very skilled and knowledgeable. Highly recommend'),
(17, 11, 4, 'The amusement park was a lot of fun! There were plenty of rides and attractions to keep us entertained, and the staff were friendly and helpful. Highly recommend');




INSERT INTO pendingReview (customer_ID, activity_id)
VALUES 
  (1, 100),
  (1, 1),
  (1, 15),
  (2, 24),
  (2, 25),
  (6, 6)