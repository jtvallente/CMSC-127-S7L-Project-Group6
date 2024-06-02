from colorama import Fore, Style, init
from database_commands import *
from datetime import datetime

init(autoreset=True)

def edit_food_review(connection, user_id):
    try:
        while True:
            print(Fore.CYAN + "\nEdit Food Review")
            
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

            review_choice = int(input(Fore.GREEN + "Enter the number of the review you want to edit: ")) - 1
            review_id = reviews[review_choice]['review_id']

            new_review_text = input(Fore.GREEN + "Enter the new review text (leave blank to keep current): ")
            new_rating = input(Fore.GREEN + "Enter the new rating (1-5, leave blank to keep current): ")
            
            # Check if the user entered new review text or rating
            new_review_text = new_review_text.strip() if new_review_text.strip() else reviews[review_choice]['review_text']
            new_rating = int(new_rating.strip()) if new_rating.strip() else reviews[review_choice]['rating']

            print(Fore.CYAN + f"\nReview changes for Review ID: {review_id}")
            print(Fore.YELLOW + f"New Review Text: {new_review_text}")
            print(Fore.YELLOW + f"New Rating: {new_rating}")
            
            confirm = input(Fore.GREEN + "Do you want to save the changes? (yes/no): ").strip().lower()
            if confirm == 'yes':
                success = update_food_review(connection, review_id, new_review_text, new_rating)
                if success:
                    print(Fore.GREEN + "Review updated successfully!")
                else:
                    print(Fore.RED + "Failed to update the review.")
            else:
                print(Fore.YELLOW + "Edit cancelled.")

            another = input(Fore.GREEN + "Do you want to edit another review? (yes/no): ").strip().lower()
            if another != 'yes':
                break

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")