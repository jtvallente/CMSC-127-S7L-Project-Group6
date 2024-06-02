from aifc import Error
from colorama import Fore, Style, init
from database_commands import delete_food_item, view_food_items_from_est, get_establishment_id_by_user_id

init(autoreset=True)

def delete_food_item_from_establishment(connection, user_id):
    try:
        while True:
            print(Fore.CYAN + "\nDelete a Food Item")
            
            establishment_id = get_establishment_id_by_user_id(connection, user_id)
            if not establishment_id:
                print(Fore.RED + "You don't have any establishments yet.")
                return

            food_items = view_food_items_from_est(connection, establishment_id)
            if not food_items:
                print(Fore.RED + "No food items found.")
                return
            
            print(Fore.YELLOW + "\nList of all food items:")
            for i, food in enumerate(food_items, start=1):
                print(f"{i}. {food['food_name']}")

            try:
                food_choice = int(input(Fore.GREEN + "Enter the number of the food item to delete: ")) - 1
                if food_choice < 0 or food_choice >= len(food_items):
                    print(Fore.RED + "Invalid choice. Please enter a valid number.")
                    continue

                selected_food = food_items[food_choice]
            except (ValueError, IndexError):
                print(Fore.RED + "Invalid input. Please enter a valid number.")
                continue

            # Confirm deletion
            confirm = input(Fore.RED + f"Are you sure you want to delete '{selected_food['food_name']}'? (yes/no): ").strip().lower()
            if confirm == 'yes':
                success = delete_food_item(connection, selected_food['item_id'])
                if success:
                    print(Fore.GREEN + "Food item deleted successfully!")
                else:
                    print(Fore.RED + "Failed to delete the food item.")
            else:
                print(Fore.YELLOW + "Deletion cancelled.")
            
            # Ask if the user wants to delete another food item
            another = input(Fore.GREEN + "Do you want to delete another food item? (yes/no): ").strip().lower()
            if another != 'yes':
                print(Fore.CYAN + "Returning to the dashboard...")
                break

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

