iteam1= int(input("Please enter the price for iteam 1: "))
iteam2= int(input("Please enter the price for iteam 2: "))
iteam3= int(input("Please enter the price for iteam 3: "))
iteam4= int(input("Please enter the price for iteam 4: "))
iteam5= int(input("Please enter the price for iteam 5: "))

subtotalOfSales = (iteam1 + iteam2 + iteam3 + iteam4 + iteam5)
print("The subtotal for the sales before tax is: $", format(subtotalOfSales, '.2f'), sep='')

sales_tax = subtotalOfSales * .07
print("The amount of sales tax is: $", format(sales_tax, '.2f'), sep='')

total_after_tax = subtotalOfSales + sales_tax
print("The subtotal for the sales after tax is: ", "$", format(total_after_tax, '.2f'), sep='')

                    
