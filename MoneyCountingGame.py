onePenny = .01
oneNickle = .05
Onedime = .10
oneQuarter = .25

numberOfBennies = int(input("Please enter the number of bennies: "))
numberOfNickels = int(input("Please enter the number of Nickels: "))
numberOfdimes = int(input("Please enter the number of dimes: "))
numberOfquarters = int(input("Please enter the number of quarters: "))

userPenniesValue = numberOfBennies * onePenny
userNicklesValue = numberOfNickels * oneNickle
userDimesValue = numberOfdimes * Onedime
userQuartersValue = numberOfquarters * oneQuarter

total_money_entered = userPenniesValue + userNicklesValue + userDimesValue + userQuartersValue


if total_money_entered == 1.00:
    print ("congratulate, you win the game! Because your total is equal to $" +\
           format(total_money_entered, ",.2f"))

else:
    if total_money_entered < 1.00:
        print("Sorry, you did not win the game, try again.", "Your total is: $" +\
              format(total_money_entered, ",.2f") + " and it is less than $1.")
    elif total_money_entered > 1.00:
        print("Sorry, you did not win the game, try again.", "Your total is: $" +\
              format(total_money_entered, ",.2f") + " and it is more than $1.")

        






