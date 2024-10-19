def calculate_pow(x, n):
    return x ** n

def add(x, n):
    return x + n

def subtract(x, n):
    return x - n

def multiply(x, n):
    return x * n

def divide(x, n):
    if n != 0:
        return x / n
    else:
        return "Error! Division by zero."

def main():
    try:
        x = float(input("Enter value for X: "))
        n = float(input("Enter value for N: "))
        choice = int(input("Enter choice (1: Pow, 2: Add, 3: Subtract, 4: Multiply, 5: Divide): "))

        if choice == 1:
            result = calculate_pow(x, n)
            print(f"Pow({x}, {n}) = {result}")
        elif choice == 2:
            result = add(x, n)
            print(f"Add({x}, {n}) = {result}")
        elif choice == 3:
            result = subtract(x, n)
            print(f"Subtract({x}, {n}) = {result}")
        elif choice == 4:
            result = multiply(x, n)
            print(f"Multiply({x}, {n}) = {result}")
        elif choice == 5:
            result = divide(x, n)
            print(f"Divide({x}, {n}) = {result}")
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input! Please enter numeric values for X and N.")

if __name__ == "__main__":
    main()
