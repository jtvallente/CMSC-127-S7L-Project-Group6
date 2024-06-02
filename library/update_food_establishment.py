from colorama import Fore, Style, init
from database_commands import view_all_FE, update_food_establishment, search_food_establishment, get_establishment_id_by_user_id, get_estab_name_by_id
from mysql.connector import Error

init(autoreset=True)

def update_food_establishment_details(connection, user_id):
    try:
        while True:
            print(Fore.CYAN + "\nUpdate Food Establishment Details")

            establishment_id = get_establishment_id_by_user_id(connection, user_id)
            establishment_name = get_estab_name_by_id(connection, establishment_id)
            print("\n - " + establishment_name)

            establishment = search_food_establishment(connection, establishment_id)
            if not establishment:
                print(Fore.RED + "\nYou don't have an establishment yet. Please add a new one.")
                return

            selected_est = establishment

            new_name = input(Fore.GREEN + "Enter the new name (leave blank to keep current): ").strip() or selected_est['name']
            new_address = input(Fore.GREEN + "Enter the new street address (leave blank to keep current): ").strip() or selected_est['street_address']
            new_city = input(Fore.GREEN + "Enter the new city (leave blank to keep current): ").strip() or selected_est['city']
            new_province = input(Fore.GREEN + "Enter the new province (leave blank to keep current): ").strip() or selected_est['province']

            print(Fore.CYAN + "\nReview the changes:")
            print(f"Name: {selected_est['name']} -> {new_name}")
            print(f"Street Address: {selected_est['street_address']} -> {new_address}")
            print(f"City: {selected_est['city']} -> {new_city}")
            print(f"Province: {selected_est['province']} -> {new_province}")

            choice = input(Fore.GREEN + "Do you want to save the changes? (yes/no): ")
            if choice.lower() == 'yes':
                success = update_food_establishment(connection, establishment_id, new_name, new_address, new_city, new_province)
                if success:
                    print(Fore.GREEN + "Food establishment updated successfully!")
                else:
                    print(Fore.RED + "Failed to update the food establishment.")
            else:
                print(Fore.YELLOW + "Changes discarded.")

            another = input(Fore.GREEN + "Do you want to update another establishment? (yes/no): ")
            if another.lower() != 'yes':
                break

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")
