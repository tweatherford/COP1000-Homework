##-----------------------------------------------------------
##Programmed by: Tim Weatherford
##Assignment 2 - Displays the subtotal, tax, and total of x number of items.
##Created 10/29/16 - v1.0
##-----------------------------------------------------------

##Presentation Methods

#Prints the introduction - just for presentation.
def displayIntro():
    print("Purchasing System")
    print("=-"*30)

#Empty Lines - for presentation. Seperates user input from the output report.
def makeSpacer():
    print("")
    print("-"*60)
    print("")
    
##Begin Helper Methods##

#This method gets the desired quantity of tests to score from the user.
def getQty():
    qty = int(input("Enter the quantity items being purchased:"))
    return qty

#This method gets the price of each item.
def getItems():
    count = 0
    items = []
    while count != qty:
       count = count + 1
       item = float(input('Enter the price for item#{0}:$'.format(count)))
       items.insert(count - 1, item)
    return items

#This method adds the subtotal cost of items.
def getSubtotal(items):
    subtotal = 0
    for cost in items:
        subtotal = subtotal + cost
    return subtotal

#This method calculates the tax.
def calculateTax(subtotal):
    subtotal = sum(subtotal)
    tax = subtotal * 0.07
    return tax

#This method calculates the total (subtotal plus tax).
def getTotal(subtotal,tax):
    total = subtotal + tax
    return total


#This method accepts our data as input and prepares the final output.
def displayReport(items,subtotal,tax,total):
    count = 0
    print("Purchase Receipt")
    print("=-"*30)
    for item in items:
        count = count + 1 
        print("Price of Item#"+ str(count) + ":$" + str(round(item,2)))
    print("Qty of Items:" + str(count))
    print("Subtotal:$" + str(round(subtotal,2)))
    print("Tax:$" + str(round(tax,2)))
    print("Total:$" + str(round(total,2)))
    print("=-"*30)
    print("End Receipt")

##End Helper Methods##

##Program Main Loop##

#Presentation
displayIntro()
#Input - Get Items and qty
qty = getQty()
items = getItems()

#Processing/Calculation - subtotal, tax, total
subtotal = getSubtotal(items)
tax = calculateTax(items)
total = getTotal(subtotal,tax)

#Output - Presents data to the user.
makeSpacer()
displayReport(items,subtotal,tax,total)

