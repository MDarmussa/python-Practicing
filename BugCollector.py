total_budget = 0

for day in range(5):
    budget = int(input("Enter the budget that collected for today: "))
    total_budget += budget

print("Total budget that collected for five days is $ ", format(total_budget, '.2f'))
