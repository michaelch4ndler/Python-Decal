#Problem 6: Minimum and Maximum but with Loops

#Minimums
def find_min_for_loop(iterable):
    min_value = iterable[0]
    for item in iterable[1:]:
        if item < min_value:
            min_value = item
    return min_value

def find_min_while_loop(iterable):
    min_value = iterable[0]
    index = 1
    while index < len(iterable):
        if iterable[index] < min_value:
            min_value = iterable[index]
        index += 1
    return min_value

#Maximums: 
def find_max_for_loop(iterable):
    max_value = iterable[0]
    for item in iterable[1:]:
        if item > max_value:
            max_value = item
    return max_value

def find_max_while_loop(iterable):
    max_value = iterable[0]
    index = 1
    while index < len(iterable):
        if iterable[index] > max_value:
            max_value = iterable[index]
        index += 1
    return max_value

#Data 
my_list = [3, 7, 2, 8, 5, 1]

#Functions
min_for_loop_result = find_min_for_loop(my_list)
min_while_loop_result = find_min_while_loop(my_list)
max_for_loop_result = find_max_for_loop(my_list)
max_while_loop_result = find_max_while_loop(my_list)

print(min_for_loop_result)
print(min_while_loop_result)
print(max_for_loop_result)
print(max_while_loop_result)
