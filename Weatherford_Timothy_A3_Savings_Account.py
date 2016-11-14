##-----------------------------------------------------------
##Programmed by: Tim Weatherford
##Assignment 3 - Manages the balance of a savings account
##Created 10/29/16 - v1.0
##-----------------------------------------------------------

import time

title = "WELCOME TO THE FAKEBANK,INC ATM"

##Presentation Functions##
#Displays text formatted as a header
def printHeader(text):
    print("=-"*30)
    print(text)
    print("=-"*30)

#Makes a spacer
def printSpacer():
    print("-"*60)

def printError(text):
    printSpacer()
    print("Error - " + text)
    input("Press enter to continue...")

##Startup Functions##
#Gets the initial balance of the ATM
def getInitialBalance():
    balance = float(input("Please enter the users initial balance:$"))
    print("Is $" + str(format(balance, "9,.2f")) + " correct for the initial balance?")
    decision = str(input("Please enter 'yes' or 'no':"))
    if decision == "yes":
        bootOS()
    else:
        balance = getInitialBalance()
    return balance

#Changes to the customer facing side of the ATM
def bootOS():
        printSpacer()
        print("Thank you, the ATM is now initialized.")
        print("Booting to CustomerOS in ")
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)

#Displays splash screen and gets the initial balance
def initializeATM():
    printHeader("Admin Startup Screen")
    balance = getInitialBalance()
    return balance

#Gets the customers name
def getCustomer():
    name = str(input("Please enter your name to continue:"))
    return name

##Main Functions##
#Prints the main menu functions
def mainMenu(balance,name):
    printHeader("MAIN MENU - Welcome " + name + "!")
    print("Please select from the following choices:")
    print("1 - Check My Balance")
    print("2 - Withdraw Money")
    print("3 - Deposit Money")
    print("4 - Logout")
    selection = int(input("Please select 1, 2, 3, or 4:"))
    takeAction(selection,balance,name)

#Handles withdrawing money
def withdrawMoney(amount,balance,name):
    printHeader("WITHDRAW MONEY - " + name)
    if balance >= amount:
        balance -= amount
        print("You sucessfully withdrew $" + str(format(amount, "9,.2f")) +". Please take your money below.")
        print("Your new balance is $" + str(format(balance, "9,.2f")) + ".")
        input("Press enter to continue...")
        mainMenu(balance,name)
    elif balance < amount:
        printError("Your balance is not sufficient.")
        mainMenu(balance,name)
    else:
        PrintError("Invalid Selection")
        mainMenu(balance,name)
    return balance
        

#Handles Deposit of Money
def depositMoney(amount,balance,name):
    printHeader("DEPOSIT MONEY -" + name)
    balance += amount
    print("You sucessfully deposited $" + str(format(amount, "9,.2f")) +" into your account.")
    print("Your new balance is:$" + str(format(balance, "9,.2f")) + ".")
    input("Press enter to continue...")
    mainMenu(balance,name)
    return balance

#Displays User's Balance
def checkBalance(balance,name):
    printHeader("DISPLAY BALANCE - " + name)
    print("Your balance is:$" + str(format(balance, "9,.2f")))
    input("Press enter to continue...")
    mainMenu(balance,name)

#Login/Logout Function
def getUser(balance):
    printHeader(title)
    name = getCustomer()
    mainMenu(balance,name)
    return name

#Processes Main Menu Input
def takeAction(selection,balance,name):
    if selection == 1:
        checkBalance(balance,name)
    elif selection == 2:
        if balance > 0:
            printSpacer()
            print("Your current balance is:$ " + str(format(balance, "9,.2f")))
            amount = round(float(input("How much would you like to withdraw?:$")), 2)
            balance = round(withdrawMoney(amount,balance,name), 2)
        else:
            printError("You do not have any money available for withdraw")
            mainMenu(balance,name)
    elif selection == 3:
        printSpacer()
        print("Your current balance is:$ " + str(format(balance, "9,.2f")))
        amount = round(float(input("How much would you like to deposit?:$")), 2)
        if amount > 0:
            balance = round(depositMoney(amount,balance,name),2)
            return balance
        else:
            printError("The amount must be greater than $0")
            mainMenu(balance,name)
    else:
        #Get us a new user if logout or invalid choice is selected.
        getUser(balance)

##Main Program Loop##

#Startsup ATM and gets an initial balance
balance = round(initializeATM(), 2)
#Gets our first customer
name = getUser(balance)
#Prints main menu for the customer
mainMenu(balance,name)

    
    
