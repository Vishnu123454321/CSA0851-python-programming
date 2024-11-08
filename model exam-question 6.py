def search_matrix(matrix, target):
    if not matrix:
        return False
    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1  # Start from top-right corner

    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left if current number is larger than target
        else:
            row += 1  # Move down if current number is smaller than target

    return False

# Example usage
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
target = 5
print(f"Is {target} in the matrix? {search_matrix(matrix, target)}")
