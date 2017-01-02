'''
Assignment#8: Creating, displaying, and searching an array.
Programmer: Timothy Weatherford
Course: COP1000 - Intro to Computer Programming
'''
#Initial Variables
gpaArray = []
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
def appendData(gpa):
    global gpaArray
    gpaArray.append(float(gpa))

#Searches the array for a a GPA of the users choice
def searchArray():
    count = 0
    targetCount = 0 
    makeHeader("GPA Search")
    searchString = input("Please enter a GPA to search for:")
    global gpaArray
    
    for gpa in gpaArray:
        if float(gpa) == float(searchString):
            targetCount += 1

    print("Your target GPA of " + str(searchString) + " occured " + str(targetCount) + " times.")
    
#Iterates array and displays each   
def displayArray():
    count = 0
    global gpaArray
    makeHeader("Display all GPA's")
    for gpa in gpaArray:
        count += 1 
        print("Gpa#" + str(count) + " is:" + str(gpaArray[count-1]))

#Main Menu 
def mainMenu():
    global quitProgram
    while quitProgram == False:
        makeHeader("Main Menu")
        choice = int(input("Please choose 1 to display all GPA entries, 2 to search GPA's or, press 3 to quit:"))
        if choice == 1:
            displayArray()
            mainMenu()
        elif choice == 2:
            searchArray()
            mainMenu()
        elif choice == 3:
            quitProgram = True
            mainMenu()

#GPA ARRAY INTIALIZATION - This handles startup more or less. 
makeHeader("Program Startup - GPA Entry")

targetCount = input("How many GPA's would you like to enter?(default 10):")
if targetCount == "":
    targetCount = 10

while count < int(targetCount):
    count +=1
    gpa = input("Please enter GPA#" + str(count)+":")
    appendData(gpa)

mainMenu()
        
    
