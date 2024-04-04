#4 Everything is in order
import numpy as np

def sorting(matrix):
    sorted_matrix = np.sort(matrix, axis=0)
    return sorted_matrix

np.random.seed(12345)
a = np.random.randint(1, 50, (4, 5))
print("Original matrix:")
print(a)

sorted_a = sorting(a)
print("\nSorted matrix along columns:")
print(sorted_a)