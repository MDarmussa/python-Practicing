rectangle_length1 = float(input("Please enter the first rectangle’s length: "))
rectangle_width1 = float(input("Please enter the first rectangle’s width: "))
Areas_of_Rectangles1 = rectangle_length1 * rectangle_width1

rectangle_length2 = float(input("Please enter the second rectangle’s  length: "))
rectangle_width2 = float(input("Please enter the second rectangle’s  width: "))
Areas_of_Rectangles2 = rectangle_length2 * rectangle_width2


if Areas_of_Rectangles1 > Areas_of_Rectangles2:
    print("The Rectangles1 is greater than Rectangles2.")

elif Areas_of_Rectangles2 > Areas_of_Rectangles1:
    print("The Rectangles2 is greater than Rectangles1.")

else:
    print("Both Rectangles are equal.")



