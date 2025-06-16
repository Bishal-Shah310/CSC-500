# Part 2: Multiplication and Division program

# define main function for user input, operation logic, and exception handling
def main():
    print("\nPlease input two numbers.")

    try:
        # get user input and convert them to int; store them in num1 and num2 variables
        num1 = int(input("\nEnter num1: "))
        num2 = int(input("\nEnter num2: "))

        # multiply num1 and num2 and store it in multiply variable
        multiply = num1 * num2

        # division logic with error validation check for if denominator equals zero
        if num2 == 0:
            division_logic = "Error, Cannot divide by zero."
        else:
            division_logic = num1 / num2

        # output the results
        print("\nMultiplication:", multiply)
        print("Division:", division_logic)

    # exception Handling for invalid inputs
    except ValueError:
        print("Invalid input. Please input two numbers.")


# call main
if __name__ == "__main__":
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
