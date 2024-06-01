from colorama import Fore, Style
from pwinput import pwinput
from database_commands import authenticate_sign_in
import os


def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')


def print_log_in():
    padding_color = '44'  
    menu_text = "  L O G  I N  "
    menu_color = '44'  
    reset = '\033[0m'  

    print(f"\033[{padding_color}m{' '*len(menu_text)}{reset}")
    
    for i, letter in enumerate(menu_text):
        colored_letter = f'\033[{menu_color}m{letter}{reset}'
        print(colored_letter, end='')

    print(f"\n\033[{padding_color}m{' '*len(menu_text)}{reset}\n") 

# Resolves circular import issue for sign in
def sign_in(connection):
    signed_in = False
    while not signed_in:
        print_log_in()
        username = input(Fore.BLUE + "Username: ").strip()
        password = pwinput(Fore.BLUE + "Password: ").strip()
        result = authenticate_sign_in(connection, username, password)
        if result["success"]:
            print(Fore.GREEN + "Successful sign in!")
            user_id = result["message"]
            print(user_id)
            signed_in = True