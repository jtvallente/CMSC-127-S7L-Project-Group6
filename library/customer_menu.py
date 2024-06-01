from colorama import Fore, Style
import os
from add_food_review import add_food_review
from update_food_review import edit_food_review
from delete_food_review import delete_user_food_review


def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_customer_menu():
    padding_color = '44'  
    menu_text = "  C U S T O M E R  M E N U  "
    menu_color = '44'  
    reset = '\033[0m'  

    print(f"\033[{padding_color}m{' '*len(menu_text)}{reset}")
    
    for i, letter in enumerate(menu_text):
        colored_letter = f'\033[{menu_color}m{letter}{reset}'
        print(colored_letter, end='')

    print(f"\n\033[{padding_color}m{' '*len(menu_text)}{reset}\n")


def customer_dashboard_menu(connection, user_id):
    while True:
        #clear_screen()  # Clear the screen
        print_customer_menu()
        print(Fore.GREEN + "[1] Add food review")
        print(Fore.YELLOW + "[2] Update food review")
        print(Fore.RED + "[3] Delete food review")
        print(Fore.BLUE + "[4] Back to catalog")
        print(Style.RESET_ALL)  # Reset colors
        choice = input("Enter your choice: ")

        if choice == '1':
            add_food_review(connection, user_id)
        elif choice == '2':
            edit_food_review(connection, user_id)
        elif choice == '3':
            delete_user_food_review(connection, user_id)
        elif choice == '4':
            print("Returning to catalog...")
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
#customer_dashboard_menu(connection, u)
