# Restaurant menus with prices
restaurants = {
    "five_guys": {
        "burger": 12.99,
        "fries": 4.99,
        "shake": 5.99,
        "wings": 10.99
    },
    "a4_pizza": {
        "margherita": 14.99,
        "pepperoni": 16.99,
        "veggie": 15.99,
        "garlic_bread": 4.99
    },
    "sushi_bar": {
        "california_roll": 8.99,
        "dragon_roll": 14.99,
        "miso_soup": 3.99,
        "gyoza": 6.99
    }
}

def display_restaurants():
    # Display available restaurants
    print("\nAvailable restaurants:")
    for rest in restaurants.keys():
        print(f"- {rest.replace('_', ' ').title()}")
    
def display_menu(restaurant):
    """Display menu for selected restaurant"""
    print(f"\n=== {restaurant.replace('_', ' ').upper()} MENU ===")
    for item, price in restaurants[restaurant].items():
        # Format item name and price nicely
        formatted_item = item.replace('_', ' ').title()
        print(f"{formatted_item:<20} ${price:>6.2f}")

def calculate_order():
    """Calculate total cost including delivery and split bill"""
    # Initialize order tracking
    order = []
    total = 0
    
    # Display restaurant list from dictinary
    display_restaurants()
    
    # Get restaurant selection with validation
    while True:
        restaurant = input("\nEnter restaurant name: ").lower()
        restaurant = restaurant.replace(" ", "_")
        if restaurant in restaurants:
            break
        print("Sorry, that restaurant is not available. Please try again.")
    
    # Display menu and take order
    display_menu(restaurant)
    
    #Get the order with input validation
    while True:
        print("\nEnter item name to order (or 'done' to finish):")
        item = input("—> ").lower()
        item = item.replace(" ", "_")
        
        # Check if done ordering
        if item == 'done':
            if not order:
                print("You haven't ordered anything. Please order at least one item.")
                continue
            break
        
        # Validate item exists in menu
        if item not in restaurants[restaurant]:
            print("Sorry, that item is not on the menu. Please try again.")
            continue
        
        # Get quantity with input validation
        while True:
            try:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        # Calculate item total and add to order
        price = restaurants[restaurant][item] * quantity
        order.append((item, quantity, price))
        total += price

    
    # Calculate final totals
    tax_rate = 0.08  # assume an 8% tax
    tax = total * tax_rate
    final_total = total + tax
    
    # Display order summary
    print("\n=== ORDER SUMMARY ===")
    for item, quantity, price in order:
        formatted_item = item.replace('_', ' ').title()
        print(f"{formatted_item} x{quantity}: ${price:.2f}")
    
    print(f"\nSubtotal: ${total:.2f}")
    print(f"Tax (8%): ${tax:.2f}")
    print(f"Final Total: ${final_total:.2f}")
    
    # Bill splitting with validation
    while True:
        try:
            split = int(input("\nSplit between how many people? "))
            if split <= 0:
                print("Please enter a positive number of people.")
                continue
            per_person = final_total / split
            print(f"\nAmount per person: ${per_person:.2f}")
            break
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main program loop to allow multiple orders"""
    while True:
        print("\nWelcome to Hult Eats!")
        calculate_order()
        
        # Ask if user wants another order
        another = input("\nPlace another order? (y/n): ").lower()
        if another != 'y':
            print("Thank you for using Hult Eats!!")
            break

if __name__ == "__main__":
    main()
