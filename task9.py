def is_palindrome(s):
    return s == s[::-1]

def main():
    print("Choose an option:")
    print("1. Check if a given string is a palindrome")
    print("2. Check if a given number is a palindrome")

    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        string = input("Enter the string: ")
        if is_palindrome(string):
            print("Palindrome")
        else:
            print("Not a Palindrome")
    elif choice == 2:
        number = input("Enter the number: ")
        if is_palindrome(number):
            print("Palindrome")
        else:
            print("Not a Palindrome")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
