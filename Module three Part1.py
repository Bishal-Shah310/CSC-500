# Program to calculate the total cost of a meal purchased
while True:
    try:
        cost_of_meal = float(input("Please enter the cost of the meal: $"))
        # Input validation
        if cost_of_meal < 1:
            print("Cost cannot be null or negative. Please enter the cost of a meal.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
# Tip logic
tip_cost = cost_of_meal * 0.18

# Sales tax logic
sales_tax = cost_of_meal * 0.07

# Total cost logic
total_cost_of_meal = cost_of_meal + tip_cost + sales_tax

# Output result
print(f"Cost Of Meal: ${cost_of_meal:.2f}")
print(f"Tip (18%): ${tip_cost:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total Cost: ${total_cost_of_meal:.2f}")