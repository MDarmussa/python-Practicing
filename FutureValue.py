def main():
    
    present_Value = float(input("Enter the present value: "))
    interest_Rate = float(input("Enter the monthly interest rate: "))
    number_of_months = float(input("Enter how many month: "))

    amount_future_value(present_Value, interest_Rate, number_of_months)

def amount_future_value(p, i, t):
    f = p * (1+i)**t
    print("The smount future value is for your acount is $", format(f, '.2f'), sep="")


main()
