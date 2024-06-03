from database_commands import *
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def view_all_establishments(connection):
    # Fetch all food establishments
    establishments = view_all_FE(connection)

    if establishments:
        # Display all establishments
        print(Fore.CYAN + Style.BRIGHT + "List of all food establishments:")
        for i, estab in enumerate(establishments, start=1):
            print(Fore.YELLOW + f"{i}. {estab['name']} - {estab['city']}, {estab['province']}")
        
        while True:
            # User options
            print(Fore.GREEN + "\nOptions:")
            print("1. View details of a food establishment")
            print("2. Search food items by price range and/or type")
            print("3. View establishments with high average rating")
            print("4. Exit")
            
            choice = input(Fore.CYAN + "Enter your choice (1-4): ")
            
            if choice == '1':
                # View details of a specific establishment
                est_id = int(input(Fore.CYAN + "Enter the establishment number to view details: "))
                if 1 <= est_id <= len(establishments):
                    selected_establishment = establishments[est_id - 1]
                    print(Fore.CYAN + Style.BRIGHT + f"\nDetails of {selected_establishment['name']}:")
                    print(f"Address: {selected_establishment['street_address']}, {selected_establishment['city']}, {selected_establishment['province']}")
                    print(Fore.MAGENTA + "Food items:")

                    est_id = selected_establishment['establishment_id']
                    while True:
                        print(Fore.GREEN + "\nOptions:")
                        print("1. View all food items")
                        print("2. View food items by type")
                        print("3. View food items ordered by price (ascending)")
                        print("4. View food items ordered by price (descending)")
                        print("5. Back to main menu")

                        sub_choice = input(Fore.CYAN + "Enter your choice (1-5): ")

                        if sub_choice == '1':
                            # Fetch all food items
                            food_items = view_food_items(connection, est_id)
                        elif sub_choice == '2':
                            food_type = input(Fore.CYAN + "Enter food type [meat, veg, etc.]: ").strip()
                            food_items = view_food_items(connection, est_id, type=food_type)
                        elif sub_choice == '3':
                            food_items = view_food_items(connection, est_id, price=1)
                        elif sub_choice == '4':
                            food_items = view_food_items(connection, est_id, price=2)
                        elif sub_choice == '5':
                            break
                        else:
                            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 5.")
                            continue

                        # Display food items
                        if food_items:
                            print(Fore.MAGENTA + "\nFood items:")
                            for food in food_items:
                                print(f"- {food['food_name']} (₱{food['price']}) - {food['type']}")
                        else:
                            print(Fore.RED + "No food items found for this establishment.")
                else:
                    print(Fore.RED + "Invalid establishment number.")
            
            elif choice == '2':
                # Search food items by price range and/or type
                min_price = float(input(Fore.CYAN + "Enter minimum price: "))
                max_price = float(input(Fore.CYAN + "Enter maximum price: "))
                food_type = input(Fore.CYAN + "Enter food type [meat, veg, etc.](or leave blank for any type): ").strip()
                if food_type:
                    food_items = view_food_items(connection, None, type=food_type, price_range={'lowest': min_price, 'highest': max_price})
                else:
                    food_items = view_food_items(connection, None, price_range={'lowest': min_price, 'highest': max_price})
                print(Fore.MAGENTA + "\nSearch results:")
                for food in food_items:
                    print(f"- {food['food_name']} (₱{food['price']}) - {food['type']}")
            
            elif choice == '3':
                # View establishments with high average rating (rating >= 4)
                high_rating_establishments = view_high_rating_FE(connection)
                print(Fore.CYAN + "\nFood establishments with high average rating (>= 4):")
                for estab in high_rating_establishments:
                    print(f"- {estab['name']} ({estab['city']}, {estab['province']}) - Average Rating: {estab['avg_rating']:.1f}")
            
            elif choice == '4':
                # Exit
                print(Fore.GREEN + "Exiting...")
                break
            
            else:
                print(Fore.RED + "Invalid choice. Please enter a number between 1 and 4.")

    else:
        print(Fore.RED + "No food establishment found.")