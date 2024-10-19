def perform_operation(X, N, choice):
    result = 0
    if choice == 1:
        result = X + N
    elif choice == 2:
        result = X - N
    elif choice == 3:
        result = X * N
    elif choice == 4:
        if N != 0:
            result = X / N
        else:
            return "Error: Division by zero."
    else:
        return "Invalid choice. Please choose 1 for Addition, 2 for Subtraction, 3 for Multiplication, or 4 for Division."

    return f"Operation result = {result}"


def main():
    try:
        X = float(input("Enter value for X: "))
        N = float(input("Enter value for N: "))
        choice = int(input("Enter choice (1: Addition, 2: Subtraction, 3: Multiplication, 4: Division): "))

        result = perform_operation(X, N, choice)
        print(result)

    except ValueError:
        print("Error: Please enter valid numerical values for X, N, and choice.")
    except Exception as e:
        print(f"Error: {e}")


# Run the main function
main()
