from colorama import Fore, Style, init
from database_commands import *
from unique_id_generator import generate_unique_id

init(autoreset=True)

def add_food_item_to_establishment(connection, user_id):
    try:
        while True:
            print(Fore.CYAN + "\nAdd a Food Item")
            establishment_id = get_establishment_id_by_user_id(connection, user_id)

            if not establishment_id:
                print(Fore.RED + "\nYou haven't added a food establishment yet!\n")
                return

            food_name = input(Fore.GREEN + "Enter the food name: ").strip()
            if not food_name:
                print(Fore.RED + "Food name cannot be empty.")
                continue

            try:
                price = float(input(Fore.GREEN + "Enter the price: ").strip())
                if price < 0:
                    print(Fore.RED + "Price cannot be negative.")
                    continue
            except ValueError:
                print(Fore.RED + "Price must be a valid number.")
                continue

            food_type = input(Fore.GREEN + "Enter the food type (meat, veg, etc.): ").strip()
            if not food_type:
                print(Fore.RED + "Food type cannot be empty.")
                continue

            confirm = input(Fore.GREEN + "Do you want to save the food item? (yes/no): ").strip().lower()
            if confirm != 'yes':
                print(Fore.YELLOW + "Food item not saved.")
                continue

            item_id = generate_unique_id()
            success = add_food_item(connection, item_id, establishment_id, food_name, price, food_type)
            if success:
                print(Fore.GREEN + "Food item added successfully!")
            else:
                print(Fore.RED + "Failed to add the food item.")
            
            another = input(Fore.GREEN + "Do you want to add another food item? (yes/no): ").strip().lower()
            if another != 'yes':
                break

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
