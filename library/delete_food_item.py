from colorama import Fore, Style, init
from database_commands import delete_food_item, view_all_FE, view_food_items_from_est

init(autoreset=True)

def delete_food_item_from_establishment(connection, user_id):
    try:
        while True:
            print(Fore.CYAN + "\nDelete a Food Item")
            
            # Display all food establishments
            establishments = view_all_FE(connection)
            if not establishments:
                print(Fore.RED + "No food establishments found.")
                return
            
            print(Fore.YELLOW + "\nList of all food establishments:")
            for i, est in enumerate(establishments, start=1):
                print(f"{i}. {est['name']}")

            est_choice = int(input(Fore.GREEN + "Enter the number of the establishment: ")) - 1
            est_id = establishments[est_choice]['establishment_id']
            
            # Display all food items belonging to the selected establishment
            food_items = view_food_items_from_est(connection, est_id)
            if not food_items:
                print(Fore.RED + "No food items found for this establishment.")
                continue
            
            print(Fore.YELLOW + "\nList of all food items in the establishment:")
            for i, item in enumerate(food_items, start=1):
                print(f"{i}. {item['food_name']}")

            item_choice = int(input(Fore.GREEN + "Enter the number of the food item to delete: ")) - 1
            item_id = food_items[item_choice]['item_id']

            # Confirm deletion
            confirm = input(Fore.RED + f"Are you sure you want to delete '{food_items[item_choice]['food_name']}'? (yes/no): ")
            if confirm.lower() == 'yes':
                success = delete_food_item(connection, item_id)
                if success:
                    print(Fore.GREEN + "Food item deleted successfully!")
                else:
                    print(Fore.RED + "Failed to delete the food item.")
            else:
                print(Fore.YELLOW + "Deletion cancelled.")
            
            # Ask if the user wants to delete another food item
            another = input(Fore.GREEN + "Do you want to delete another food item? (yes/no): ")
            if another.lower() != 'yes':
                print(Fore.CYAN + "Returning to the dashboard...")
                break

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")