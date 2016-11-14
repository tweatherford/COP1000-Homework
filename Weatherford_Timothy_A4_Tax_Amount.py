##-----------------------------------------------------------
##Programmed by: Tim Weatherford
##Assignment 4 - Calculates Tax
##Created 11/11/16 - v1.0
##-----------------------------------------------------------

#Input
income = float(input("Please enter your taxable income:$"))


#Logic
if income <= 20000:
    tax = .02 * income
elif income <= 50000:
    tax = 400 + .025 * (income - 20000)
else:
    tax = 1150 + .035 * (income - 50000)

#Output
print("=-"*30)
print("Your tax due is $" + str(format(tax, ".2f")) + " based on a taxable income of $" + str(format(income, ".2f")))
print("=-"*30)
