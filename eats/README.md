## Hult Eats — Requirements

Your program should:

1. Allow users to select a restaurant from a predefined list
2. Display the menu for the selected restaurant
3. Let users order multiple items with quantities
4. Calculate the subtotal for all ordered items
5. Add appropriate delivery fee based on distance
6. Calculate tax (8% of subtotal)
7. Calculate final total and split bill among specified number of people

## Getting Started

1. Download the starter code provided (food_delivery_starter.py)
2. Read through the existing code and comments
3. Look for `TODO` comments that indicate where you need to add code
4. Test your program after implementing each section

## Implementation Steps

### Part 1: Restaurant Selection

- Review the provided restaurant dictionaries
- Implement the restaurant selection validation
- Display the menu for the selected restaurant

### Part 2: Order Processing

- Create a loop to accept multiple item orders
- Validate that ordered items exist in the menu
- Keep track of ordered items and their quantities
- Calculate running total

### Part 3: Delivery and Total Calculation

- Implement delivery fee selection
- Calculate tax
- Compute final total
- Implement bill splitting

## Testing Your Implementation

Test your program with these scenarios:

1. Basic Order:
    - Select "burger_place"
    - Order: 2 burgers, 1 fries
    - Delivery: 0-2km
    - Split between 2 people
2. Invalid Inputs:
    - Try ordering an item not on the menu
    - Enter invalid distance range
    - Enter 0 for bill splitting
