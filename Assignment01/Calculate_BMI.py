weight = float(input("enter your weight according to Kilograms: "))
height = float(input("enter your height according to Metres: "))

BMI = weight / (height ** 2)

if BMI < 18.5:
    print("UNDERWEIGHT")

if 18.5 <= BMI <= 24.9:
    print("NORMAL")

if 25 <= BMI <= 29.9:
    print("OVERWEIGHT")

if 30 <= BMI <= 34.9:
    print("OBESE")

if 35 <= BMI :
    print("EXTREMELY OBESE")