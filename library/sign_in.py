from colorama import Fore, Style
import os

import getpass
import re
from werkzeug.security import generate_password_hash, check_password_hash

#This will be connected to the user_id column
user_id = {}

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_main_menu():
    padding_color = '44'  
    menu_text = "  W E L C O M E  "
    menu_color = '44'  
    reset = '\033[0m'  

    print(f"\033[{padding_color}m{' '*len(menu_text)}{reset}")
    
    for i, letter in enumerate(menu_text):
        colored_letter = f'\033[{menu_color}m{letter}{reset}'
        print(colored_letter, end='')

    print(f"\n\033[{padding_color}m{' '*len(menu_text)}{reset}\n")

#These 2 functions below are just placeholders. 
#It will be replaced by the imported functions/libs created by other members

def sign_up():
    print("Signing up...")

def sign_in():
    clear_screen()
    print("Sign In")
    username = input("Username: ").strip()
    password = getpass.getpass("Password: ").strip()
    
    if username in user_id and check_password_hash(user_id[username], password):
        print(f"Welcome, {username}!")
    else:
        print("Invalid credentials. Please try again.")
    
    input("Press enter to continue...")

def main_menu():
    while True:
        clear_screen() # Clear the screen
        print_main_menu()
        print(Fore.GREEN + "[1] Sign In")
        print(Fore.YELLOW + "[2] Sign Up")
        print(Fore.BLUE + "[3] Exit")
        print(Style.RESET_ALL)  # Reset colors
        choice = input("Enter your choice: ")

        if choice == '1':
            sign_in()
        elif choice == '2':
            sign_up()
        elif choice == '3':
            print("Thank you! Until next time...")
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
main_menu()