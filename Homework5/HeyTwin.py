#1 Hey Twin
import numpy as np

def findEqual(arr):
    equal_rows = arr[np.all(arr[:, 1:] == arr[:, :-1], axis=1)]
    return equal_rows

arr = np.array([[1, 1, 1], [1, 2, 3], [2, 2, 2]])
result = findEqual(arr)
print(result)