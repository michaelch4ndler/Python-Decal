#Problem 1 
def exp(x,y):
    if y==0:
        return 1
    return x*exp(x, y-1)

print(exp(3,3))