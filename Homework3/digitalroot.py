#Problem 8 Digital Root 
def digital_root(x):
    while x >= 10:
        # Sum the digits of the number
        x = sum(int(digit) for digit in str(x))
    
    return x

# Example usage:
input_number = 12345
result = digital_root(input_number)
print(result)