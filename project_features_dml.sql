-- DML FOR PROJECT FEATURES
-- 1. Add, update, and delete a food review (on a food establishment or a food item);
-- Add a food review on a food establisment or a food item, assumming there are
-- variables for these values. Either can be, depending on the id given.
-- Establishment id or food id are NULL by default
INSERT INTO
    foodreview (
        reviewid,
        rating,
        datecreated,
        establishmentid,
        userid
    )
VALUES
    (
        review_id,
        rating,
        CURDATE(),
        establishment_id,
        user_id
    );

INSERT INTO
    foodreview (
        reviewid,
        rating,
        datecreated,
        foodid,
        userid
    )
VALUES
    (
        review_id,
        rating,
        CURDATE(),
        foodid,
        user_id
    );

-- Update a food review on a food establishment or food item, review id is given 
-- and assumming there are variables for these values.
-- Update rating
UPDATE foodreview
SET
    rating = new_rating
WHERE
    reviewid = review_id;

-- Update review
UPDATE foodreview
SET
    review = new_review
WHERE
    reviewid = review_id;

-- Update rating and review
UPDATE foodreview
SET
    rating = new_rating,
    review = new_review
WHERE
    reviewid = review_id;

-- Delete a food review on a food establishment or food item, review id is given.
DELETE FROM foodreview
WHERE
    reviewid = review_id;

-- 2. Add, delete, search, and update a food establishment;
-- Add a food establishment, assumming there are variables for these values.
-- Average rating is NULL by default
INSERT INTO
    foodestablishment (establishmentid, establishmentname, establishmentlocation)
VALUES
    (
        establishment_id,
        establishment_name,
        establishment_location
    );

-- Delete a food establishment
DELETE FROM foodestablishment
WHERE
    establishmentid = establishment_id;

-- Search for a food establishment
SELECT
    establishmentid,
    establishmentname,
    establishmentlocation,
    averagerating
FROM
    foodestablishment
WHERE
    establishmentid = establishment_id;

-- Update a food establishment, establishment id is given. 
-- Assumming there are variables for these values. 
-- Update establishment name
UPDATE foodestablishment
SET
    establishmentname = new_name
WHERE
    establishmentid = establishment_id;

-- Update location
UPDATE foodestablishment
SET
    establishmentlocation = new_location
WHERE
    establishmentid = establishment_id;

-- Update average rating
UPDATE foodestablishment
SET
    averagerating = new_average_rating
WHERE
    establishmentid = establishment_id;

-- 3. Add, delete, search, and update a food item
-- Add a food item, assumming there are variables for these values.
-- Average rating is NULL by default
INSERT INTO
    fooditem (foodid, foodname, foodtype, price, establishmentid)
VALUES
    (
        food_id,
        food_name,
        food_type,
        food_price,
        establishment_id
    );

-- Delete a food item
DELETE FROM fooditem
WHERE
    foodid = food_id;

-- Search for a food item
SELECT
    foodid,
    foodname,
    foodtype,
    price,
    establishmentid
FROM
    fooditem
WHERE
    foodid = food_id;

-- Update a food item, food id is given. 
-- Assumming there are variables for these values. 
-- Update food name
UPDATE fooditem
SET
    foodname = new_name
WHERE
    foodid = food_id;

-- Update food type
UPDATE fooditem
SET
    foodtype = new_food_type
WHERE
    foodid = food_id;

-- Update price
UPDATE fooditem
SET
    price = new_price
WHERE
    foodid = food_id;