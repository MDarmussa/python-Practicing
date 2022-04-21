underweight_BMI = 18.5
optimalweight_BMI = 25

weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print ("Your body mass index is ", format(BMI, '.2f'))

if BMI < underweight_BMI:
    print("Your BMI is underwight")
elif BMI >= underweight_BMI and BMI <= optimalweight_BMI:
    print("Your BMI is optimal")
else:
    print("Your BMI is overweight")
