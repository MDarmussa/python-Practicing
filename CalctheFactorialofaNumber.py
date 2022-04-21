

N = int(input("Enter the number: "))

Factorial = 1

if N < 0:
    print("Factorial is not apply for negative values")

elif N == 0:
    print("Please enter a number more than a zero")
else:
    for M in range (1, N + 1):
        Factorial = Factorial * M
    print('The factorial for the number you entered is: ', Factorial)

        
