WeightOfPackage1 = 2
WeightOfPackage2 = 6
WeightOfPackage3 = 10

WeightOfPackagesRate = int(input("Enter the weight of packages need to be shipped: "))

shipping_charges1 = WeightOfPackagesRate * 1.50
shipping_charges2 = WeightOfPackagesRate * 3
shipping_charges3 = WeightOfPackagesRate * 4
shipping_charges4 = WeightOfPackagesRate * 4.75

if WeightOfPackagesRate <= WeightOfPackage1:
    print ("The shipping charges is: $", format(shipping_charges1, '.2f'), sep='')
    
elif WeightOfPackagesRate > WeightOfPackage1 and WeightOfPackagesRate <= WeightOfPackage2:
    print ("The shipping charges is: $", format(shipping_charges2, '.2f'), sep="")
elif WeightOfPackagesRate > WeightOfPackage2 and WeightOfPackagesRate <= WeightOfPackage3:
    print ("The shipping charges is: $", format(shipping_charges3, '.2f'), sep="")
    
else: 
    print ("The shipping charges is: $", format(shipping_charges4, '.2f'), sep="")

