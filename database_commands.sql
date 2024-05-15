-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS food_review_db;

-- Use the created database
USE food_review_db;

-- Create table 'users'
CREATE TABLE IF NOT EXISTS Users (
    user_id VARCHAR(36) PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(25) NOT NULL,
    role ENUM('business_owner', 'customer') NOT NULL
);

-- Table: BusinessOwner (Subclass)
CREATE TABLE IF NOT EXISTS BusinessOwner (
    user_id VARCHAR(36) PRIMARY KEY,
    establishment_id VARCHAR(36) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (establishment_id) REFERENCES FoodEstablishment(establishment_id) ON DELETE CASCADE
);


-- Table: Customer (Subclass)
CREATE TABLE IF NOT EXISTS Customer (
    user_id VARCHAR(36) PRIMARY KEY,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Table: FoodEstablishment
CREATE TABLE IF NOT EXISTS FoodEstablishment (
    establishment_id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    street_address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    province VARCHAR(50) NOT NULL,
);

-- Table: FoodItem
CREATE TABLE IF NOT EXISTS FoodItem (
    item_id VARCHAR(36) PRIMARY KEY,
    establishment_id VARCHAR(36)  NOT NULL,
    food_name VARCHAR(100) NOT NULL,
    price DECIMAL(8, 2) NOT NULL,
    type ENUM('meat', 'veg', 'etc.') NOT NULL,
    FOREIGN KEY (establishment_id) REFERENCES FoodEstablishment(establishment_id) ON DELETE CASCADE
);

-- Table: FoodReview
CREATE TABLE IF NOT EXISTS FoodReview (
    review_id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    establishment_id VARCHAR(36) NOT NULL,
    item_id VARCHAR(36) NULL,
    review_text TEXT NOT NULL,
    rating TINYINT UNSIGNED NOT NULL,
    review_month TINYINT NOT NULL,
    review_day TINYINT NOT NULL,
    review_year SMALLINT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (establishment_id) REFERENCES FoodEstablishment(establishment_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES FoodItem(item_id) ON DELETE CASCADE
);

INSERT INTO Users (user_id, username, password, role) 
VALUES ('2021-67857', 'jtvallente', 'gno8fsbhrtx', 'customer');

INSERT INTO Users (user_id, username, password, role) 
VALUES ('2021-00234', 'aglicup', 'gno3fsafg', 'business_owner');

INSERT INTO Users (user_id, username, password, role) 
VALUES ('2022-67845', 'ctrojano', 'abcdefgh', 'customer');
