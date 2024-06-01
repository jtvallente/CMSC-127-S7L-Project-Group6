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
def add_food_establishment(connection, establishment_id, name, street_address, city, province):
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


# Add a food review in the database
def add_food_review(connection, review_id, user_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year):
    cursor = connection.cursor()
    if item_id is None:
        add_FR = "INSERT INTO FoodReview (review_id, user_id, establishment_id, review_text, rating, review_month, review_day, review_year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        FR_values = (review_id, user_id, establishment_id, review_text, rating, review_month, review_day, review_year)

        try:
            cursor.execute(add_FR, FR_values)
            connection.commit()
            return True
        except Error as err:
            print(Fore.RED + f"Error: '{err}'")
        
        return False
    else:
        add_FR = "INSERT INTO FoodReview (review_id, user_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
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
    cursor = connection.cursor()
    food_estab = None
    search_FE = "SELECT establishment_id, name, street_address, city, province FROM FoodEstablishment WHERE establishment_id = %s LIMIT 1);"

    try:
        cursor.execute(search_FE, (establishment_id,))
        food_estab = cursor.fetchone()
        return food_estab
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return food_estab


# Search for a food item in the database
def search_food_item(connection, item_id):
    cursor = connection.cursor()
    food_itm = None
    search_FI = "SELECT item_id, establishment_id, food_name, price, type FROM FoodItem WHERE item_id = %s LIMIT 1);"

    try:
        cursor.execute(search_FI, (item_id,))
        food_itm = cursor.fetchone()
        return food_itm
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return food_itm
    


# View all food establishments in the database
def view_all_FE(connection):
    result = []
    cursor = connection.cursor()
    view_FE = "SELECT * FROM FoodEstablishment;"
    try:
        cursor.execute(view_FE)
        records = cursor.fetchAll()
        for record in records:
            record = list(record)
            result.append(record)

        return result
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return result

# View all food items in the database
def view_all_FI(connection):
    result = []
    cursor = connection.cursor()
    view_FI = "SELECT * FROM FoodItem;"
    try:
        cursor.execute(view_FI)
        records = cursor.fetchAll()
        for record in records:
            record = list(record)
            result.append(record)

        return result
    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

    return result


# View all food items from an establishment in the database where price = [None - None, 1 - ASC, 2 - DESC]
def view_food_items(connection, id, type, price, price_range):
    result = []
    cursor = connection.cursor()
    result = None

    if id == None:
        if type == None: 
            # Search food items from any establishment based on a given price range
            query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE price >= %s AND price <= %s;"
            try:
                cursor.execute(query, (id, price_range['lowest'], price_range['highest']))
                records = cursor.fetchAll()
                for record in records:
                    record = list(record)
                    result.append(record)

                return result
            except Error as err:
                print(Fore.RED + f"Error: '{err}'")

            return result
        else:
            if not price_range:
                # Search food items from any establishment based on a food type
                query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE food_type = %s;"
                try:
                    cursor.execute(query, (type,))
                    records = cursor.fetchAll()
                    for record in records:
                        record = list(record)
                        result.append(record)

                    return result
                except Error as err:
                    print(Fore.RED + f"Error: '{err}'")

                return result
            else:
                # Search food items from any establishment based on a given price range and food type
                query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE food_type = %s AND (price >= %s AND price <= %s);"
                try:
                    cursor.execute(query, (type, price_range['lowest'], price_range['highest']))
                    records = cursor.fetchAll()
                    for record in records:
                        record = list(record)
                        result.append(record)

                    return result
                except Error as err:
                    print(Fore.RED + f"Error: '{err}'")

                return result
    else:
        if type == None:
            if price == None:
                # View all food items from an establishment
                query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE establishment_id = %s;"
                try:
                    cursor.execute(query, (id,))
                    records = cursor.fetchAll()
                    for record in records:
                        record = list(record)
                        result.append(record)

                    return result
                except Error as err:
                    print(Fore.RED + f"Error: '{err}'")

                return result
            elif price == 1:
                # View all food items from an establishment arranged according to price (ascending)
                query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE establishment_id = %s ORDER BY price;"
                try:
                    cursor.execute(query, (id,))
                    records = cursor.fetchAll()
                    for record in records:
                        record = list(record)
                        result.append(record)

                    return result
                except Error as err:
                    print(Fore.RED + f"Error: '{err}'")

                return result
            else:
                # View all food items from an establishment arranged according to price (descending)
                query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE establishment_id = %s ORDER BY price DESC;"
                try:
                    cursor.execute(query, (id,))
                    records = cursor.fetchAll()
                    for record in records:
                        record = list(record)
                        result.append(record)

                    return result
                except Error as err:
                    print(Fore.RED + f"Error: '{err}'")

                return result
        else:
            if price == None:
                # View all food items from an establishment that belong to a food type
                query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE establishment_id = %s AND food_type = %s;"
                try:
                    cursor.execute(query, (id, type))
                    records = cursor.fetchAll()
                    for record in records:
                        record = list(record)
                        result.append(record)

                    return result
                except Error as err:
                    print(Fore.RED + f"Error: '{err}'")

                return result
            elif price == 1:
                # View all food items from an establishment that belong to a food type, order by price (ascending)
                query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE establishment_id = %s AND food_type = %s ORDER BY price;"
                try:
                    cursor.execute(query, (id, type))
                    records = cursor.fetchAll()
                    for record in records:
                        record = list(record)
                        result.append(record)

                    return result
                except Error as err:
                    print(Fore.RED + f"Error: '{err}'")

                return result
            else:
                # View all food items from an establishment that belong to a food type, order by price (descending)
                query = "SELECT item_id, food_name, price, type FROM FoodItem WHERE establishment_id = %s AND food_type = %s ORDER BY price DESC;"
                try:
                    cursor.execute(query, (id,))
                    records = cursor.fetchAll()
                    for record in records:
                        record = list(record)
                        result.append(record)

                    return result
                except Error as err:
                    print(Fore.RED + f"Error: '{err}'")

                return result

# View food reviews within a month            
def view_reviews_month(connection):
    cursor = connection.cursor()
    result = None
    food_reviews = "SELECT review_id, user_id, establishment_id, item_id, review_text, rating, review_month, review_day, review_year FROM FoodReview WHERE review_month = MONTH(CURDATE());"
    try:
        cursor.execute(food_reviews)
        records = cursor.fetchAll()
        for record in records:
            record = list(record)
            result.append(record)

        return result
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

