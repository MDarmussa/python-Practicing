
Age1 = 1
Age2 = 13
Age3 = 20
Age4 = 20

The_person_Age = int(input("Please enter the person age: "))

if The_person_Age <= Age1:
    print("The person is infant.")

elif The_person_Age < Age2:
    print("The person is child.")

elif The_person_Age < Age3:
    print("The person is teenager.")

else: 
    print("The person is adult.")
