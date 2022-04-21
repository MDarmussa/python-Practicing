import random
def main():



    userNumber = int(input("Enter your number: "))
    number = random.randint(1, 100)
    print('the number is: ', number)

    if userNumber > number:
        print ("Too high, try again")

    elif userNumber < number:
        print("Too low, try again")

    else:
        print("congratulation!")

  
main()
