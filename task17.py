def generate_sequence(M, N, K):
    if K == 0:
        return "Error: K cannot be zero."

    result = []
    if M <= N:
        current = M
        while current <= N:
            result.append(current)
            current += K
    else:
        current = M
        while current >= N:
            result.append(current)
            current -= K

    return result


def main():
    try:
        M = int(input("M = "))
        N = int(input("N = "))
        K = int(input("K = "))

        sequence = generate_sequence(M, N, K)

        if isinstance(sequence, list):
            print(", ".join(map(str, sequence)))
        else:
            print(sequence)

    except ValueError:
        print("Error: Please enter valid integer values for M, N, and K.")


# Run the main function
main()
