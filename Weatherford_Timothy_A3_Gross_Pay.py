##-----------------------------------------------------------
##Programmed by: Tim Weatherford
##Assignment 3 - Calculates a payroll report
##Created 11/10/16 - v1.0
##-----------------------------------------------------------

##Declare Variables##
grossPay = 0.00
overtimeHours = 0
overtimePay = 0
regularPay = 0

#For Presentation
print("Payroll System")
print("=-"*30)


##Input Section##
empName = str(input("Enter the Employee's Full Name:"))
hoursWorked = float(input("Enter Hours Worked:"))
payRate = float(input("Enter " + empName + "'s hourly rate of pay:$"))
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

    
