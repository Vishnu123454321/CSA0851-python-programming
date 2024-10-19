def count_vowels_and_consonants(statement):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0

    # Count vowels and consonants
    for char in statement:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    return num_vowels, num_consonants


def main():
    try:
        statement = input("Enter a statement: ")

        # Get counts of vowels and consonants
        num_vowels, num_consonants = count_vowels_and_consonants(statement)

        # Print the counts
        print(f"Number of vowels = {num_vowels}")
        print(f"Number of consonants = {num_consonants}")

        # Determine which count is maximum
        if num_vowels > num_consonants:
            print("Vowels are maximum.")
        elif num_consonants > num_vowels:
            print("Consonants are maximum.")
        else:
            print("Both vowels and consonants are equal.")

    except Exception as e:
        print(f"Error: {e}")


# Run the main function
main()
