import numpy as np

# Take input for the dimensions of the matrix
n = int(input("Enter the order of the square matrix: "))

# Take input for the matrix
print("Enter the elements of the matrix:")
matrix = []
for i in range(n):
    row = input(f"Row {i+1} (space-separated values): ").split()
    row = [float(x) for x in row]
    matrix.append(row)

# Convert the list to a NumPy array
matrix = np.array(matrix)

# Calculate the determinant
determinant = np.linalg.det(matrix)

# Print the result
print(f"The determinant of the matrix is: {determinant}")
