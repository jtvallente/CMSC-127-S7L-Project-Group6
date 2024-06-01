from colorama import Fore, Style
import os
#from welcome_page import main_menu
from customer_menu import customer_dashboard_menu
from view_all_foodest import view_all_establishments

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_catalog_menu():
    padding_color = '44'  
    menu_text = " C A T A L O G  "
    menu_color = '44'  
    reset = '\033[0m'  

    print(f"\033[{padding_color}m{' '*len(menu_text)}{reset}")
    
    for i, letter in enumerate(menu_text):
        colored_letter = f'\033[{menu_color}m{letter}{reset}'
        print(colored_letter, end='')

    print(f"\n\033[{padding_color}m{' '*len(menu_text)}{reset}\n")


#These 3 functions below are just placeholders. 
#It will be replaced by the imported functions/libs created by other members


def view_all_foodreview(connection):
    print("Updating food review...")

def my_dashboard(connection, user_id):
    print(user_id)
    if user_id[:4] == 'CUST':
        print("going to cust dashb")
        customer_dashboard_menu(connection, user_id)
    else:
        print("going to business owner")

def catalog(connection, user_id):
    while True:
        #clear_screen()  # Clear the screen
        print_catalog_menu()
        print(Fore.GREEN + "[1] View all food establishment")
        print(Fore.YELLOW + "[2] View all food review")
        print(Fore.RED + "[3] My Dashboard")
        print(Fore.BLUE + "[4] Exit")
        print(Style.RESET_ALL)  # Reset colors
        choice = input("Enter your choice: ")

        if choice == '1':
            view_all_establishments(connection)
        elif choice == '2':
            view_all_foodreview()
        elif choice == '3':
            my_dashboard(connection, user_id)
        elif choice == '4':
            print("Returning to welcome page...")
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
#customer_menu()
