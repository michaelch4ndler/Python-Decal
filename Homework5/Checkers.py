#2 Checkers
import numpy as np

def checkerboard():
   
    pattern = np.array([0, 1] * 4)
    
    board = np.tile(pattern, (8, 1))
    return board

result = checkerboard()
print(result)