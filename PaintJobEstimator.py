def main():
    sqFeetPainWall = float(input("Please enter the square feet of wall space: "))
    paintPrice = float(input("please enter the price of the paint: "))
    totalPaintGan = calPaintAmount(sqFeetPainWall)
    totalHours = calhours(sqFeetPainWall)
    totalLaborCharge = calLabor(totalHours)
    totalPaintCharge = calPaintCost(totalPaintGan, paintPrice)
    totalCost = calTotalCost(totalLaborCharge, totalPaintCharge)

    print("The number of gallons of paint required: ", format(totalPaintGan, ".2f"))
    print("The hours of labor required : ", format(totalHours, ".2f"))
    print("The cost of the paint: ", format(totalPaintCharge, ".2f"))
    print("The labor charges: ", format(totalLaborCharge, ".2f"))
    print("The total cost of the paint job: ", format(totalCost, ".2f"))
    


def calPaintAmount(sqFeetWall):
    totalGanNeeded = int(sqFeetWall / 112)
    return totalGanNeeded
    

def calhours(LaborFeetWall):
    totalLabNeeded = (LaborFeetWall / 112) * 8
    return totalLabNeeded

def calLabor(hours):
    totalLaborNeeded = hours * 35
    return totalLaborNeeded

def calPaintCost(paintGal, paintPrice):
    totalPaintCostNeeded = paintGal * paintPrice
    return totalPaintCostNeeded

def calTotalCost(laborCharge, paintCharge):
    totalCostNeeded = laborCharge + paintCharge
    return totalCostNeeded


main()
