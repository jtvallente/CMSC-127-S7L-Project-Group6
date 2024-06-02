from colorama import Fore, Style, init
from database_commands import view_all_FE, update_food_establishment

init(autoreset=True)

def update_food_establishment_details(connection):
    try:
        while True:
            print(Fore.CYAN + "\nUpdate Food Establishment Details")

            establishments = view_all_FE(connection)
            if not establishments:
                print(Fore.RED + "No food establishments found.")
                return

            print(Fore.YELLOW + "\nList of all food establishments:")
            for i, est in enumerate(establishments, start=1):
                print(f"{i}. {est['name']} - {est['street_address']}")

            est_choice = int(input(Fore.GREEN + "Enter the number of the establishment you want to update: ")) - 1
            selected_est = establishments[est_choice]
            est_id = selected_est['establishment_id']

            new_name = input(Fore.GREEN + "Enter the new name (leave blank to keep current): ")
            if not new_name:
                new_name = selected_est['name']

            new_address = input(Fore.GREEN + "Enter the new address (leave blank to keep current): ")
            if not new_address:
                new_address = selected_est['street_address']

            print(Fore.CYAN + "\nReview the changes:")
            print(f"Name: {selected_est['name']} -> {new_name}")
            print(f"Address: {selected_est['street_address']} -> {new_address}")

            choice = input(Fore.GREEN + "Do you want to save the changes? (yes/no): ")
            if choice.lower() == 'yes':
                success = update_food_establishment(connection, est_id, new_name, new_address)
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