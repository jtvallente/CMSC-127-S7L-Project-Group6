from colorama import Fore, Style
import os

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome():
    padding_color = '44'  
    menu_text = "  W E L C O M E !  "
    menu_color = '44'  
    reset = '\033[0m'  

    print(f"\033[{padding_color}m{' '*len(menu_text)}{reset}")
    
    for i, letter in enumerate(menu_text):
        colored_letter = f'\033[{menu_color}m{letter}{reset}'
        print(colored_letter, end='')

    print(f"\n\033[{padding_color}m{' '*len(menu_text)}{reset}\n")


#These 2 functions below are just placeholders. 
#It will be replaced by the imported functions/libs created by other members
def login():
    print("Adding food review...")

def signup():
    print("Updating food review...")

def welcome_page():
    while True:
        clear_screen()  # Clear the screen
        print_welcome()
        print("App version: 1.1\n")
        print(Fore.GREEN + "[1] Login")
        print(Fore.BLUE + "[2] Create an Account")
        print("")
        print(Fore.RED + "[3] Exit")
        print(Style.RESET_ALL)  # Reset colors
        choice = input("Enter your choice: ")

        if choice == '1':
            login()
        elif choice == '2':
            signup()
        elif choice == '3':
            print("\nProgram Exitting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
welcome_page()
