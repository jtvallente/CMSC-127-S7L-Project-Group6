from colorama import Fore, Style
import os

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


#These 3 functions below are just placeholders. 
#It will be replaced by the imported functions/libs created by other members
def add_food_review():
    print("Adding food review...")


def update_food_review():
    print("Updating food review...")

def delete_food_review():
    print("Deleting food review...")

def customer_menu():
    while True:
        clear_screen()  # Clear the screen
        print_customer_menu()
        print(Fore.GREEN + "1: Add food review")
        print(Fore.YELLOW + "2: Update food review")
        print(Fore.RED + "3: Delete food review")
        print(Fore.BLUE + "4: Back to catalog")
        print(Style.RESET_ALL)  # Reset colors
        choice = input("Enter your choice: ")

        if choice == '1':
            add_food_review()
        elif choice == '2':
            update_food_review()
        elif choice == '3':
            delete_food_review()
        elif choice == '4':
            print("Returning to catalog...")
            break
        else:
            print("Invalid choice. Please try again.")

# Example usage
customer_menu()
