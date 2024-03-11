#Problem 2 Maximum and Minimum 

list=[11,52,54,4,12]

def maxmin():
    eval(input(list)) 

max=list[0]
min=list[0]

for num in list:
    if num>max:
        max=num
    if num<min:
        min=num

print(max)
print(min)
tuple=(min,max)
print(tuple)