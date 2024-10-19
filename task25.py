def reverse_words(s):
    # Split the string into words based on whitespace
    words = s.split()

    # Reverse the list of words
    reversed_words = words[::-1]

    # Join the reversed words into a single string with spaces
    reversed_string = " ".join(reversed_words)

    return reversed_string


def main():
    try:
        s = input("Enter a string: ")
        reversed_string = reverse_words(s)
        print("Reversed words:", reversed_string)

    except Exception as e:
        print(f"Error: {e}")


# Run the main function
main()

