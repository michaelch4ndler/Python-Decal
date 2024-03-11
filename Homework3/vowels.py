#Problem 7
def vowel_count(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count

# Example usage:
input_str = "Holey Moley"
result = vowel_count(input_str)
print(result)