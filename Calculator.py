def calculator():
    print("Welcome to the Basic Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take input from the user
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

    # Validate the operation
    if operation not in ['1', '2', '3', '4']:
        print("Invalid operation. Please try again.")
        return

    try:
        # Get the numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Perform the calculation based on the operation
    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")

# Run the calculator
calculator()
