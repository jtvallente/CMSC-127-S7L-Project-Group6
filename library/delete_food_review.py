from colorama import Fore, Style, init
from database_commands import *

init(autoreset=True)

def delete_user_food_review(connection, user_id):
    try:
        while True:
            print(Fore.CYAN + "\nDelete Food Review")
            
            reviews = get_user_reviews(connection, user_id)
            if not reviews:
                print(Fore.RED + "No reviews found.")
                return
            
            print(Fore.YELLOW + "\nList of all your reviews:")
            for i, review in enumerate(reviews, start=1):
                establishment_name = get_estab_name_by_id(connection, review['establishment_id'])
                food_item_name = get_food_name_by_id(connection, review['item_id']) if review['item_id'] else "N/A"
                review_date = f"{review['review_month']:02}/{review['review_day']:02}/{review['review_year']}"
                print(f"{i}. Review ID: {review['review_id']}, Establishment: {establishment_name}, "
                      f"Food Item: {food_item_name}, Rating: {review['rating']}, Date: {review_date}")
                print(f"   Review Text: {review['review_text']}")

            review_choice = int(input(Fore.GREEN + "Enter the number of the review you want to delete: ")) - 1
            review_id = reviews[review_choice]['review_id']

            confirm = input(Fore.GREEN + "Are you sure you want to delete this review? (yes/no): ")

            if confirm.lower() == 'yes':
                success = delete_food_review(connection, review_id)
                if success:
                    print(Fore.GREEN + "Review deleted successfully!")
                else:
                    print(Fore.RED + "Failed to delete the review.")
            else:
                print(Fore.YELLOW + "Deletion canceled.")

            another = input(Fore.GREEN + "Do you want to delete another review? (yes/no): ")
            if another.lower() != 'yes':
                break

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")