def is_palindrome(x):
    return str(x) == str(x)[::-1]

# Example usage
x = 121
print(f"Is {x} a palindrome?", is_palindrome(x))
