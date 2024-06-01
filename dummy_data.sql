INSERT INTO `FoodEstablishment` (`establishment_id`, `name`, `street_address`, `city`, `province`) VALUES
('ESTAB001', 'Happy Meals', '123 Food St.', 'Foodville', 'FV'),
('ESTAB002', 'Veggie Delight', '456 Green Rd.', 'Green City', 'GC'),
('ESTAB003', 'Meat Lovers', '789 Steak Ave.', 'Meat Town', 'MT'),
('ESTAB004', 'Healthy Bites', '101 Healthy Blvd.', 'Health City', 'HC'),
('ESTAB005', 'Quick Snacks', '202 Fast Ln.', 'Snackville', 'SV');

INSERT INTO `Users` (`user_id`, `username`, `password`, `role`) VALUES
('BUSIN001AA', 'john_doe', 'pass1', 'business_owner'),
('BUSIN002BB', 'jane_smith', 'pass2', 'business_owner'),
('BUSIN003CC', 'mike_jones', 'pass3', 'business_owner'),
('BUSIN004DD', 'sarah_lee', 'pass4', 'business_owner'),
('BUSIN005EE', 'tom_brown', 'pass5', 'business_owner'),
('CUSTO001AA', 'alice_w', 'pass6', 'customer'),
('CUSTO002BB', 'bob_k', 'pass7', 'customer'),
('CUSTO003CC', 'charlie_r', 'pass8', 'customer'),
('CUSTO004DD', 'david_m', 'pass9', 'customer'),
('CUSTO005EE', 'eva_n', 'pass10', 'customer');

INSERT INTO `FoodItem` (`item_id`, `establishment_id`, `food_name`, `price`, `type`) VALUES
('ITEM001', 'ESTAB001', 'Burger', 299.00, 'meat'),
('ITEM002', 'ESTAB001', 'Fries', 99.00, 'veg'),
('ITEM003', 'ESTAB002', 'Salad', 149.00, 'veg'),
('ITEM004', 'ESTAB003', 'Steak', 799.00, 'meat'),
('ITEM005', 'ESTAB004', 'Smoothie', 199.00, 'etc.');

INSERT INTO `FoodReview` (`review_id`, `user_id`, `establishment_id`, `item_id`, `review_text`, `rating`, `review_month`, `review_day`, `review_year`) VALUES
('REVIEW001', 'CUSTO001AA', 'ESTAB001', 'ITEM001', 'Great burger!', 5, 5, 10, 2024),
('REVIEW002', 'CUSTO002BB', 'ESTAB002', 'ITEM003', 'Fresh salad.', 4, 4, 12, 2024),
('REVIEW003', 'CUSTO003CC', 'ESTAB003', 'ITEM004', 'Perfectly cooked steak.', 5, 3, 15, 2024),
('REVIEW004', 'CUSTO004DD', 'ESTAB004', 'ITEM005', 'Delicious smoothie!', 4, 2, 20, 2024),
('REVIEW005', 'CUSTO005EE', 'ESTAB001', 'ITEM002', 'Crispy fries.', 4, 1, 25, 2024);

INSERT INTO `BusinessOwner` (`user_id`, `establishment_id`) VALUES
('BUSIN001AA', 'ESTAB001'),
('BUSIN002BB', 'ESTAB002'),
('BUSIN003CC', 'ESTAB003'),
('BUSIN004DD', 'ESTAB004'),
('BUSIN005EE', 'ESTAB005');

INSERT INTO `Customer` (`user_id`) VALUES
('CUSTO001AA'),
('CUSTO002BB'),
('CUSTO003CC'),
('CUSTO004DD'),
('CUSTO005EE');
