import mysql.connector
from mysql.connector import Error
from colorama import Fore


# Create a connection to the database
def establish_server_connection(host_name, user_name, user_password, database_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name
        )
        print(Fore.GREEN + "Database connection successful!")
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return connection


# Checks if the username already exist
def check_username_exists(connection, user_name):
    cursor = connection.cursor()
    check_username = "SELECT EXISTS(SELECT 1 FROM Users WHERE username = %s LIMIT 1);"

    try:
        cursor.execute(check_username, (user_name,))
        result = cursor.fetchone()
        exists = result[0]
        if exists == 1:
            return True
        return False
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return False


# Add a food establishment in the database
def add_food_establishment_to_db(connection, establishment_id, name, street_address, city, province):
    cursor = connection.cursor()
    add_FE = "INSERT INTO FoodEstablishment (establishment_id, name, street_address, city, province) VALUES (%s, %s, %s, %s, %s);"
    FE_values = (establishment_id, name, street_address, city, province)

    try:
        cursor.execute(add_FE, FE_values)
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
        return False


# Add a food item in the database
def add_food_item(connection, item_id, establishment_id, food_name, price, type):
    cursor = connection.cursor()
    add_FI = "INSERT INTO FoodItem (item_id, establishment_id, food_name, price, type) VALUES (%s, %s, %s, %s, %s);"
    FI_values = (item_id, establishment_id, food_name, price, type)

    try:
        cursor.execute(add_FI, FI_values)
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return False


# Add a customer in the database
def add_customer(connection, user_id):
    cursor = connection.cursor()
    add_cust = "INSERT INTO customer (user_id) VALUES (%s);"
    
    try:
        cursor.execute(add_cust, (user_id,))
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
        
    return False


# Add a business owner in the database
def add_businessowner(connection, user_id, establishment_id):
    cursor = connection.cursor()
    add_BO = "INSERT INTO BusinessOwner (user_id, establishment_id) VALUES (%s, %s);"
    BO_values = (user_id, establishment_id)

    try:
        cursor.execute(add_BO, BO_values)
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
    
    return False


# Add a user in the database
def add_user(connection, user_id, username, password, role):
    cursor = connection.cursor()
    add_user = "INSERT INTO Users (user_id, username, password, role) VALUES (%s, %s, %s, %s);"
    user_values = (user_id, username, password, role)

    try:
        cursor.execute(add_user, user_values)
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
    
    return False


def add_food_review_db(connection, review_id, user_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year):
    cursor = connection.cursor()
    if item_id is None:
        add_FR = "INSERT INTO FoodReview (review_id, user_id, establishment_id, review_text, rating, review_month, review_day, review_year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        FR_values = (review_id, user_id, establishment_id, review_text, rating, review_month, review_day, review_year)
    else:
        add_FR = "INSERT INTO FoodReview (review_id, user_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        FR_values = (review_id, user_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year)

    try:
        cursor.execute(add_FR, FR_values)
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
        return False

# Delete a food review in the database
def delete_food_review(connection, review_id):
    cursor = connection.cursor()
    delete_FR = "DELETE FROM FoodReview WHERE review_id = %s;"
    FR_id = (review_id,)

    try:
        cursor.execute(delete_FR, FR_id)
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
    
    return False


# Delete a food establishment from the database
def delete_food_establishment(connection, establishment_id):
    cursor = connection.cursor()
    delete_FE = "DELETE FROM FoodEstablishment WHERE establishment_id = %s;"
    FE_id = (establishment_id,)
    
    try:
        cursor.execute(delete_FE, FE_id)
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
    
    return False


# Delete a food item from the database
def delete_food_item(connection, item_id):
    cursor = connection.cursor()
    delete_FI = "DELETE FROM FoodItem WHERE item_id = %s;"
    FI_id = (item_id,)
    
    try:
        cursor.execute(delete_FI, FI_id)
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
    
    return False

