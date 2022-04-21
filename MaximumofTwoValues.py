def main():
    n_one = int(input("enter number 1: "))
    n_two = int(input("ente rnumber 2: "))
    returned_value = max_value(n_one, n_two)
    print(returned_value)

def max_value(number1, number2):
    if number1 > number2:
        return number1
    elif number1 < number2:
        return number2
    else:
        return "The numbers are the same"

main()
