#Problem 4: Calculating BMI
def calculate_bmi(weight,height):
    if height == 0:
        raise ValueError("Height needs to be greater than 0.")
    
    bmi = weight / (height ** 2)
    return bmi

weight = 150 #Pounds
height = 65 #Inches

result = calculate_bmi(weight, height)
print(result)