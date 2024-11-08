def is_composite(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return False

def print_composites(a, b):
    for num in range(a, b + 1):
        if is_composite(num):
            print(num, end=" ")

# Example usage
a = 10
b = 30
print("Composite numbers between", a, "and", b, ":")
print_composites(a, b)
