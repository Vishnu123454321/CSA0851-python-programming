def generate_spiral_matrix(n):
    # Initialize an n x n matrix with zeros
    spiral_matrix = [[0] * n for _ in range(n)]
    
    # Define the boundaries: top, bottom, left, right
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1  # Start from 1 and increment
    
    while top <= bottom and left <= right:
        # Fill the top row (left to right)
        for i in range(left, right + 1):
            spiral_matrix[top][i] = num
            num += 1
        top += 1  # Move down after filling the top row
        
        # Fill the right column (top to bottom)
        for i in range(top, bottom + 1):
            spiral_matrix[i][right] = num
            num += 1
        right -= 1  # Move left after filling the right column
        
        if top <= bottom:
            # Fill the bottom row (right to left)
            for i in range(right, left - 1, -1):
                spiral_matrix[bottom][i] = num
                num += 1
            bottom -= 1  # Move up after filling the bottom row
        
        if left <= right:
            # Fill the left column (bottom to top)
            for i in range(bottom, top - 1, -1):
                spiral_matrix[i][left] = num
                num += 1
            left += 1  # Move right after filling the left column
    
    return spiral_matrix

# Function to print the matrix
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# Example usage
n = 5  # Size of the matrix
spiral_matrix = generate_spiral_matrix(n)
print("Spiral Matrix:")
print_matrix(spiral_matrix)
