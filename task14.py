def remove_duplicates(arr):
    if not arr:
        return []

    # Initialize variables
    result = [arr[0]]

    # Traverse the sorted array and remove duplicates
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result.append(arr[i])

    return result


# Sample Input
array = [15, 14, 25, 14, 32, 14, 31]

# Sorting the array (assuming the input is sorted as per the problem statement)
array.sort()

# Removing duplicates
result_array = remove_duplicates(array)

# Sample Output
print("Sorted Array without duplicates:", result_array)
