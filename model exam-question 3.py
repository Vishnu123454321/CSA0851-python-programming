def is_tech_number(num):
    str_num = str(num)
    if len(str_num) % 2 == 0:
        mid = len(str_num) // 2
        left_half = int(str_num[:mid])
        right_half = int(str_num[mid:])
        return left_half + right_half == num
    return False

def print_tech_numbers():
    for num in range(1000, 10000):
        if is_tech_number(num):
            print(num, end=" ")

# Example usage
print("4-digit Tech numbers:")
print_tech_numbers()
