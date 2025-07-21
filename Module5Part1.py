def main():
    rainfall_data = {}  # Dictionary to store rainfall data
    total_rainfall = 0.0
    total_months = 0

    # Input: Ask for number of years with validation
    while True:
        try:
            years = int(input("Enter the number of years to collect rainfall data: "))
            if years < 1:
                print("Error: Number of years must be at least 1.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Loop through each year
    for year in range(1, years + 1):
        print(f"\nEntering data for Year {year}:")
        rainfall_data[year] = []  # Initialize list for this year's monthly rainfall

        # Loop through 12 months
        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"  Month {month}: Enter rainfall in inches: "))
                    if rainfall < 0:
                        print("Rainfall cannot be negative. Try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Store and accumulate
            rainfall_data[year].append(rainfall)
            total_rainfall += rainfall
            total_months += 1

    # Compute average rainfall
    average_rainfall = total_rainfall / total_months if total_months else 0

    # Display final results
    print(f"Total months rainfall recorded : {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")


# Run the program
main()
