

The_Packet_number = int(input("Please enter the number to display the color: "))

if The_Packet_number >= 1 and The_Packet_number <= 10:
     if The_Packet_number % 2 == 0:
         print ("black")
     else:
         print("red")

        
        

elif The_Packet_number >= 11 and The_Packet_number <= 18:
     if The_Packet_number % 2 == 0:
         print ("red")
                
     else:
         print("black")

elif The_Packet_number >= 19 and The_Packet_number <= 28:
     if The_Packet_number % 2 == 0:
         print ("black")
     else:
         print("red")

elif The_Packet_number >= 29 and The_Packet_number <= 36:
     if The_Packet_number % 2 == 0:
         print ("red")
     else:
         print("black")

elif The_Packet_number == 0:
    print("green")




else:
    print("The number is outside the range of 0 through 36, please try another number.")
    

