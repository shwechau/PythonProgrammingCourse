from datetime import datetime
#This program is to calculate efficiency of a car based on inputs from the user
name = "CNET-142 - Shweta Chauhan"
#Printing Name based on the variable defined as name
print("{:14}".format("Name"), ":",  name)
lab = "Lab 2 - Car Mileage"
#Printing Lab name based on the variable defined as lab
print("{:14}".format("Lab"), ":", lab)
#Taking current date and time
currentTime = datetime.now()
print(currentTime)
timestamp_str = currentTime.strftime("%b-%d-%Y %a (%I:%M:%S%p)")
#Printing current date and time based on the variables defined as timestamp_str
print("{:14}".format("Current Time"), ":", timestamp_str)

capacity = float(input("Enter the capacity of the car's gas tank (in gallons): "))
miles_per_gallon = int(input("Enter car's miles per gallon: "))
price_per_gallon = float(input("Enter price per gallon: "))
print("Cost for driving 100 miles is : $ %.2f" %((100/miles_per_gallon)*price_per_gallon))
print("Distance on a tank of gas is: %.2f miles" %(capacity*miles_per_gallon))
if miles_per_gallon < 30:
    print("Your car MPG is %.1f . It is not fuel efficient car"  %miles_per_gallon )
elif 30 < miles_per_gallon < 40:
    print("Your car MPG is %.1f . It is average fuel efficient car." %miles_per_gallon )
elif 40 < miles_per_gallon < 50:
    print("Your car MPG is %.1f . It is fuel efficient car" %miles_per_gallon)
else:
    print("Your car MPG is %.1f . It is very fuel efficient car" %miles_per_gallon)







