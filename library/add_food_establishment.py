from colorama import Fore, Style, init
from database_commands import *
from unique_id_generator import generate_unique_id

init(autoreset=True)

def add_food_establishment(connection, user_id):
    try:
        print(Fore.CYAN + "\nAdd a Food Establishment")

        # Check if the owner already has an establishment
        establishment_id = get_establishment_id_by_user_id(connection, user_id)
        if establishment_id:
            print(Fore.RED + "\nYou already have an establishment. Please delete it before adding a new one.\n")
            return
        
        name = input(Fore.GREEN + "Enter the establishment name: ").strip()
        street_address = input(Fore.GREEN + "Enter the street address: ").strip()
        city = input(Fore.GREEN + "Enter the city: ").strip()
        province = input(Fore.GREEN + "Enter the province: ").strip()

        if not name or not street_address or not city or not province:
            print(Fore.RED + "All fields are required. Please provide valid inputs.")
            return

        establishment_id = generate_unique_id()

        success = add_food_establishment_to_db(connection, establishment_id, name, street_address, city, province)
        if success:
            print(Fore.GREEN + "Food establishment added successfully!")
            add_businessowner(connection, user_id, establishment_id)
        else:
            print(Fore.RED + "Failed to add the food establishment.")

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")