# Delete a user from the database
def delete_user(connection, user_id):
    cursor = connection.cursor()
    delete_user = "DELETE FROM Users WHERE user_id = %s;"
    userid = (user_id,)
    
    try:
        cursor.execute(delete_user, userid)
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
    
    return False


# Search for a food establishment in the database
def search_food_establishment(connection, establishment_id):
    cursor = connection.cursor(dictionary=True)
    food_estab = None
    search_FE = "SELECT establishment_id, name, street_address, city, province FROM FoodEstablishment WHERE establishment_id = %s LIMIT 1;"

    try:
        cursor.execute(search_FE, (establishment_id,))
        food_estab = cursor.fetchone()
        return food_estab
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return food_estab

#update a food review
def update_food_review(connection, review_id, new_review_text, new_rating):
    cursor = connection.cursor()
    update_query = "UPDATE FoodReview SET review_text = %s, rating = %s WHERE review_id = %s"
    values = (new_review_text, new_rating, review_id)

    try:
        cursor.execute(update_query, values)
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
        return False
    
#update a food item
def update_food_item(connection, item_id, new_name, new_price):
    cursor = connection.cursor()
    update_query = "UPDATE FoodItem SET food_name = %s, price = %s WHERE item_id = %s"
    values = (new_name, new_price, item_id)
    try:
        cursor.execute(update_query, values)
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
        return False

# Search for a food item in the database
def search_food_item(connection, item_id):
    cursor = connection.cursor(dictionary=True)
    food_itm = None
    search_FI = "SELECT item_id, establishment_id, food_name, price, type FROM FoodItem WHERE item_id = %s LIMIT 1);"

    try:
        cursor.execute(search_FI, (item_id,))
        food_itm = cursor.fetchone()
        return food_itm
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return food_itm


# View food reviews of a user in the database
def view_food_reviews(connection, user_id):
    result = []
    cursor = connection.cursor(dictionary=True)
    view_FR = "SELECT review_id, user_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year FROM foodreview WHERE user_id = %s;"
    try:
        cursor.execute(view_FR, (user_id,))
        records = cursor.fetchall()
        for record in records:
            result.append(record)

        return result
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return result

# View reviews within a month of a user in the database
def view_reviews_month_user(connection, id):
    cursor = connection.cursor(dictionary=True)
    result = []
    user_id = (id,)
    food_reviews = "SELECT review_id, user_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year FROM foodreview WHERE user_id = %s AND (review_year = YEAR(CURDATE()) AND review_month = MONTH(CURDATE()));"
    try:
        cursor.execute(food_reviews, user_id)
        records = cursor.fetchall()
        for record in records:
            result.append(record)
        return result
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return result
    
# View reviews within a month for an FE in the database
def view_reviews_month_estab(connection, id):
    cursor = connection.cursor(dictionary=True)
    result = []
    FE_id = (id,)
    food_reviews = "SELECT review_id, user_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year FROM foodreview WHERE establishment_id = %s AND (review_year = YEAR(CURDATE()) AND review_month = MONTH(CURDATE()));"
    try:
        cursor.execute(food_reviews, FE_id)
        records = cursor.fetchall()
        for record in records:
            result.append(record)
        return result
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return result


# View all food establishments in the database
def view_all_FE(connection):
    result = []
    cursor = connection.cursor(dictionary=True)
    view_FE = "SELECT * FROM FoodEstablishment;"
    try:
        cursor.execute(view_FE)
        records = cursor.fetchall()
        for record in records:
            result.append(record)

        return result
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return result

# View all food items in the database
def view_all_FI(connection):
    result = []
    cursor = connection.cursor(dictionary=True)
    view_FI = "SELECT * FROM FoodItem;"
    try:
        cursor.execute(view_FI)
        records = cursor.fetchall()
        for record in records:
            result.append(record)

        return result
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return result


