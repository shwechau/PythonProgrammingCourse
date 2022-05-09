
def mortgage():
    principle = 1
    while (principle > 0):
        try:
            principle = int(input("Enter the loan amount, 0 to quit: "))
            if principle == 0:
                print("Exiting Mortgage Program ...")
                break
            roi = float(input("Enter the loan interest rate % : "))
            loanTerm = int(input("Enter the loan term (number of years): "))
            monthlyRate = (roi/100)/12
            numPayments = loanTerm*12
            monthlyPayment = principle*monthlyRate\
                             * pow((1+monthlyRate), numPayments)\
                             /(pow((1+monthlyRate),numPayments)-1)
            totalPayment = monthlyPayment*numPayments
            interestPaid = totalPayment-principle
            print("For the loan amount of ${:,.2f} for {:1d} years with interest rate {:,.2f} % \
            \n The monthly payment is ${:,.2f}  \n Total amount paid for this loan is ${:,.2f} \
            \n Total Interest paid for this loan is ${:,.2f} ".format(principle, loanTerm, roi, monthlyPayment, totalPayment, interestPaid))
        except Exception as err:
            print("Error due to - ", err)
