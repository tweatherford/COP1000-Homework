'''
Assignment#8: Rainfall Array
Programmer: Timothy Weatherford
Course: COP1000 - Intro to Computer Programming
'''
#Initial Variables
rainArray = []
count = 0
#For while loop
quitProgram = False

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

#Searches the array for a a rain data point of the users choice
def searchArray():
    count = 0
    targetCount = 0 
    makeHeader("Rain Data Search")
    searchString = input("Please enter a rain to search for:")
    global rainArray
    
    for rain in rainArray:
        if float(rain) == float(searchString):
            targetCount += 1

    print("Your target rain of " + str(searchString) + " occured " + str(targetCount) + " times.")
    
#Iterates array and displays each   
def displayArray():
    count = 0
    global rainArray
    makeHeader("Display all rain data points")
    for rain in rainArray:
        count += 1 
        print("Rain data point#" + str(count) + " is:" + str(rainArray[count-1]))

#Main Menu 
def mainMenu():
    global quitProgram
    while quitProgram == False:
        makeHeader("Main Menu")
        choice = int(input("Please choose 1 to display all rain entries, 2 to search rain data points's or, press 3 to quit:"))
        if choice == 1:
            displayArray()
            mainMenu()
        elif choice == 2:
            searchArray()
            mainMenu()
        elif choice == 3:
            quitProgram = True
            mainMenu()

#RAIN ARRAY INTIALIZATION - This handles startup more or less. 
makeHeader("Program Startup - Rain Entry")

targetCount = input("How many rain data points's would you like to enter?(default 10):")
if targetCount == "":
    targetCount = 10

while count < int(targetCount):
    count +=1
    rain = input("Please enter rain data point#" + str(count)+":")
    appendData(rain)

mainMenu()
        
    
