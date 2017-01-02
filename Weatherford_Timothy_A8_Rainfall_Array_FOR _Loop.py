'''
Assignment#8: Rainfall Array
Programmer: Timothy Weatherford
Course: COP1000 - Intro to Computer Programming
'''
#Initial Variables
rainArray = []
count = 0

#Helper Methods

#Makes headers
def makeHeader(text):
    print("=-"*30)
    print(text)
    print("=-"*30)

#Appends data to array for us
def appendData(rain):
    global rainArray
    rainArray.append(float(rain))

#Searches the array for a a rainfall of the users choice
def searchArray():
    count = 0
    targetCount = 0 
    makeHeader("Rain data Search")
    searchString = input("Please enter a rain data point to search for:")
    global rainArray
    
    for rain in rainArray:
        if float(rain) == float(searchString):
            targetCount += 1

    print("Your target rainfall of " + str(searchString) + " occured " + str(targetCount) + " times.")
    
#Iterates array and displays each   
def displayArray():
    count = 0
    global rainArray
    makeHeader("Display all rain data points:")
    for rain in rainArray:
        count += 1 
        print("Rain Data#" + str(count) + " is:" + str(rainArray[count-1]))

#Main Menu 
def mainMenu():
    makeHeader("Main Menu")
    choice = int(input("Please choose 1 to display all rain entries, 2 to search rain's or, press 3 to quit:"))
    if choice == 1:
        displayArray()
        mainMenu()
    elif choice == 2:
        searchArray()
        mainMenu()
    elif choice == 3:
        pass
    else:
        print("Invalid Selection - Please choose again")
        mainMenu()


#RAIN ARRAY INTIALIZATION - This handles startup more or less. 
makeHeader("Program Startup - Rain Entry")

targetCount = input("How many rain data points would you like to enter?(default 10):")
if targetCount == "":
    targetCount = 10

while count < int(targetCount):
    count +=1
    rain = input("Please enter rain#" + str(count)+":")
    appendData(rain)

mainMenu()
        
    
