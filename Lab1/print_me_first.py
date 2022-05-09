from datetime import datetime
#This program is to print name, lab name and current time and the message Hello World
name = "CNET-142 - Shweta Chauhan"
#Printing Name based on the variable defined as name
print("{:14}".format("Name"), ":",  name)
lab = "Lab 1 - Hello World"
#Printing Lab name based on the variable defined as lab
print("{:14}".format("Lab"), ":", lab)
#Taking current date and time
currentTime = datetime.now()
timestamp_str = currentTime.strftime("%b-%d-%Y %a (%I:%M:%S%p)")
#Printing current date and time based on the variables defined as timestamp_str
print("{:14}".format("Current Time"), ":", timestamp_str)
