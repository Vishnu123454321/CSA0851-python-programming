def count_spaces_lines_vowels_consonants(filename):
    vowels = "aeiouAEIOU"
    spaces_count = 0
    lines_count = 0
    vowels_count = 0
    consonants_count = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                lines_count += 1
                for char in line:
                    if char == ' ':
                        spaces_count += 1
                    elif char.isalpha():
                        if char in vowels:
                            vowels_count += 1
                        else:
                            consonants_count += 1

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

    return spaces_count, lines_count, vowels_count, consonants_count


def main():
    try:
        filename = input("Enter the filename: ")
        spaces_count, lines_count, vowels_count, consonants_count = count_spaces_lines_vowels_consonants(filename)

        print(f"Number of spaces: {spaces_count}")
        print(f"Number of lines: {lines_count}")
        print(f"Number of vowels: {vowels_count}")
        print(f"Number of consonants: {consonants_count}")

    except Exception as e:
        print(f"Error: {e}")


# Run the main function
main()
