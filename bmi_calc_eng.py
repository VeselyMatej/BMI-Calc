height_cm = float(input("Enter your height in cm:\n"))
weight = float(input("Enter your weight in kg:\n"))
height = height_cm / 100

bmi = round(weight / (height) ** 2, 1)

if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
elif bmi < 24.9:
    print(f"Your BMI is {bmi}. It is normal.")
elif bmi < 29.9:
    print(f"Your BMI is {bmi}. You are overweight.")
elif bmi < 34.9:
    print(f"Your BMI is {bmi}. You have obesity.")
else:
    print(f"Your BMI is {bmi}. You have extreme obesity.")
