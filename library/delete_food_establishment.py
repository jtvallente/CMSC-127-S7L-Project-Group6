from colorama import Fore, Style, init
from database_commands import *

init(autoreset=True)

def delete_food_establishment_menu(connection):
    try:
        while True:
            print(Fore.CYAN + "\nDelete a Food Establishment")

            establishments = view_all_FE(connection)
            if not establishments:
                print(Fore.RED + "No food establishments found.")
                return

            print(Fore.YELLOW + "\nList of all food establishments:")
            for i, est in enumerate(establishments, start=1):
                print(f"{i}. {est['name']}")

            est_choice = int(input(Fore.GREEN + "Enter the number of the establishment to delete: ")) - 1
            est_id = establishments[est_choice]['establishment_id']

            confirm = input(Fore.RED + "Are you sure you want to delete this establishment? This will also delete all associated food items and reviews. Type 'yes' to confirm or 'no' to cancel: ")

            if confirm.lower() == 'yes':
                reviews_deleted = delete_reviews_under_establishment(connection, est_id)
                items_deleted = delete_items_under_establishment(connection, est_id)
                establishment_deleted = delete_food_establishment(connection, est_id)

                if establishment_deleted:
                    print(Fore.GREEN + "Food establishment and all associated items and reviews deleted successfully!")
                else:
                    print(Fore.RED + "Failed to delete the food establishment.")
            else:
                print(Fore.YELLOW + "Deletion cancelled. Returning to the dashboard.")
                return

            another = input(Fore.GREEN + "Do you want to delete another establishment? (yes/no): ")
            if another.lower() != 'yes':
                break

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")

def delete_reviews_under_establishment(connection, establishment_id):
    reviews = view_food_reviews_under_establishment(connection, establishment_id)
    for review in reviews:
        delete_food_review(connection, review['review_id'])
    return True

def delete_items_under_establishment(connection, establishment_id):
    items = view_food_items_from_est(connection, establishment_id)
    for item in items:
        delete_food_item(connection, item['item_id'])
    return True