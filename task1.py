def reverse_string(word):
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word

# Test cases
test_cases = ["TEMPLE", "SIGN UP", "AT-LEAST", "1245", "!@#$%", "145*999=144855"]

for test in test_cases:
    print(f"Original String: {test}")
    print(f"Reversed String: {reverse_string(test)}")
    print()
