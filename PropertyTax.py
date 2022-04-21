def main():
    Actual_value = float(input("Please enter the actual value of the property: "))
    Assessment_Value = Actual_value * .60
    print("The assessment value  of a piece of property you entered is $", Assessment_Value, sep='')
    Property_tax = (Assessment_Value / 100) * .72
    print("The property tax is $", format(Property_tax, '.2f'), sep='')

main()
