def main():
    
    amount_purchase = int(input("Please enter the amount of purchase: "))

    staxtotal = s_tax(amount_purchase) 
    ctaxtotal = C_tax(amount_purchase, )
    tsalestax = T_sales_tax(staxtotal, ctaxtotal)
    totalsales = Total_sales(amount_purchase, tsalestax)
    
def s_tax(sTax):
    state_tax = sTax * 0.05
    print("The state sales tax is: $", format(state_tax, ".2f"))
    return state_tax

def C_tax(cTax):
    country_tax = cTax * 0.025
    print("The country sales tax is: ", format(country_tax, ".2f"))
    return country_tax

def T_sales_tax(tSalesTax, county_tax):
    total_sales_tax = tSalesTax + county_tax
    print ("The total sales tax is: ", format(total_sales_tax, ".2f"))
    return total_sales_tax

def Total_sales(amount_purchase, tSalesTax):
    total_of_sales = amount_purchase + tSalesTax
    print("The total of the sale is: ", format(total_of_sales, ".2f"))
    return total_of_sales

                    
main()

# s_tax   function
# state_tax    variable

# we can't return function, return must be to variables only. 


