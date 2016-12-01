##-----------------------------------------------------------
##Programmed by: Tim Weatherford
##Assignment 7 - Calculates a payroll report
##Created 11/30/16 - v1.0
##-----------------------------------------------------------

##Declare Variables - especially since we are using global here.##
#Use of globals is for simplicity. Sorry!

grossPay = 0.00
overtimeHours = 0
overtimePay = 0
regularPay = 0
empName = ""
hoursWorked = 0
payRate = 0

#Helper Functions
def loopCheck():
    #Repeat?
    print("Would you like to calculate pay for another employee?")
    answer = str(input("'yes' or 'no' to quit:"))
    print("-"*60)
    if answer == 'yes':
        calculatePay()
    else:
        return
        

def notNull(params):
    if params:
        return params
    else:
        input("Error: Input must not be blank. Press any key to continue...")
        calculatePay()


#Main Loop
def calculatePay():
    global grossPay, overtimeHours,overtimePay,regularPay, empName, hoursWorked, payRate
        
    #For Presentation
    print("Payroll System")
    print("=-"*30)


    ##Input Section##
    empName = notNull(str(input("Enter the Employee's Full Name:")))
    hoursWorked = notNull(float(input("Enter Hours Worked:")))
    payRate = notNull(float(input("Enter " + empName + "'s hourly rate of pay:$")))
    print("-"*60)

    ##Logic Functions##
    if hoursWorked > 40:
        overtimeHours = hoursWorked - 40
        regularPay = 40 * payRate
        overtimePay = (payRate*1.5) * overtimeHours
        grossPay = regularPay + overtimePay
    else:
        regularPay = hoursWorked * payRate
        grossPay = regularPay
    outputReport()


def outputReport():
    global grossPay, overtimeHours,overtimePay,regularPay, empName, hoursWorked, payRate
    #Output
    print("=-"*30)
    print("Payroll Report for " + empName)
    print("=-"*30)
    print("--Hours Worked--")
    print("Total Hours Worked:" + str(hoursWorked))
    print("Overtime Hours:" + str(overtimeHours))
    print("--Pay Information--")
    print("Regular Pay:$" + str(format(regularPay, "9,.2f")))
    print("Overtime Pay:$" + str(format(overtimePay, "9,.2f")))
    print("Total Gross Pay:$" + str(format(grossPay, "9,.2f")))
    print("=-"*30)
    print("End Payroll Report")
    #Spacer
    print("-"*60)
    #Go again?
    loopCheck()


calculatePay()



