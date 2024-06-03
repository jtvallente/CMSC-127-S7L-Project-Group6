from colorama import Fore, Style, init
from database_commands import *

init(autoreset=True)

def delete_food_establishment_menu(connection, user_id):
    try:
        while True:
            print(Fore.CYAN + "\nDelete a Food Establishment")

            establishment_id = get_establishment_id_by_user_id(connection, user_id)
            establishment = search_food_establishment(connection, establishment_id)
            if not establishment:
                print(Fore.RED + "\nNo food establishment found.\n")
                return

            print(Fore.YELLOW + "\nYour food establishment:")
            print(f" -  {establishment['name']}")

            establishment_name = input(Fore.GREEN + "Enter the name of the establishment to delete: ")

            # Check if the entered establishment name matches the existing establishment
            if establishment['name'].lower() == establishment_name.lower():
                confirm = input(Fore.RED + f"Are you sure you want to delete '{establishment_name}' establishment? "
                                             f"This will also delete all associated food items and reviews. "
                                             f"Type 'yes' to confirm or 'no' to cancel: ")

                if confirm.lower() == 'yes':
                    reviews_deleted = delete_reviews_under_establishment(connection, establishment_id)
                    items_deleted = delete_items_under_establishment(connection, establishment_id)
                    establishment_deleted = delete_food_establishment(connection, establishment_id)

                    if establishment_deleted:
                        print(Fore.GREEN + "Food establishment and all associated items and reviews deleted successfully!")
                    else:
                        print(Fore.RED + "Failed to delete the food establishment.")
                else:
                    print(Fore.YELLOW + "Deletion cancelled. Returning to the dashboard.")
                    return
            else:
                print(Fore.RED + "No matching establishment found. Please try again.")

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
