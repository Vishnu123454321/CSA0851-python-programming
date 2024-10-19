def matrix_addition(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])

    # Initialize a result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    # Perform matrix addition
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] + mat2[i][j]

    return result


def main():
    try:
        # Input matrices
        Mat1 = [[int(x) for x in input("Enter elements of Mat1 row separated by space: ").split()] for _ in range(2)]
        Mat2 = [[int(x) for x in input("Enter elements of Mat2 row separated by space: ").split()] for _ in range(2)]

        # Check if matrices have the same dimensions
        if len(Mat1) != len(Mat2) or len(Mat1[0]) != len(Mat2[0]):
            print("Matrices must have the same dimensions for addition.")
            return

        # Perform matrix addition
        MatSum = matrix_addition(Mat1, Mat2)

        # Print the result
        print("Mat Sum =")
        for row in MatSum:
            print(" ".join(map(str, row)))

    except ValueError:
        print("Error: Please enter valid integer values for matrix elements.")


# Run the main function
main()
