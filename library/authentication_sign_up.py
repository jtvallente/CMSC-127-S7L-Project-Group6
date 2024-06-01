from colorama import Fore, Style
from create_account_menu import create_account_menu

# Resolves circular import issue for sign up
def sign_up(connection):
    create_account_menu(connection)
