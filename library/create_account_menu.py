from colorama import Fore, Style
import os
from create_account import create_account

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_create_account_menu():
    padding_color = '44'  
    menu_text = "  C R E A T E  A C C O U N T  "
    menu_color = '44'  
    reset = '\033[0m'  

    print(f"\033[{padding_color}m{' '*len(menu_text)}{reset}")
    
    for i, letter in enumerate(menu_text):
        colored_letter = f'\033[{menu_color}m{letter}{reset}'
        print(colored_letter, end='')

    print(f"\n\033[{padding_color}m{' '*len(menu_text)}{reset}\n") 

# Menu for create account page
def create_account_menu(connection):
    print(Fore.GREEN + "Signing up...")
    while True:
        clear_screen()  # Clear the screen
        print_create_account_menu()
        print(Fore.GREEN + "[1] Sign Up As Customer")
        print(Fore.RED + "[2] Sign Up As Business Owner")
        print(Fore.BLUE + "[3] Back to catalog")
        print(Style.RESET_ALL)  # Reset colors
        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            create_account(connection, 1)
            break
        elif choice == '2':
            print()
            create_account(connection, 2)
            break
        elif choice == '3':
            print("Returning to catalog...")
            break
        else:
            print("Invalid choice. Please try again.")
