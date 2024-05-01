import numpy as np

# Take input for the two vectors
vector1 = input("Enter the first vector (space-separated values): ").split()
vector2 = input("Enter the second vector (space-separated values): ").split()

# Convert the input strings to float
vector1 = [float(x) for x in vector1]
vector2 = [float(x) for x in vector2]

# Convert the lists to NumPy arrays
vector1 = np.array(vector1)
vector2 = np.array(vector2)

# Calculate the dot product
dot_product = np.dot(vector1, vector2)

# Print the result
print(f"The dot product of the two vectors is {dot_product}")
