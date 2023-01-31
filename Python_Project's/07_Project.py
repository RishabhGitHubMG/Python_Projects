# BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight_int = int(weight)
height_int = float(height)

BMI = weight_int / height_int ** 2

BMI_int = int(BMI) 

print(BMI_int)
