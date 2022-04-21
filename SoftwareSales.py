package1 = 10
package2 = 20
package3 = 50
package4 = 100

Number_of_packages = int(input("Please enter the amount of packages purchased: " ))

Total_amount = Number_of_packages * 99

dicount1 = Total_amount * .10
dicount2 = Total_amount * .20
dicount3 = Total_amount * .30
dicount4 = Total_amount * .40

AmountAfterDiscount1 = Total_amount - dicount1
AmountAfterDiscount2 = Total_amount - dicount2
AmountAfterDiscount3 = Total_amount - dicount3
AmountAfterDiscount4 = Total_amount - dicount4

if Number_of_packages >= package1 and Number_of_packages < package2:
    print("The amount of the discount is: $",format(dicount1, '.2f'), sep='' )
    print("The total amount purchase after the discount is: $", format(AmountAfterDiscount1, '.2f'), sep='')
elif Number_of_packages >= package2 and Number_of_packages < package3:
    print("The amount of the discount is: $",format(dicount2, '.2f'), sep='' )
    print("The total purchase after the discount is: $", format(AmountAfterDiscount2, '.2f'), sep='')
elif Number_of_packages >= package3 and Number_of_packages < package4:
    print("The amount of the discount is: $",format(dicount3, '.2f'), sep='' )
    print("The total amount purchase after the discount is: $", format(AmountAfterDiscount3, '.2f'), sep='')
elif Number_of_packages >= package4:
    print("The amount of the discount is: $",format(dicount4, '.2f'), sep='' )
    print("The total amount purchase after the discount is: $", format(AmountAfterDiscount4, '.2f'), sep='')
else:
    print("You have no discount for purchasing less than 10 packages")

