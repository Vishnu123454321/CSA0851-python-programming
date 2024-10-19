def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()


def main():
    try:
        rows = int(input("Enter the number of rows: "))
        if rows <= 0:
            print("Number of rows should be greater than zero.")
        else:
            print_pattern(rows)

    except ValueError:
        print("Error: Please enter a valid integer for the number of rows.")


# Run the main function
main()
