# Online Shopping Cart with Input Validation for Name, Price, and Quantity

class ItemToPurchase:
    def __init__(default):
        # Default constructor values if no input is provided
        default.item_name = "none"
        default.item_price = 0.0
        default.item_quantity = 0

    # Function logic to calculate total cost

    def print_item_cost(default):
        # Compute total cost and display item info in a clean format
        total = default.item_price * default.item_quantity
        print(f"{default.item_name} {default.item_quantity} @ ${default.item_price:.2f} = ${total:.2f}")


# Function to get a valid item name (must be a string and not purely numeric)
def get_valid_name(message):
    while True:
        name = input(message).strip()

        # Check if input is not empty and not only numbers
        if not name:
            print("Item name cannot be empty. Please enter a valid name.")
        elif name.isnumeric():
            print("Item name cannot be just numbers. Please enter a descriptive name.")
        else:
            return name


# Function to get a valid price (non-negative float with up to 2 decimal places)
def get_valid_price(message):
    while True:
        user_input = input(message).strip()

        try:
            value = float(user_input)

            # Reject negative numbers
            if value < 0:
                print("Price cannot be negative. Try again.")
                continue

            # Ensure no more than two decimal places
            if '.' in user_input:
                decimal_part = user_input.split('.')[1]
                if len(decimal_part) > 2:
                    print("Please enter a price with up to 2 decimal places.")
                    continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Function to get a valid quantity (non-negative integer)
def get_valid_quantity(message):
    while True:
        try:
            value = int(input(message))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("That's not a valid whole number. Try again.")


# message the user for item details with validations
def get_item_details(item_number):
    print(f"\nItem {item_number}")
    item = ItemToPurchase()
    item.item_name = get_valid_name("Enter the item name:\n")
    item.item_price = get_valid_price("Enter the item price:\n")
    item.item_quantity = get_valid_quantity("Enter the item quantity:\n")
    return item


# Main function to run the program
def main():
    print("Welcome to the Online Shopping Cart!\n")

    # Store items in a list
    cart_items = []

    # Get two items from the user
    cart_items.append(get_item_details(1))
    cart_items.append(get_item_details(2))

    # Print the breakdown of item costs
    print("\nTOTAL COST")
    grand_total = 0
    for item in cart_items:
        item.print_item_cost()
        grand_total += item.item_price * item.item_quantity

    # Display the grand total
    print(f"\nTotal: ${grand_total:.2f}")

# Run the application
main()
