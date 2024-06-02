from colorama import Fore, Style, init
from database_commands import *
from unique_id_generator import generate_unique_id

init(autoreset=True)

def view_all_food_items(connection, establishment_id):
    while True:
        clear_screen()
        print(Fore.CYAN + "\nFood Items Menu")

        food_items = view_food_items_from_est(connection, establishment_id)
        if not food_items:
            print(Fore.RED + "No food items found for this establishment.")
        else:
            print(Fore.YELLOW + "\nList of all food items in the establishment:")
            for i, item in enumerate(food_items, start=1):
                print(f"{i}. {item['food_name']} - ${item['price']} ({item['type']})")

        print(Fore.GREEN + "\nOptions:")
        print("[1] Add a food item")
        print("[2] Update a food item")
        print("[3] Delete a food item")
        print("[4] Go back to dashboard")
        print(Style.RESET_ALL)

        choice = input("Enter your choice: ")

        if choice == '1':
            add_food_item_to_establishment(connection)
        elif choice == '2':
            update_food_item_from_establishment(connection, establishment_id)
        elif choice == '3':
            delete_food_item_from_establishment(connection)
        elif choice == '4':
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")