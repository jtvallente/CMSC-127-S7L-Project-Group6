from colorama import Fore, Style, init
from database_commands import *
from unique_id_generator import generate_unique_id
from datetime import datetime

init(autoreset=True)

def add_food_review(connection, user_id):
    try:
        while True:
            print(Fore.CYAN + "\nAdd a Food Review")
            
            establishments = view_all_FE(connection)
            if not establishments:
                print(Fore.RED + "No food establishments found.")
                return
            
            print(Fore.YELLOW + "\nList of all food establishments:")
            for i, est in enumerate(establishments, start=1):
                print(f"{i}. {est['name']}")

            est_choice = int(input(Fore.GREEN + "Enter the number of the establishment: ")) - 1
            est_id = establishments[est_choice]['establishment_id']
            
            print(Fore.CYAN + "\n1. Review the establishment directly")
            print("2. Review a food item from the establishment")
            review_choice = input(Fore.GREEN + "Enter your choice: ")

            item_id = None
            if review_choice == '2':
                food_items = view_food_items_from_est(connection, est_id)
                if not food_items:
                    print(Fore.RED + "No food items found for this establishment.")
                    continue
                
                print(Fore.YELLOW + "\nList of all food items in the establishment:")
                for i, item in enumerate(food_items, start=1):
                    print(f"{i}. {item['food_name']}")

                item_choice = int(input(Fore.GREEN + "Enter the number of the food item: ")) - 1
                item_id = food_items[item_choice]['item_id']

            review_text = input(Fore.GREEN + "Enter your review text: ")
            rating = int(input(Fore.GREEN + "Enter your rating (1-5): "))
            while rating < 1 or rating > 5:
                print(Fore.RED + "Rating must be between 1 and 5.")
                rating = int(input(Fore.GREEN + "Enter your rating (1-5): "))

            current_date = datetime.now()
            review_month = current_date.month
            review_day = current_date.day
            review_year = current_date.year

            review_id = generate_unique_id()

            success = add_food_review_db(connection, review_id, user_id, est_id, item_id, review_text, rating, review_month, review_day, review_year)
            if success:
                print(Fore.GREEN + "Review added successfully!")
            else:
                print(Fore.RED + "Failed to add the review.")
            
            another = input(Fore.GREEN + "Do you want to add another review? (yes/no): ")
            if another.lower() != 'yes':
                break

    except Error as err:
        print(Fore.RED + f"Error: '{err}'")