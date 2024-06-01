from colorama import Fore, Style, init
from database_commands import *
from unique_id_generator import generate_unique_id
from datetime import datetime

init(autoreset=True)

def add_food_item_to_establishment(connection, user_id):
    try:
        print(Fore.CYAN + "\nAdd a Food Item")
        
        # Get the establishment associated with the owner
        query = """
        SELECT establishment_id 
        FROM BusinessOwner 
        WHERE user_id = %s
        """
        cursor = connection.cursor()
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        
        if not result:
            print(Fore.RED + "No establishment found for this owner.")
            return
        
        est_id = result[0]

        # Get the establishment details
        est_name = get_estab_name_by_id(connection, est_id)
        print(Fore.YELLOW + f"\nEstablishment: {est_name}")

        food_name = input(Fore.GREEN + "Enter the food item name: ")
        price = float(input(Fore.GREEN + "Enter the price of the food item: "))
        food_type = input(Fore.GREEN + "Enter the type of food item: ")

        item_id = generate_unique_id()

        success = add_food_item(connection, item_id, est_id, food_name, price, food_type)
        if success:
            print(Fore.GREEN + "Food item added successfully!")
        else:
            print(Fore.RED + "Failed to add the food item.")

        another = input(Fore.GREEN + "Do you want to add another food item? (yes/no): ")
        if another.lower() == 'yes':
            add_food_item_to_establishment(connection, user_id)

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")