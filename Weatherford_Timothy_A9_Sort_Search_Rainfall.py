'''
Assignment#9: Rainfall Version - Sorts data, searches array, and outputs to file.
Programmer: Timothy Weatherford
Course: COP1000 - Intro to Computer Programming
'''
#Initial Variables
rainArray = []
count = 0
file = open("rainfallData.txt","r")
sortStatus = False
outputFile = open("Weatherford_Timothy_A9_Python_Rainfall_Output.txt", "w")

#Helper Methods
#prints header
def makeHeader(text):
    print("=-"*30)
    print(text)
    print("=-"*30)

#writes headers to file
def writeHeader(text):
    global outputFile
    outputFile.write("=-"*30 + "\n")
    outputFile.write(text + "\n")
    outputFile.write("=-"*30 + "\n")

#Appends data to array for us
def appendData(rain):
    global rainArray
    rainArray.append(float(rain))

#Searches the array for a a rain data of the users choice
def searchArray(outputFile):
    outputFile = outputFile
    count = 0
    targetCount = 0 
    writeHeader("Rain Data Search")
    searchString = input("Please enter rain data to search for:")
    global rainArray
    
    for rain in rainArray:
        if float(rain) == float(searchString):
            targetCount += 1

    outputFile.write("Your target rain data of " + str(searchString) + " occured " + str(targetCount) + " times." + "\n")
    print("-"*10)
    print("Your target rain data of " + str(searchString) + " occured " + str(targetCount) + " times." + "and the output has been saved to the file.")
    print("-"*10)
    
#Iterates array and displays each   
def displayArray(sortStatus,outputFile):
    outputFile = outputFile
    count = 0
    global rainArray
    if sortStatus == True:
        makeHeader("Display all rain data(sorted):")
        writeHeader("Display all rain datas(sorted):")
    else:
        makeHeader("Display all rain data(unsorted):")
        writeHeader("Display all rain data(unsorted):")
    for rain in rainArray:
        count += 1 
        outputFile.write("Rain Data#" + str(count) + " is:" + str(rainArray[count-1]) + "\n")
        print("Rain Data#" + str(count) + " is:" + str(rainArray[count-1]))
    print("The output has been prepared to the file. Please quit to save.")

#Sorts array
def sortArray(rainArray,targetCount):
    #Bubble sort variables
    flag = 0
    swap = 0
    while flag == 0:
        flag = 1
        swap = 0
        while swap < (int(targetCount)-1):
            if rainArray[swap] > rainArray[swap + 1]:
                tempRain = rainArray[swap]
                rainArray[swap] = rainArray[swap + 1]
                rainArray[swap + 1] = tempRain
                flag = 0
            swap = swap + 1
    sortStatus = True
    print("-"*10)
    print("The rain list has been sorted, please re-run 1 from the main menu to prepare the file for output.")
    print("-"*10)
    return sortStatus
    

#Main Menu 
def mainMenu():
    global targetCount, sortStatus, outputFile
    makeHeader("Main Menu")
    choice = int(input("Please choose 1 to display and output all rain entries to file, 2 to search rain data, 3 to sort rain data, or 4 to quit(writes file to disk):"))
    if choice == 1:
        displayArray(sortStatus,outputFile)
        mainMenu()
    elif choice == 2:
        searchArray(outputFile)
        mainMenu()
    elif choice == 3:
        sortStatus = sortArray(rainArray,targetCount)
        mainMenu()
    elif choice == 4:
        outputFile.close()
        pass
    else:
        print("Invalid Selection - Please choose again")
        mainMenu()


#RAIN ARRAY INTIALIZATION - This handles startup more or less. 
makeHeader("Program Startup - Rain Entry")

targetCount = input("How many rain data points are in the input file?(default 60):")
if targetCount == "":
    targetCount = 60

while count < int(targetCount):
    count +=1
    rain = float(file.readline().strip())
    appendData(rain)

mainMenu()
        
    
