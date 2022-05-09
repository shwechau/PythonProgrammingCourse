import InterestCalculator
import Mortgage
from printuser import *

print_user()

def userInputs():
    selections()
    while(True):
        try:
            command = int(input("Select one of the command number above "))
            if command == 1:
                InterestCalculator.interestCalculator()
                selections()
            elif command == 2:
                Mortgage.mortgage()
                selections()
            elif command == 99:
                print("Have a nice day...")
                exit()
            else:
                print("Error:Command not recognised")
        except Exception as err:
            print("Error:Command not recognised")

def selections():
    msg1 = "Calculate simple interest"
    msg2 = "Calculate Mortgage Payment"
    msg3 = "Quit the program"
    length = len(msg2) + 10
    print("-" * length)
    print("{:8}".format("1"), msg1)
    print("{:8}".format("2"), msg2)
    print("{:8}".format("99"), msg3)
    print("-" * length)

userInputs()
