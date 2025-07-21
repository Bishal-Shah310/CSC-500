def main():
    # Dictionary mapping minimum books to points
    points_award = {
        0: 0,
        2: 5,
        4: 15,
        6: 30,
        8: 60
    }

    # Input: Ask for number of books with validation
    while True:
        try:
            books = int(input("Enter the number of books purchased this month: "))
            if books < 0:
                print("Number of books cannot be negative. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

        # Determine points awarded based on rules
        # We start by checking the highest thresholds first (e.g., 8, 6, 4, ...)
        # 'sorted(points_award.keys(), reverse=True)' sorts the list in reverse: [8, 6, 4, 2, 0]
        # So we can match the highest possible reward the user qualifies for
    for min_books in sorted(points_award.keys(), reverse=True):
        # If the number of books the user entered is greater than or equal to this threshold
        if books >= min_books:
            # Then assign the corresponding points
            points_awarded = points_award[min_books]
            break

    # Output the result
    print(f"Books purchased : {books}")
    print(f"Points awarded  : {points_awarded}")

# Run the program
main()
