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

