def calculator():
    print("Simple Calculator")
    while True:
        try:
            op = input("Enter operation (+, -, *, /) or 'quit' to exit: ")
            if op == 'quit':
                break
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if op == '+':
                print(x + y)
            elif op == '-':
                print(x - y)
            elif op == '*':
                print(x * y)
            elif op == '/':
                if y != 0:
                    print(x / y)
                else:
                    print("Error: Division by zero.")
            else:
                print("Invalid operation.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

calculator()
