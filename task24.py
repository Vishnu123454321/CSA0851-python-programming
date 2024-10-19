def calculate_average(numbers):
    positive_sum = 0
    positive_count = 0
    negative_sum = 0
    negative_count = 0

    for num in numbers:
        if num == -1:
            break
        elif num > 0:
            positive_sum += num
            positive_count += 1
        elif num < 0:
            negative_sum += num
            negative_count += 1

    if positive_count > 0:
        avg_positive = positive_sum / positive_count
    else:
        avg_positive = 0

    if negative_count > 0:
        avg_negative = negative_sum / negative_count
    else:
        avg_negative = 0

    return avg_positive, avg_negative


def main():
    try:
        numbers = []

        while True:
            num = float(input("Enter the number (enter -1 to exit): "))
            if num == -1:
                break
            numbers.append(num)

        avg_positive, avg_negative = calculate_average(numbers)

        print(f"The average of negative numbers is: {avg_negative}")
        print(f"The average of positive numbers is: {avg_positive}")

    except ValueError:
        print("Error: Please enter a valid number.")
    except ZeroDivisionError:
        print("Error: Cannot calculate average. Division by zero error.")
    except Exception as e:
        print(f"Error: {e}")


# Run the main function
main()
