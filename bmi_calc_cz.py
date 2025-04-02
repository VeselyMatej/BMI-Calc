height_cm = float(input("Zadejte svou výšku v cm:\n"))
weight = float(input("Zadejte svou váhu v kg:\n"))
height = height_cm / 100

bmi = round (weight / (height)**2, 1)

if bmi < 18.5:
    print(f"Vaše BMI je {bmi}. Máte podváhu.")
elif bmi < 24.9:
    print(f"Vaše BMI je {bmi}. Je normální.")
elif bmi < 29.9:
    print(f"Vaše BMI je {bmi}. Máte nadváhu.")
elif bmi < 34.9:
    print(f"Vaše BMI je {bmi}. Máte obezitu.")
else:
    print(f"Vaše BMI je {bmi}. Máte extrémní obezitu.")