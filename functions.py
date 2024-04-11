def find_min_max(numbers):
    if not numbers:
        return None

    minimum = maximum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    return minimum, maximum

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value, max_value = find_min_max(numbers)
print(f"The minimum value is: {min_value}")
print(f"The maximum value is: {max_value}")