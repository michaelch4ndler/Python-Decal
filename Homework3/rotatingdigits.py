#5 Rotating Digits
def rotate_digits(n):
    if n < 0:
        raise ValueError("Input has to be non-negative integer.")
    
    last_digit = n % 10

    n //= 10 
    rotated_number = last_digit * (10 ** (len(str(n)))) + n

    return rotated_number

# Example
input_number = 12345
result = rotate_digits(input_number)
print(result)