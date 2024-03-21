#2D Lists
# 3.1 Part 1 
#Using nested for loops to create and print a 5x5 2D list with numbers 1 to 25
matrix = []
num = 1
for i in range(5):
    row = []
    for j in range(5):
        row.append(num)
        num += 1
    matrix.append(row)

for row in matrix:
    print(row)

# 3.2 Part 2
# Replace multiples of 3 with '?' character in the 2D list
for i in range(5):
    for j in range(5):
        if matrix[i][j] % 3 == 0:
            matrix[i][j] = '?'
            
for row in matrix:
    print(row)