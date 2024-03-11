#Problem 3: Checking Leap Year
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
year_check1 = 2024
result1 = leap_year(year_check1)
year_check2 = 2023
result2 = leap_year(year_check2)
print(result1)
print(result2)


