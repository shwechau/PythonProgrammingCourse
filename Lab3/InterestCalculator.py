from print_me_first import *

print_me_time()

p = 1

while (p > 0):
    try:
        p = int(input("Enter the starting principle, 0 to quit: "))
        if p == 0:
            print("Program exiting ...")
            exit()
        r = float(input("Enter the annual interest rate: "))
        n = int(input("How many times per year is the interest compounded? "))
        t = float(input("For how many years will the account earn interest? "))
        total = p * (1 + (r / (100 * n))) ** (n * t)
        interest = total - p
        print("At the end of {:.1f} years you will have $ {:,.2f} with interest earned $ {:,.2f} \n".format(t, total, interest))
    except Exception:
        print("Please enter a valid integer or float value only")


