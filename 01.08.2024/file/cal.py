def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Cannot divide by zero'
    return x / y

def main():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice in ['1', '2', '3', '4']:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if choice == '1':
                print(f"Result: {add(x, y)}")
            elif choice == '2':
                print(f"Result: {subtract(x, y)}")
            elif choice == '3':
                print(f"Result: {multiply(x, y)}")
            elif choice == '4':
                print(f"Result: {divide(x, y)}")
        elif choice == '5':
            break

if __name__ == '__main__':
    main()
