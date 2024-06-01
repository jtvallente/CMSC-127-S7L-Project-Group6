from database_commands import *

def view_all_establishments(connection):
        # Fetch all food establishments
    establishments = view_all_FE(connection)
    
    # Display all establishments
    print("List of all food establishments:")
    for i, estab in enumerate(establishments, start=1):
        print(f"{i}. {estab['name']} - {estab['city']}, {estab['province']}")
    
    while True:
        # User options
        print("\nOptions:")
        print("1. View details of a food establishment")
        print("2. Search food items by price range and/or type")
        print("3. View establishments with high average rating")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            # View details of a specific establishment
            est_id = int(input("Enter the establishment number to view details: "))
            if 1 <= est_id <= len(establishments):
                selected_establishment = establishments[est_id - 1]
                print(f"\nDetails of {selected_establishment['name']}:")
                print(f"Address: {selected_establishment['street_address']}, {selected_establishment['city']}, {selected_establishment['province']}")
                print("Food items:")
                food_items = search_food_establishment(connection, selected_establishment['establishment_id'])
                for food in food_items:
                    print(f"- {food['food_name']} (${food['price']}) - {food['type']}")
            else:
                print("Invalid establishment number.")
        
        elif choice == '2':
            # Search food items by price range and/or type
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            food_type = input("Enter food type [meat, veg, etc.](or leave blank for any type): ").strip()
            if food_type:
                food_items = search_food_item_bypriceft(connection, min_price, max_price, food_type)
            else:
                food_items = search_food_item_bypriceft(connection, min_price, max_price)
            print("\nSearch results:")
            for food in food_items:
                print(f"- {food['food_name']} (P{food['price']}) - {food['type']}")
        
        elif choice == '3':
            # View establishments with high average rating (rating >= 4)
            high_rating_establishments = view_high_rating_FE(connection)
            print("\nFood establishments with high average rating (>= 4):")
            for estab in high_rating_establishments:
                print(f"- {estab['name']} ({estab['city']}, {estab['province']}) - Average Rating: {estab['avg_rating']:.1f}")
        
        elif choice == '4':
            # Exit
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
