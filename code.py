# My attempt to make a Ohm's Law Calculator
# Author: Justin Ludwick
# Date: 11-10-2021

# Function for multiplication
def multi(x, y):
    return x * y

# Function for division
def div(x, y):
    return x / y


print("What do you need: ")
print("1. Volts")
print("2. Amps")
print("3. Resistance")

while True:
    # takes input
    choice = input("Enter choice(1/2/3): ")

    # check if choice is one of three options
    if choice in ('1', '2', '3'):

        if choice =='1':
            num1 = float(input("Enter amps: "))
            num2 = float(input("Enter ohms: "))
            print(num1, "*", num2, "=", multi(num1, num2))

        elif choice =='2':
            num1 = float(input("Enter volts: "))
            num2 = float(input("Enter ohms: "))
            print (num1, "/", num2, "=", div(num1, num2))

        elif choice =='3':
            num1 = float(input("Enter volts: "))
            num2 = float(input("Enter amps: "))
            print(num1, "/", num2, "=", div(num1, num2))

        # check if user wants another calc
        # break while loop if answer is no

        nextCalc = input("Another calculation? ([YES]/no): ")
        if nextCalc == "no":
            break

    else:
        print("Invalid Input")

    break




