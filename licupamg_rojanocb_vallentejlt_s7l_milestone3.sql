-- Milestone 3 - SQL
-- Section S-7L
-- Angelica Mae G. Licup
-- Christian B. Rojano
-- James Lourence T. Vallente

-- DDL FOR FOOD REVIEWS INFORMATION SYSTEM
-- Table: User (Superclass)
CREATE TABLE User (
    user_id VARCHAR(36) PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(25) NOT NULL,
    role ENUM('business_owner', 'customer') NOT NULL
);

-- Table: BusinessOwner (Subclass)
CREATE TABLE BusinessOwner (
    user_id VARCHAR(36) PRIMARY KEY,
    establishment_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE,
    FOREIGN KEY (establishment_id) REFERENCES FoodEstablishment(establishment_id) ON DELETE CASCADE
);

-- Table: Customer (Subclass)
CREATE TABLE Customer (
    user_id VARCHAR(36) PRIMARY KEY,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE
);

-- Table: FoodEstablishment
CREATE TABLE FoodEstablishment (
    establishment_id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    street_address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    province VARCHAR(50) NOT NULL,
);

-- Table: FoodItem
CREATE TABLE FoodItem (
    item_id VARCHAR(36) PRIMARY KEY,
    establishment_id INT NOT NULL,
    food_name VARCHAR(100) NOT NULL,
    price DECIMAL(8, 2) NOT NULL,
    type ENUM('meat', 'veg', 'etc.') NOT NULL,
    FOREIGN KEY (establishment_id) REFERENCES FoodEstablishment(establishment_id) ON DELETE CASCADE
);

-- Table: FoodReview
CREATE TABLE FoodReview (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    establishment_id INT NOT NULL,
    item_id INT NULL,
    review_text TEXT NOT NULL,
    rating TINYINT UNSIGNED NOT NULL,
    review_month TINYINT NOT NULL,
    review_day TINYINT NOT NULL,
    review_year SMALLINT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE,
    FOREIGN KEY (establishment_id) REFERENCES FoodEstablishment(establishment_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES FoodItem(item_id) ON DELETE CASCADE
);

-- DML FOR PROJECT FEATURES


-- DML FOR PROJECT REPORTS
-- 1. View all food establishments
SELECT * FROM FoodEstablishment;

-- 2. View all food reviews for an establishment or a food item;
-- View all food reviews for an establishment
SELECT * FROM FoodReview WHERE establishment_id=(SELECT establishment_id FROM FoodEstablishment WHERE name=name);

-- View all food reviews for a food item
SELECT * FROM FoodReview WHERE item_id=(SELECT item_id FROM FoodItem WHERE food_name=food_name);

-- 3. View all food items from an establishment;
SELECT * FROM FoodItem WHERE establishment_id=(SELECT establishment_id FROM FoodEstablishment WHERE name=name);

-- 4. View all food items from an establishment that belong to a food type (meat, veg, etc.);
SELECT * FROM FoodItem WHERE establishment_id=(SELECT establishment_id FROM FoodEstablishment WHERE name=name) AND type=type;

-- 5. View all reviews made within a month for an establishment or a food item;
-- View all reviews made within a month for an establishment
SELECT * FROM FoodReview WHERE establishment_id=(SELECT establishment_id FROM FoodEstablishment WHERE name=name) AND review_month=review_month;

-- View all reviews made within a month for a food item
SELECT * FROM FoodReview WHERE item_id=(SELECT item_id FROM FoodItem WHERE food_name=food_name) AND review_month=review_month;

-- 6. View all establishments with a high average rating (rating >= 4) (ratings from 1-5; highest is 5);
SELECT * FROM FoodEstablishment WHERE establishment_id=(SELECT establishment_id FROM FoodReview WHERE rating>=4);

-- 7. View all food items from an establishment arranged according to price; 
SELECT * FROM FoodItem WHERE establishment_id=(SELECT establishment_id FROM FoodEstablishment WHERE name=name) ORDER BY price ASC;

-- 8. Search food items from any establishment based on a given price range and/or food type;
SELECT * FROM FoodItem WHERE price IN (price, price) AND type=type;