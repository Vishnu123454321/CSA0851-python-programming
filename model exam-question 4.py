def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(m, n):
    for num in range(m, n + 1):
        if is_prime(num):
            print(num, end=" ")

# Example usage
m = 10
n = 50
print("Prime numbers between", m, "and", n, ":")
print_primes(m, n)
