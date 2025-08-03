# Online Shopping Cart

# ITEM CLASS
class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0, description="no description"):
        # Initialize item attributes with default values
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    # Method to print the cost of the item in the required format
    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")

    # Method to print the description of the item
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


# SHOPPING CART CLASS
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # Initialize cart with customer name, date, and empty list of items
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Method to add an item object to the cart
    def add_item(self, item):
        self.cart_items.append(item)

    # Method to remove an item from the cart by name
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    # Method to modify an existing item in the cart
    def modify_item(self, modified_item):
        found = False
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                found = True
                # Update only fields that are not default values
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                if modified_item.item_description != "no description":
                    item.item_description = modified_item.item_description
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    # Return total quantity of items in the cart
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    # Return total cost of all items in the cart
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    # Print all items and total cost in cart
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    # Print descriptions of all items in the cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


# INPUT VALIDATION FUNCTIONS

# Validate customer name (non-empty, not numeric)
def get_valid_customer_name(message):
    while True:
        name = input(message).strip()
        if not name:
            print("Customer name cannot be empty. Please enter a valid name.")
        elif name.isnumeric():
            print("Customer name cannot be only numbers. Enter a valid name.")
        else:
            return name


# Validate date in format: Month Day, Year
def get_valid_date(message):
    while True:
        date = input(message).strip()
        if not date:
            print("Date cannot be empty. Please enter a valid date (e.g., February 1, 2025).")
        elif "," not in date or not any(month in date for month in
                                        ["January", "February", "March", "April", "May", "June",
                                         "July", "August", "September", "October", "November", "December"]):
            print("Invalid format. Use format like: February 1, 2025")
        else:
            return date


# Validate item name
def get_valid_name(message):
    while True:
        name = input(message).strip()
        if not name:
            print("Item name cannot be empty. Please enter a valid name.")
        elif name.isnumeric():
            print("Item name cannot be just numbers. Please enter a descriptive name.")
        else:
            return name


# Validate description
def get_valid_description(message):
    while True:
        desc = input(message).strip()
        if not desc:
            print("Description cannot be empty. Please enter a valid description.")
        else:
            return desc


# Validate price
def get_valid_price(message):
    while True:
        user_input = input(message).strip()
        try:
            value = float(user_input)
            if value < 0:
                print("Price cannot be negative. Try again.")
                continue
            if '.' in user_input and len(user_input.split('.')[1]) > 2:
                print("Please enter a price with up to 2 decimal places.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Validate quantity
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


# MENU FUNCTION

def print_menu(cart: object) -> object:
    choice = ""
    while choice != "q":
        print("""
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option:
        """, end="")

        choice = input().lower()

        # Add item to cart
        if choice == "a":
            name = get_valid_name("Enter the item name:\n")
            description = get_valid_description("Enter the item description:\n")
            price = get_valid_price("Enter the item price:\n")
            quantity = get_valid_quantity("Enter the item quantity:\n")
            cart.add_item(ItemToPurchase(name, price, quantity, description))

        # Remove item from cart
        elif choice == "r":
            name = get_valid_name("Enter name of item to remove:\n")
            cart.remove_item(name)

        # Change item quantity
        elif choice == "c":
            name = get_valid_name("Enter the item name to modify:\n")

            # Check existence before asking for quantity
            if not any(item.item_name == name for item in cart.cart_items):
                print("Item not found in cart. Nothing modified.")
            else:
                quantity = get_valid_quantity("Enter the new quantity:\n")
                cart.modify_item(ItemToPurchase(name, 0, quantity))


        # Output item descriptions
        elif choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        # Output shopping cart
        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        # Invalid menu option
        elif choice != "q":
            print("Invalid option, try again.")


# MAIN FUNCTION

def main():
    try:
        # Ask for customer details
        customer_name = get_valid_customer_name("Enter customer's name:\n")
        current_date = get_valid_date("Enter today's date:\n")

        # Display confirmation
        print(f"Customer name: {customer_name}")
        print(f"Today's date: {current_date}")

        # Create ShoppingCart object and run menu
        cart = ShoppingCart(customer_name, current_date)
        print_menu(cart)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
main()
