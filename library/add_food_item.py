from colorama import Fore, Style, init
from database_commands import add_food_item, view_all_FE
from unique_id_generator import generate_unique_id

init(autoreset=True)

def add_food_item_to_establishment(connection):
    try:
        while True:
            print(Fore.CYAN + "\nAdd a Food Item")

            establishments = view_all_FE(connection)
            if not establishments:
                print(Fore.RED + "No food establishments found.")
                return

            print(Fore.YELLOW + "\nList of all food establishments:")
            for i, est in enumerate(establishments, start=1):
                print(f"{i}. {est['name']}")

            est_choice = int(input(Fore.GREEN + "Enter the number of the establishment: ")) - 1
            est_id = establishments[est_choice]['establishment_id']

            food_name = input(Fore.GREEN + "Enter the food name: ").strip()
            if not food_name:
                print(Fore.RED + "Food name cannot be empty.")
                continue

            try:
                price = float(input(Fore.GREEN + "Enter the price: ").strip())
            except ValueError:
                print(Fore.RED + "Price must be a number.")
                continue

            food_type = input(Fore.GREEN + "Enter the food type (meat, veg, etc.): ").strip()
            if not food_type:
                print(Fore.RED + "Food type cannot be empty.")
                continue

            confirm = input(Fore.GREEN + "Do you want to save the food item? (yes/no): ").strip().lower()
            if confirm != 'yes':
                print(Fore.YELLOW + "Food item not saved.")
                return

            item_id = generate_unique_id()
            success = add_food_item(connection, item_id, est_id, food_name, price, food_type)
            if success:
                print(Fore.GREEN + "Food item added successfully!")
            else:
                print(Fore.RED + "Failed to add the food item.")
            
            another = input(Fore.GREEN + "Do you want to add another food item? (yes/no): ").strip().lower()
            if another != 'yes':
                break

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")