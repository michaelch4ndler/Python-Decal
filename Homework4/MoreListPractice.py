#4 More List Practice 
def removeDuplicates(lst):
    return list(set(lst))

# Test the function
lis = [1, 1, 2, 3, 4, 4]
result = removeDuplicates(lis)
print(result)