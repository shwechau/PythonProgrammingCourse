from datetime import datetime

def print_user():
#This program is to print name, lab name and current time and the message Hello World
    name = "CNET-142 - Shweta Chauhan, Lab 4 - Menu Function"
#Printing Name based on the variable defined as name
    print(name)
#Taking current date and time
    currentTime = datetime.now()
    #print(currentTime)
    timestamp_str = currentTime.strftime("%Y-%m-%d %H:%M:%S.%f")
#Printing current date and time based on the variables defined as timestamp_str
    print(timestamp_str)

