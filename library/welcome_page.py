from colorama import Fore, Style
from authentication_sign_in import sign_in
from authentication_sign_up import sign_up
import os

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


def main_menu(connection):
    while True:
        clear_screen() # Clear the screen
        print_main_menu()
        print(Fore.GREEN + "[1] Sign In")
        print(Fore.BLUE + "[2] Sign Up")
        print(Fore.RED + "[3] Exit")
        print(Style.RESET_ALL)  # Reset colors
        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            sign_in(connection)
        elif choice == '2':
            print()
            sign_up(connection)
        elif choice == '3':
            print("Thank you! Until next time...")
            # Close the connection to the database
            connection.close()
            break
        else:
            print("Invalid choice. Please try again.")
