def find_mth_max_nth_min(arr, M, N):
    if not arr:
        return "Array is empty"

    sorted_arr = sorted(arr)

    if M > len(arr) or N > len(arr) or M <= 0 or N <= 0:
        return "Invalid values for M or N"

    mth_max = sorted_arr[-M]
    nth_min = sorted_arr[N - 1]

    return mth_max, nth_min


def main():
    arr = [14, 16, 87, 36, 25, 89, 34]
    M = 1
    N = 3

    result = find_mth_max_nth_min(arr, M, N)
    if isinstance(result, str):
        print(result)
    else:
        mth_max, nth_min = result
        sum_result = mth_max + nth_min
        difference_result = mth_max - nth_min

        print(f"{M}st Maximum Number = {mth_max}")
        print(f"{N}rd Minimum Number = {nth_min}")
        print(f"Sum = {sum_result}")
        print(f"Difference = {difference_result}")


if __name__ == "__main__":
    main()
