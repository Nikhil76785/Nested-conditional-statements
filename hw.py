print("Welcome to the test site!")

age = int(input("Please enter your age: "))

if (age > 10 and age < 20):
    print("You are eligible for the test. Please proceed to xyz10.com")

elif (age < 10 or age > 20):
    print("You are not eligible for the test.")