def main():
    print("Please enter the following monthly expenses for your automobile")
    
    Loan_Payement = float(input("Enter the loan expenses: "))
    insurance_Payement = float(input("Enter the insurance expenses: "))
    gas_Payement = float(input("Enter the gas expenses: "))
    oil_Payement = float(input("Enter the oil expenses: "))
    tires_Payement = float(input("Enter the tires expenses: "))
    maintenance_Payement = float(input("Enter the tires expenses: "))
    
    total_monthly_cost(Loan_Payement, insurance_Payement, gas_Payement, oil_Payement, tires_Payement, maintenance_Payement)


def total_monthly_cost(Loan_Payement, insurance_Payement, gas_Payement, oil_Payement, tires_Payement, maintenance_Payement):
    calmonthlycost = Loan_Payement + insurance_Payement + gas_Payement + oil_Payement + tires_Payement + maintenance_Payement
    print("The mothly expenses is: $", format(calmonthlycost, ".2f"))
    total_annual_cost(calmonthlycost)

def total_annual_cost(monthly):
    calannualcost = monthly * 12
    print("The annually expenses is: $", format(calannualcost, ".2f"))

main()
    

