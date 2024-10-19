def calculate_total_balance(denominations, counts):
    total_balance = 0
    for denomination, count in zip(denominations, counts):
        total_balance += denomination * count
    return total_balance


def main():
    denominations = []
    counts = []

    for i in range(1, 5):
        denomination = int(input(f"Enter the {i}st Denomination: "))
        count = int(input(f"Enter the {i}st Denomination number of notes: "))
        denominations.append(denomination)
        counts.append(count)

    total_balance = calculate_total_balance(denominations, counts)
    print(f"Total Available Balance in ATM: {total_balance}")


if __name__ == "__main__":
    main()
