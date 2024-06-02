from colorama import Fore, Style, init
from database_commands import *
init(autoreset=True)

def update_food_item_from_establishment(connection, establishment_id):
    try:
        while True:
            print(Fore.CYAN + "\nUpdate a Food Item")
            
            food_items = view_food_items_from_est(connection, establishment_id)
            if not food_items:
                print(Fore.RED + "No food items found for this establishment.")
                return
            
            print(Fore.YELLOW + "\nList of all food items in the establishment:")
            for i, item in enumerate(food_items, start=1):
                print(f"{i}. {item['food_name']} - ${item['price']}")
            
            item_choice = int(input(Fore.GREEN + "Enter the number of the food item to edit: ")) - 1
            selected_item = food_items[item_choice]

            print(Fore.CYAN + f"\nEditing {selected_item['food_name']}")
            new_name = input(Fore.GREEN + "Enter new name (leave blank to keep current): ").strip()
            new_price = input(Fore.GREEN + "Enter new price (leave blank to keep current): ").strip()

            new_name = new_name if new_name else selected_item['food_name']
            new_price = float(new_price) if new_price else selected_item['price']

            print(Fore.CYAN + f"\nNew details for {selected_item['food_name']}:")
            print(Fore.YELLOW + f"Name: {new_name}")
            print(Fore.YELLOW + f"Price: ${new_price:.2f}")
            
            confirm = input(Fore.GREEN + "Save changes? (yes/no): ").strip().lower()
            if confirm == 'yes':
                success = update_food_item(connection, selected_item['item_id'], new_name, new_price)
                if success:
                    print(Fore.GREEN + "Food item updated successfully!")
                else:
                    print(Fore.RED + "Failed to update the food item.")
            else:
                print(Fore.YELLOW + "Edit cancelled.")
            
            another = input(Fore.GREEN + "Do you want to edit another food item? (yes/no): ").strip().lower()
            if another != 'yes':
                break

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")