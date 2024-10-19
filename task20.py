def multiplication_table(M, N):
    # Adjust N to be positive if it's negative
    if N < 0:
        N = abs(N)

    # Generate and print multiplication table
    for i in range(1, N + 1):
        product = i * M
        print(f"{i}x{M}={product}")


def main():
    try:
        # Input values of M and N
        M = int(input("M = "))
        N = int(input("N = "))

        # Print multiplication table
        multiplication_table(M, N)

    except ValueError:
        print("Error: Please enter valid integer values for M and N.")


# Run the main function
main()
