from colorama import Fore, Style, init
from database_commands import *

init(autoreset=True)

def view_all_food_reviews(connection):
    try:
        while True:
            print(Fore.CYAN + "\nViewing all Food Reviews")
            print("1. View reviews by food establishment")
            print("2. View reviews by food item")
            print("3. Exit")

            choice = input(Fore.GREEN + "Enter your choice: ")

            if choice == '1':
                establishments = view_all_FE(connection)
                if establishments:
                    print(Fore.YELLOW + "\nList of all food establishments:")
                    for i, est in enumerate(establishments, start=1):
                        print(f"{i}. {est['name']}")

                    est_choice = int(input(Fore.GREEN + "Enter the number of the establishment: ")) - 1
                    est_id = establishments[est_choice]['establishment_id']

                    reviews = view_food_reviews_under_establishment(connection, est_id)
                    print(Fore.YELLOW + f"\nReviews for {establishments[est_choice]['name']}:")
                    if reviews:
                        for review in reviews:
                            username = get_username_by_user_id(connection, review['user_id'])
                            review_date = f"{review['review_month']:02}/{review['review_day']:02}/{review['review_year']}"
                            print(f"Review ID: {review['review_id']}, Reviewed by: {username}, Rating: {review['rating']}, Date: {review_date}, Text: {review['review_text']}")
                    else:
                        print(Fore.RED + "No reviews found for this establishment.")

                    month_choice = input(Fore.GREEN + "Do you want to see reviews within the current month? (yes/no): ")
                    if month_choice.lower() == 'yes':
                        monthly_reviews = view_reviews_month(connection)
                        print(Fore.YELLOW + "\nReviews within the current month:")
                        if monthly_reviews:
                            for review in monthly_reviews:
                                if review['establishment_id'] == est_id:
                                    username = get_username_by_user_id(connection, review['user_id'])
                                    review_date = f"{review['review_month']:02}/{review['review_day']:02}/{review['review_year']}"
                                    print(f"Review ID: {review['review_id']}, Reviewed by: {username}, Rating: {review['rating']}, Date: {review_date}, Text: {review['review_text']}")
                        else:
                            print(Fore.RED + "No reviews found for this establishment within the current month.")
                else:
                    print(Fore.RED + "No food establishments found.")

            elif choice == '2':
                food_items = view_all_FI(connection)
                if food_items:
                    print(Fore.YELLOW + "\nList of all food items:")
                    for i, item in enumerate(food_items, start=1):
                        print(f"{i}. {item['food_name']}")

                    item_choice = int(input(Fore.GREEN + "Enter the number of the food item: ")) - 1
                    item_id = food_items[item_choice]['item_id']

                    reviews = view_food_reviews_under_food(connection, item_id)
                    print(Fore.YELLOW + f"\nReviews for {food_items[item_choice]['food_name']}:")
                    if reviews:
                        for review in reviews:
                            username = get_username_by_user_id(connection, review['user_id'])
                            review_date = f"{review['review_month']:02}/{review['review_day']:02}/{review['review_year']}"
                            print(f"Review ID: {review['review_id']}, Reviewed by: {username}, Rating: {review['rating']}, Date: {review_date}, Text: {review['review_text']}")
                    else:
                        print(Fore.RED + "No reviews found for this food item.")

                    month_choice = input(Fore.GREEN + "Do you want to see reviews within the current month? (yes/no): ")
                    if month_choice.lower() == 'yes':
                        monthly_reviews = view_reviews_month(connection)
                        print(Fore.YELLOW + "\nReviews within the current month:")
                        if monthly_reviews:
                            for review in monthly_reviews:
                                if review['item_id'] == item_id:
                                    username = get_username_by_user_id(connection, review['user_id'])
                                    review_date = f"{review['review_month']:02}/{review['review_day']:02}/{review['review_year']}"
                                    print(f"Review ID: {review['review_id']}, Reviewed by: {username}, Rating: {review['rating']}, Date: {review_date}, Text: {review['review_text']}")
                        else:
                            print(Fore.RED + "No reviews found for this food item within the current month.")
                else:
                    print(Fore.RED + "No food items found.")

            elif choice == '3':
                break

            else:
                print(Fore.RED + "Invalid choice. Please try again.")

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")