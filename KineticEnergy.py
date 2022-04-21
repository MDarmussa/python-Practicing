def main():
    
    mass = float(input("Enter the value for mass in kiloegram: "))
    velocity = float(input("Enter the velocity in meters per second : "))

    kinetic_energy(mass, velocity)
        
    

def kinetic_energy(m, v):
    KE = 1/2 * m*v*v
    print("The object's kinetic_energy is: ", format(KE, '.2f'))


main()
    
