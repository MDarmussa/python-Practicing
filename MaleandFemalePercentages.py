NumberOfMales = float(input("Please enter the number of males: "))
NumbeOfFemales = float(input("Please enter the number of female: "))
total_class = NumberOfMales + NumbeOfFemales
Male_percentage = NumberOfMales/total_class
Female_percentage = NumbeOfFemales/total_class


print("the percentage of males in the class is: ", format(Male_percentage , '.0%'))
print("the percentage of females in the class is: ", format(Female_percentage ,'.0%'))
