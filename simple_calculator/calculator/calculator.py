from calculator.operations import add, subtract, multiply, divide

def calculate(operation, a, b):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
        raise ValueError("Invalid operation. Use +, -, *, or /")
