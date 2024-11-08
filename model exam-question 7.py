def matrix_multiply(A, B):
    # Get dimensions of A and B
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Ensure matrix multiplication is possible (columns of A must equal rows of B)
    if cols_A != rows_B:
        raise ValueError("Matrices cannot be multiplied: incompatible dimensions.")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example usage
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Call the function
result = matrix_multiply(A, B)

# Print the result
print("Result of matrix multiplication:")
for row in result:
    print(row)
