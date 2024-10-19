def count_special_characters(statement):
    special_characters = 0
    # Define special characters as per your requirement
    special_characters_list = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    # Iterate through each character in the statement
    for char in statement:
        # Check if the character is in the list of special characters
        if char in special_characters_list:
            special_characters += 1

    return special_characters


# Sample Input
given_statement = "Modi Birthday @ September 17, #&$% is the wishes code for him."

# Count special characters
num_special_characters = count_special_characters(given_statement)

# Sample Output
print(f"Number of special Characters: {num_special_characters}")
