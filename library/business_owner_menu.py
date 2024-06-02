from colorama import Fore, Style
import os
from add_food_establishment import add_food_establishment
from update_food_establishment import update_food_establishment_details
from delete_food_establishment import delete_food_establishment_menu
from database_commands import get_estab_name_by_id, get_establishment_id_by_user_id, view_food_items
from add_food_item import *
from update_food_item import *
from delete_food_item import *


def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_business_owner_menu():
    padding_color = '44'  
    menu_text = "  B U S I N E S S  O W N E R  M E N U  "
    menu_color = '44'  
    reset = '\033[0m'  

    print(f"\033[{padding_color}m{' '*len(menu_text)}{reset}")
    
    for i, letter in enumerate(menu_text):
        colored_letter = f'\033[{menu_color}m{letter}{reset}'
        print(colored_letter, end='')

    print(f"\n\033[{padding_color}m{' '*len(menu_text)}{reset}\n")

def print_view_all_food_items_menu():
    padding_color = '44'  
    menu_text = "  V I E W  A L L  F O O D  I T E M S  "
    menu_color = '44'  
    reset = '\033[0m'  

    print(f"\033[{padding_color}m{' '*len(menu_text)}{reset}")
    
    for i, letter in enumerate(menu_text):
        colored_letter = f'\033[{menu_color}m{letter}{reset}'
        print(colored_letter, end='')

    print(f"\n\033[{padding_color}m{' '*len(menu_text)}{reset}\n")


def view_all_food_items(connection, user_id):
    while True:
        #clear_screen()  # Clear the screen
        print_view_all_food_items_menu()
        establishment_id = get_establishment_id_by_user_id(connection, user_id)
        food_items = view_food_items(connection, establishment_id)

        if not food_items:  # This handles both None and empty list cases
            print(Fore.RED + "\nNo Food Items yet\n")
        else:
            print(Fore.YELLOW + "\nList of all food items:")
            for i, food in enumerate(food_items, start=1):
                print(f"{i}. {food['food_name']} - P{food['price']}")
            print("\n")

        print(Fore.GREEN + "[1] Add food item")
        print(Fore.YELLOW + "[2] Update food item")
        print(Fore.RED + "[3] Delete food item")
        print(Fore.BLUE + "[4] Back to previous menu")
        print(Style.RESET_ALL) # Reset colors
        choice = input("Enter your choice: ")

        if choice == '1':
            add_food_item_to_establishment(connection, user_id)
        elif choice == '2':
            update_food_item_from_establishment(connection, user_id)
        elif choice == '3':
            delete_food_item_from_establishment(connection, user_id)
        elif choice == '4':
            print("Returning to previous menu...")
            break
        else:
            print("Invalid choice. Please try again.")
        
def business_owner_dashboard_menu(connection, user_id):
    while True:
        #clear_screen()  # Clear the screen
        print_business_owner_menu()
        establishment_id = get_establishment_id_by_user_id(connection, user_id)
        if not establishment_id:
            establishment_name = get_estab_name_by_id(connection, establishment_id)
            if not establishment_name: 
                print("\nBusiness Establishment: " + establishment_name + "\n")
        print(Fore.GREEN + "[1] Add food establishment")
        print(Fore.YELLOW + "[2] Update food establishment")
        print(Fore.RED + "[3] Delete food establishment")
        print(Fore.CYAN + "[4] View all food items")
        print(Fore.BLUE + "[5] Back to catalog")
        print(Style.RESET_ALL)  # Reset colors
        choice = input("Enter your choice: ")

        if choice == '1':
            add_food_establishment(connection, user_id)
        elif choice == '2':
            update_food_establishment_details(connection, user_id)
        elif choice == '3':
            delete_food_establishment_menu(connection, user_id)
        elif choice == '4':
            view_all_food_items(connection, user_id)
        elif choice == '5':
            print("Returning to catalog...")
            break
        else:
            print("Invalid choice. Please try again.")

