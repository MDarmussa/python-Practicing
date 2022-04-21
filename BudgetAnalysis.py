budget = float(input("How much do you budget for this month "))
total_spending = 0
spending = 1
while spending !=0:
    spending = int(input("how much you spent in this month"))
    total_spending = total_spending + spending # or: total_spending += spending

if total_spending >= budget:
    print("over budget")

else:
    print("under budget")
    
