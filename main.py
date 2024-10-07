"""
TODO: Implement a try again option to allow user to go again without having to restart the program
    Try creating a def function() instead
        
Calculator psuedocode

Assume the user will only enter two numbers
Prompt the user to enter the first number
Save the user's input
Prompt the user to enter the second number
Save the user's input

Ask user to choose an operation
    If user chooses addition
    Add the two numbers together
    Print the sum of the two numbers

    elif user chooses subtraction
    Subtract the second number from the first number
    Print the difference of the two numbers

    elif user chooses multiplication
    Multiply the two numbers together
    Print the product of the two numbers

    elif user chooses division
    Divide the first number by the second number
    Print the quotient of the two numbers

    else
    Print an error message stating that the operation is not supported
    Ask the user to choose a valid operation
"""
print("Welcome to the calculator program")
print("------------------------------------")

# Prompt user to enter two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Prompt user to choose an operation
operation = input("\nAvailable operations: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division \nPlease choose an option: ")

# Store variables for each operation
sum_addition = int(num1) + int(num2) # Addition
sum_subtraction = int(num1) - int(num2) # Subtraction
sum_multiplication = int(num1) * int(num2) # Multiplication
sum_division = int(num1) // int(num2) # Division with no remainder
# Ask the user if they want to perform another calculation

# Perform the operation based on user's choice
while True:
    if operation == "1":
        print(f"Sum: {sum_addition}")
        break
    elif operation == "2":
        print(f"Difference: {sum_subtraction}")
        break
    elif operation == "3":
        print(f"Product: {sum_multiplication}")
        break
    elif operation == "4":
        print(f"Quotient: {sum_division}")
        break
    else:
        print("\n\nInvalid operation chosen. Please choose again.")
        operation = input("Available operations: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division \nPlease choose an option: ")