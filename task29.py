def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(f"{j * 0.1:.1f}", end=" ")
        print()

# Test the function with 4 rows as given in the example
print_pattern(4)
