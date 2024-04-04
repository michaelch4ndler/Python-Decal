#3 I need some space
import numpy as np

def spaceBetween(arr):
  
    spaced_arr = np.char.join(' ', arr)
    return spaced_arr

myarr = np.array(['python', 'is', 'cool!'])
result = spaceBetween(myarr)
print(result)
