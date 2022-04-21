offer1 = 2
offer2 = 4
offer3 = 6
offer4 = 8

numberOfBooks = int(input("Please enter how many books have you purchased in this month: "))

if numberOfBooks >= offer1 and numberOfBooks < offer2:
    print("You have earned 5 points for this month")
elif numberOfBooks >= offer2 and numberOfBooks < offer3:
    print ("You have earned 15 points for this month")
elif numberOfBooks >= offer3 and numberOfBooks < offer4:
    print ("You have earned 30 points for this month")
elif numberOfBooks >= offer4:
    print("You have earned 60 points for this month")

else:
    print ("You have earned 0 points for this month")





