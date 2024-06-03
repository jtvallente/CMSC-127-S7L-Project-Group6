import unique_id_generator
from database_commands import establish_server_connection, check_username_exists, add_user, add_customer, add_businessowner, add_food_establishment_to_db, add_food_item
from authentication_sign_in import sign_in
from colorama import Fore
from pwinput import pwinput
import random
import string
import os

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_create_account(role):
    padding_color = '44'
    if(role == 1): menu_text = "  S I G N  U P  A S  C U S T O M E R  "
    else: menu_text = "  S I G N  U P  A S  B U S I N E S S  O W N E R  "
    menu_color = '44'  
    reset = '\033[0m'  

    print(f"\033[{padding_color}m{' '*len(menu_text)}{reset}")
    
    for i, letter in enumerate(menu_text):
        colored_letter = f'\033[{menu_color}m{letter}{reset}'
        print(colored_letter, end='')

    print(f"\n\033[{padding_color}m{' '*len(menu_text)}{reset}\n")

# Checks if username is valid
def validate_username(connection, username):
    exists = check_username_exists(connection, username)
    
    if(len(username) == 0):
        print(Fore.RED + "Username cannot be empty!")
        return False
    elif(len(username) < 6):
        print(Fore.RED + "Username must be atleast 6 characters.")
        return False
    elif(exists):
        print(Fore.RED + "Username already exists!")
        return False
    else: return True

# Create user ID for customer or business owner
def generate_user_id(role):
    random_characters = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    if(role == 1):
        return f"CUSTO{random_characters}"
    else: return f"BUSO{random_characters}"

# Get the details for creating a new food establishment
def get_food_establishment_details():
    id = unique_id_generator.generate_unique_id()
    food_establishment = dict(
        establishment_id = id,
        name = "",
        street = "",
        city = "",
        province =  "",
        food_items = []
    )

    print()
    print(Fore.GREEN + "FOOD ESTABLISHMENT DETAILS")
    while len(food_establishment["name"]) == 0:
        food_establishment["name"] = input(Fore.BLUE + "Enter name of food establishment: ")
        if len(food_establishment["name"]) == 0: print(Fore.RED + "Food establishment name cannot be empty!")
    while len(food_establishment["street"]) == 0:
        food_establishment["street"] = input(Fore.BLUE + "Enter street and barangay address: ")
        if len(food_establishment["street"]) == 0: print(Fore.RED + "Street and barangay address name cannot be empty!")
    while len(food_establishment["city"]) == 0:
        food_establishment["city"] = input(Fore.BLUE + "Enter city address: ")
        if len(food_establishment["city"]) == 0: print(Fore.RED + "City address name cannot be empty!")
    while len(food_establishment["province"]) == 0:
        food_establishment["province"] = input(Fore.BLUE + "Enter province address: ")
        if len(food_establishment["province"]) == 0: print(Fore.RED + "Province address name cannot be empty!")
    print()
    print(Fore.RED + "ATLEAST ONE FOOD ITEM IS REQUIRED")
    added_food_items = False

    while not added_food_items:
        item_id = unique_id_generator.generate_unique_id()
        food_name = ""
        food_type = ""
        valid_food_price = False
        valid_food_type = False

        while len(food_name) == 0:
            food_name = input(Fore.BLUE + "Enter food name: ")
            if len(food_name) == 0: print(Fore.RED + "Food name cannot be empty!")

        while not valid_food_type:
            type = input(Fore.BLUE + "Enter food type (1 - Meat, 2 - Veg, 3 - Etc.): ")
            try:
                food_type = int(type)
                if food_type < 1 or food_type > 3:
                    print(Fore.RED + "Invalid food type! Please enter 1, 2, or 3.")
                else:
                    valid_food_type = True
                    break
            except ValueError:
                print(Fore.RED + "Invalid food type! Please enter a number.")


        while not valid_food_price:
            price = input(Fore.BLUE + "Enter food price: ")
            try:
                food_price = float(price)
                if food_price <= 0:
                    print(Fore.RED + "Food price must be greater than 0!")
                else:
                    valid_food_price = True
                    break
            except ValueError:
                print(Fore.RED + "Invalid food price!")

        food_establishment["food_items"].append({
            "item_id": item_id,
            "food_name": food_name,
            "food_price": food_price,
            "food_type": food_type,
            "establishment_id": id
        })

        while True:
            choice = input(Fore.BLUE + "Add another food item? (Y/N): ")
            if choice.upper() == 'Y': break
            elif choice.upper() == 'N':
                added_food_items = True
                break
            else: print(Fore.RED + "Invalid choice! Try again...")
    
    return food_establishment


# Implements create account for customer or business owner
def create_account(connection, role):
    print_create_account(role)
    if role == 1: account_role = "customer"
    else: account_role = "business_owner"
    valid_username = False
    valid_password = False
    password_confirmed = False

    while not valid_username:
        username = input(Fore.BLUE + "Create your username: ")
        if validate_username(connection, username): valid_username = True

    while not password_confirmed:
        if not password_confirmed:
            while not valid_password:
                password = pwinput(Fore.BLUE + "Create your password: ")
                if(len(password) == 0): 
                    print(Fore.RED + "Password cannot be empty!")
                elif(len(password) < 6):
                    print(Fore.RED + "Password must be atleast 6 characters.")
                else: valid_password = True
        confirm_password = pwinput(Fore.BLUE + "Confirm your password: ")
        if(confirm_password == password): password_confirmed = True
        else: print(Fore.RED + "Passwords do not match!")

    user_id = generate_user_id(role)
    if(role == 2):
        food_establishment = get_food_establishment_details()

    print(Fore.BLUE + "Creating account...")
    result = add_user(connection, user_id, username, password, account_role)
    if result:
        print(Fore.GREEN + "Your account has been successfully created!")
        if role == 1:
            if add_customer(connection, user_id):
                print(Fore.GREEN + "A new customer has been added!")
            else:
                print(Fore.RED + "Failed to add new customer")
        else:
            if add_food_establishment_to_db(connection, food_establishment["establishment_id"], food_establishment["name"], food_establishment["street"], food_establishment["city"], food_establishment["province"]):
                print(Fore.GREEN + "Your food establishment has been successfully created!")
                for item in food_establishment["food_items"]:
                    add_food_item(connection, item["item_id"], item["establishment_id"], item["food_name"], item["food_price"], item["food_type"])
                if add_businessowner(connection, user_id, food_establishment["establishment_id"]):
                    print(Fore.GREEN + "A new business owner has been added!")
                else:
                    print(Fore.RED + "Failed to add new business owner")
            else:
                print(Fore.RED + "Failed to create your food establishment")

        while True:
            choice = input(Fore.BLUE + "Continue to sign in [Y] or exit [N]? ")
            if choice.upper() == 'Y':
                sign_in(connection)
                break
            elif choice.upper() == 'N':
                # Close the connection to the database
                connection.close()
                print("Returning to catalog...")
                break
            else: print(Fore.RED + "Invalid choice! Try again...")
    else:
        print(Fore.RED + "Account creation failed.")