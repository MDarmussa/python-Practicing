def main():
    fat_grams = int(input("Enter the number of fat grams that you consumed in a day: "))
    carb_grams = int(input("Enter the number of carbohydrate grams that you consumed in a day: "))

    fat_gram = fatGrams(fat_grams)
    carb_gram = fatGrams(carb_grams)

def fatGrams(FatGram):
    calories_from_fat = FatGram *  9
    print("The number of calories that result from the fat is: ", format(calories_from_fat, ".2f"))
    return calories_from_fat

def fatGrams(CarbGram):
    calories_from_carbs = CarbGram * 4
    print("The number of calories that result from the carbohydrates is: ", format(calories_from_carbs, ".2f"))
    return calories_from_carbs

main()
