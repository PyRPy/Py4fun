from calculator.calculator import calculate 

def main():
    print("Simple calculator")
    while True:
        try:
            a = float(input("enter first number: "))
            op = input("enter operation (+, -, *, /): ")
            b = float(input("enter second number: "))

            result = calculate(op, a, b)
            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")

        cont = input("Do you want to calculate again? (y/n): ").strip().lower()
        while cont not in ["y", "n"]:
            cont = input("Invalid input! Please enter 'y' to continue or 'n' to exit: ").strip().lower()
        
        if cont == 'n':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main() 