-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS food_review_db;

-- Use the created database
USE food_review_db;

-- Create table 'users'
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    usertype ENUM('Owner', 'Customer') NOT NULL
);

INSERT INTO users (id, username, password, usertype)
VALUES (1, 'new_user', 'new_password', 'Customer');
