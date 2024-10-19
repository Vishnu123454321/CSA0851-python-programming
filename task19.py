def sort_names(names, order):
    names_list = [name.strip() for name in names.split(',')]

    if order.upper() == 'A':
        sorted_names = sorted(names_list)
    elif order.upper() == 'D':
        sorted_names = sorted(names_list, reverse=True)
    else:
        return "Invalid order choice. Please choose 'A' for Ascending or 'D' for Descending."

    return sorted_names


def main():
    try:
        # Input names and order choice
        names = input("Enter a comma-separated list of names: ")
        order = input("Order (A for Ascending, D for Descending): ").strip()

        # Sort names based on user choice
        sorted_names = sort_names(names, order)

        # Print the sorted names
        if isinstance(sorted_names, list):
            print("Sorted names:", " ".join(sorted_names))
        else:
            print(sorted_names)

    except Exception as e:
        print(f"Error: {e}")


# Run the main function
main()