# View all food items from an establishment in the database where price = [None - None, 1 - ASC, 2 - DESC]
def view_food_items(connection, id, type=None, price=None, price_range=None):
    result = []
    cursor = connection.cursor(dictionary=True)

    try:
        if id is not None:
            if type is None:
                if price is None:
                    # View all food items from an establishment
                    query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE establishment_id = %s;"
                    cursor.execute(query, (id,))
                elif price == 1:
                    # View all food items from an establishment arranged according to price (ascending)
                    query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE establishment_id = %s ORDER BY price ASC;"
                    cursor.execute(query, (id,))
                else:
                    # View all food items from an establishment arranged according to price (descending)
                    query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE establishment_id = %s ORDER BY price DESC;"
                    cursor.execute(query, (id,))
            else:
                if price is None:
                    # View all food items from an establishment that belong to a food type
                    query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE establishment_id = %s AND type = %s;"
                    cursor.execute(query, (id, type))
                elif price == 1:
                    # View all food items from an establishment that belong to a food type, order by price (ascending)
                    query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE establishment_id = %s AND type = %s ORDER BY price ASC;"
                    cursor.execute(query, (id, type))
                else:
                    # View all food items from an establishment that belong to a food type, order by price (descending)
                    query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE establishment_id = %s AND type = %s ORDER BY price DESC;"
                    cursor.execute(query, (id, type))
        else:
            if type is None: 
                # Search food items from any establishment based on a given price range
                query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE price >= %s AND price <= %s;"
                cursor.execute(query, (price_range['lowest'], price_range['highest']))
            else:
                if not price_range:
                    # Search food items from any establishment based on a food type
                    query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE type = %s;"
                    cursor.execute(query, (type,))
                else:
                    # Search food items from any establishment based on a given price range and food type
                    query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE type = %s AND (price >= %s AND price <= %s);"
                    cursor.execute(query, (type, price_range['lowest'], price_range['highest']))
        
        records = cursor.fetchall()
        for record in records:
            result.append(record)

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return result


# Verify user credentials for signing in
def authenticate_sign_in(connection, username, password):
    cursor = connection.cursor()
    if not check_username_exists(connection, username):
        return {"success": False, "message": "Invalid credentials. Please try again."}
    else:
        verify_password = "SELECT password, user_id FROM Users WHERE username = %s LIMIT 1;"
        cursor.execute(verify_password, (username,))
        result = cursor.fetchone()
        pw = result[0]
        if(password == pw):
            user_id = result[1]
            return {"success": True, "message": user_id}
        else:
            return {"success": False, "message": "Invalid credentials. Please try again."}

#view food establishment with high average rating
def view_high_rating_FE(connection):
    cursor = connection.cursor(dictionary=True)
    high_rating_establishments = []

    query = """
        SELECT fe.*, AVG(fr.rating) as avg_rating
        FROM FoodEstablishment fe
        JOIN FoodReview fr ON fe.establishment_id = fr.establishment_id
        GROUP BY fe.establishment_id
        HAVING avg_rating >= 4
    """

    try:
        cursor.execute(query)
        high_rating_establishments = cursor.fetchall()
    except Error as err:
        print(f"Error: '{err}'")
    finally:
        cursor.close()

    return high_rating_establishments

#Search food item from any estb by price and type
def search_food_item_bypriceft(connection, min_price=None, max_price=None, food_type=None):
    cursor = connection.cursor(dictionary=True)
    search_results = []

    query = """
        SELECT fi.*, fe.name AS establishment_name
        FROM FoodItem fi
        JOIN FoodEstablishment fe ON fi.establishment_id = fe.establishment_id
        WHERE 1=1
    """
    params = []

    if min_price is not None:
        query += " AND fi.price >= %s"
        params.append(min_price)
    
    if max_price is not None:
        query += " AND fi.price <= %s"
        params.append(max_price)
    
    if food_type is not None:
        query += " AND fi.type = %s"
        params.append(food_type)

    try:
        cursor.execute(query, params)
        search_results = cursor.fetchall()
    except Error as err:
        print(f"Error: '{err}'")
    finally:
        cursor.close()

    return search_results

