print("Welcome To Uber!")

print("Select your ride:")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice (1 or 2): "))

if (choice == 1):
    print("Type of bike: ")
    print("1. Scooter")
    print("2. Motorcycle")

    bike_choice = int(input("Enter your choice (1 or 2): "))

    if (bike_choice == 1): 
        print("You have selected a scooter.")

    else:
        print("You have selected a motorcycle.")
        
elif (choice == 2):
    print("Type of car: ")
    print("1. 5 seater")
    print("2. 7 seater")

    car_choice = int(input("Enter your choice (1 or 2): "))

    if (car_choice == 1): 
        print("You have selected a 5 seater.")

    else:
        print("You have selected a 7 seater.")

else:
    print("Invalid input. Please enter 1 or 2.")