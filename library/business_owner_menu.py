from colorama import Fore, Style
import os

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

#These 7 functions below are just placeholders. 
#It will be replaced by the imported functions/libs created by other members
def add_food_establishment():
    print("Adding food establishment...")

def update_food_establishment():
    print("Updating food establishment...")

def delete_food_establishment():
    print("Deleting food establishment...")

def add_food_item():
    print("Adding food item...")

def update_food_item():
    print("Updating food item...")

def delete_food_item():
    print("Deleting food item...")

def view_all_food_items():
    while True:
        clear_screen()  # Clear the screen
        print_view_all_food_items_menu()
        print(Fore.GREEN + "[1] Add food item")
        print(Fore.YELLOW + "[2] Update food item")
        print(Fore.RED + "[3] Delete food item")
        print(Fore.BLUE + "[4] Back to previous menu")
        print(Style.RESET_ALL) # Reset colors
        choice = input("Enter your choice: ")

        if choice == '1':
            add_food_item()
        elif choice == '2':
            update_food_item()
        elif choice == '3':
            delete_food_item()
        elif choice == '4':
            print("Returning to previous menu...")
            break
        else:
            print("Invalid choice. Please try again.")
        
def business_owner_dashboard_menu(connection, user_id):
    while True:
        clear_screen()  # Clear the screen
        print_business_owner_menu()
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
            update_food_establishment(connection, user_id)
        elif choice == '3':
            delete_food_establishment(connection, user_id)
        elif choice == '4':
            view_all_food_items(connection, establishment_id)
        elif choice == '5':
            print("Returning to catalog...")
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
business_owner_menu()