#View food items belonging to a food establishment
def view_food_items_from_est(connection, establishment_id):
    cursor = connection.cursor(dictionary=True)
    food_items = []

    query = """
        SELECT fi.*, fe.name AS establishment_name
        FROM FoodItem fi
        JOIN FoodEstablishment fe ON fi.establishment_id = fe.establishment_id
        WHERE fi.establishment_id = %s
    """

    try:
        cursor.execute(query, (establishment_id,))
        food_items = cursor.fetchall()
    except Error as err:
        print(f"Error: '{err}'")
    finally:
        cursor.close()

    return food_items

#get the username of a user using user_id 
def get_username_by_user_id(connection, user_id):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT username FROM Users WHERE user_id = %s;"
    try:
        cursor.execute(query, (user_id,))
        record = cursor.fetchone()
        if record:
            return record['username']
        else:
            return None
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
        return None

#view all food reviews from a food establishment
def view_food_reviews_under_establishment(connection, establishment_id):
    result = []
    cursor = connection.cursor(dictionary=True)
    query = """
    SELECT review_id, user_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year 
    FROM FoodReview 
    WHERE establishment_id = %s;
    """
    try:
        cursor.execute(query, (establishment_id,))
        records = cursor.fetchall()
        for record in records:
            result.append(record)
        return result
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
    return result

#view all food reviews from a food item
def view_food_reviews_under_food(connection, food_id):
    result = []
    cursor = connection.cursor(dictionary=True)
    query = """
    SELECT review_id, user_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year 
    FROM FoodReview 
    WHERE item_id = %s;
    """
    try:
        cursor.execute(query, (food_id,))
        records = cursor.fetchall()
        for record in records:
            result.append(record)
        return result
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
    return result

#view reviews within a month
def view_reviews_month(connection):
    cursor = connection.cursor(dictionary=True)
    result = []
    food_reviews = "SELECT review_id, user_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year FROM FoodReview WHERE review_month = MONTH(CURDATE());"
    try:
        cursor.execute(food_reviews)
        records = cursor.fetchall()
        for record in records:
            result.append(record)
        return result
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
    return result

#get reviews made by the user
def get_user_reviews(connection, user_id):
    cursor = connection.cursor(dictionary=True)
    user_reviews = []

    query = """
        SELECT review_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year 
        FROM FoodReview 
        WHERE user_id = %s
    """

    try:
        cursor.execute(query, (user_id,))
        user_reviews = cursor.fetchall()
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
    finally:
        cursor.close()

    return user_reviews

#get the name of the establishment using id
def get_estab_name_by_id(connection, establishment_id):
    cursor = connection.cursor(dictionary=True)  # Use dictionary=True
    query = "SELECT name FROM FoodEstablishment WHERE establishment_id = %s"
    try:
        cursor.execute(query, (establishment_id,))
        result = cursor.fetchone()
        return result['name'] if result else None
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
        return None
    finally:
        cursor.close()

#get the name of the food item using id
def get_food_name_by_id(connection, item_id):
    cursor = connection.cursor(dictionary=True)  # Use dictionary=True
    query = "SELECT food_name FROM FoodItem WHERE item_id = %s"
    try:
        cursor.execute(query, (item_id,))
        result = cursor.fetchone()
        return result['food_name'] if result else None
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
        return None
    finally:
        cursor.close()

#get establishment id by user id
def get_establishment_id_by_user_id(connection, user_id):
    cursor = connection.cursor()
    query = "SELECT establishment_id FROM BusinessOwner WHERE user_id = %s;"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    return result[0] if result else None

#update food establishment
def update_food_establishment(connection, establishment_id, new_name, new_street_address, new_city, new_province):
    cursor = connection.cursor()
    update_FE = "UPDATE FoodEstablishment SET name = %s, street_address = %s, city = %s, province = %s WHERE establishment_id = %s;"
    FE_values = (new_name, new_street_address, new_city, new_province, establishment_id)

    try:
        cursor.execute(update_FE, FE_values)
        connection.commit()
        return True
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return False


