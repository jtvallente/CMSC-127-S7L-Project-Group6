-- DML FOR PROJECT FEATURES
-- 1. Add, update, and delete a food review (on a food establishment or a food item);
-- Add a food review on a food establisment or a food item, assumming there are
-- variables for these values. Either can be, dependeng if item id is given.
-- Food id are NULL by default
INSERT INTO
    FoodReview (
        review_id,
        user_id,
        establishment_id,
        review_text,
        rating,
        review_month,
        review_day,
        review_year
    )
VALUES
    (
        review_id,
        user_id,
        establishment_id,
        review_text,
        rating,
        MONTH (CURDATE ()),
        DAY (CURDATE ()),
        YEAR (CURDATE ()),
    );

INSERT INTO
    FoodReview (
        review_id,
        user_id,
        establishment_id,
        item_id,
        review_text,
        rating,
        review_month,
        review_day,
        review_year
    )
VALUES
    (
        review_id,
        user_id,
        establishment_id,
        item_id,
        review_text,
        rating,
        MONTH (CURDATE ()),
        DAY (CURDATE ()),
        YEAR (CURDATE ()),
    );

-- Update a food review on a food establishment or food item, review id is given 
-- and assumming there are variables for these values.
-- Update rating
UPDATE FoodReview
SET
    rating = new_rating
WHERE
    review_id = review_id;

-- Update review
UPDATE FoodReview
SET
    review_text = new_review_text
WHERE
    review_id = review_id;

-- Update rating and review
UPDATE FoodReview
SET
    rating = new_rating,
    review_text = new_review_text
WHERE
    review_id = review_id;

-- Delete a food review on a food establishment or food item, review id is given.
DELETE FROM FoodReview
WHERE
    review_id = review_id;

-- 2. Add, delete, search, and update a food establishment;
-- Add a food establishment, assumming there are variables for these values.
-- Average rating is NULL by default
INSERT INTO
    FoodEstablishment (
        establishment_id,
        name,
        street_address,
        city,
        province
    )
VALUES
    (
        establishment_id,
        establishment_name,
        street_address,
        city,
        province
    );

-- Delete a food establishment
DELETE FROM FoodEstablishment
WHERE
    establishment_id = establishment_id;

-- Search for a food establishment
SELECT
    establishment_id,
    name,
    street_address,
    city,
    province,
    rating
FROM
    FoodEstablishment
WHERE
    establishment_id = establishment_id;

-- Update a food establishment, establishment id is given. 
-- Assumming there are variables for these values. 
-- Update establishment name
UPDATE FoodEstablishment
SET
    name = new_name
WHERE
    establishment_id = establishment_id;

-- Update location
UPDATE FoodEstablishment
SET
    street_address = new_street_address,
    city = new_city,
    province = new_province
WHERE
    establishment_id = establishment_id;

-- Update average rating
UPDATE FoodEstablishment
SET
    rating = new_rating
WHERE
    establishment_id = establishment_id;

-- 3. Add, delete, search, and update a food item
-- Add a food item, assumming there are variables for these values.
-- Average rating is NULL by default
INSERT INTO
    FoodItem (item_id, food_name, type, price, establishment_id)
VALUES
    (
        item_id,
        food_name,
        food_type,
        food_price,
        establishment_id
    );

-- Delete a food item
DELETE FROM FoodItem
WHERE
    item_id = item_id;

-- Search for a food item
SELECT
    item_id,
    food_name,
    type,
    price,
    establishment_id
FROM
    FoodItem
WHERE
    item_id = item_id;

-- Update a food item, food id is given. 
-- Assumming there are variables for these values. 
-- Update food name
UPDATE FoodItem
SET
    food_name = new_name
WHERE
    item_id = item_id;

-- Update food type
UPDATE FoodItem
SET
    type = new_food_type
WHERE
    item_id = item_id;

-- Update price
UPDATE FoodItem
SET
    price = new_price
WHERE
    item_id = item_id;