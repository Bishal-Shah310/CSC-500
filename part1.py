# Part 1: Addition and Subtraction

# define main function for user input, operation logic, and exception handling
def main():
    print("\nPlease input two numbers.")

    try:
        # get user input and convert the string input as an int
        num1 = int(input("\nEnter num1: "))
        num2 = int(input("\nEnter num2: "))

        # add the two input and store in add variable to call later
        add = num1 + num2

        # subtract the two input and store in subtract variable to call later
        subtract = num1 - num2

        # display the results
        print("\nAddition:", add)
        print("Subtraction:", subtract)

    # exception Handling for non-numeric input
    except ValueError:
        print("Invalid input. Please input two numbers.")


# call main
if __name__ == "__main__":
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
