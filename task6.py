def reverse_number(number):
    try:
        num = int(number)
        if num < 0:
            is_negative = True
            num = -num
        else:
            is_negative = False

        reversed_num = 0
        while num > 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num = num // 10

        if is_negative:
            reversed_num = -reversed_num

        return reversed_num

    except ValueError:
        return "Invalid input: Not a valid integer"

def main():
    number = input("Enter the number: ")
    result = reverse_number(number)
    if isinstance(result, int):
        print(f"Reverse Number: {result}")
    else:
        print(result)

if __name__ == "__main__":
    main()
