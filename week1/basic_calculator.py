
# A simple calculator program to demonstrate basic Python operations,variables, and data types.

def calculate(num1, num2, operation):
    """
    Performs arithmetic operations based on user input.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform (+, -, *, /).

    Returns:
        float: The result of the operation, or None if an error occurs.
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return num1 / num2
    else:
        print("Error: Invalid operation.")
        return None

def main():
    """
    Main function to get user input and display the result.
    """
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        result = calculate(num1, num2, operation)

        if result is not None:
            print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Error: Invalid input. Please enter numbers.")

if __name__ == "__main__":
    main()