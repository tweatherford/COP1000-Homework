'''
Assignment#9: Sorts and searches array plus outputs to file.
Programmer: Timothy Weatherford
Course: COP1000 - Intro to Computer Programming
'''
#Initial Variables
gpaArray = []
count = 0
file = open("studentGPA.txt","r")
sortStatus = False
outputFile = open("Weatherford_Timothy_A10_Python_GPA_Output.txt", "w")

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
def appendData(gpa):
    global gpaArray
    gpaArray.append(float(gpa))

#Searches the array for a a GPA of the users choice
def searchArray(outputFile):
    outputFile = outputFile
    count = 0
    targetCount = 0 
    writeHeader("GPA Search")
    searchString = input("Please enter a GPA to search for:")
    global gpaArray
    
    for gpa in gpaArray:
        if float(gpa) == float(searchString):
            targetCount += 1

    outputFile.write("Your target GPA of " + str(searchString) + " occured " + str(targetCount) + " times." + "\n")
    print("-"*10)
    print("Your target GPA of " + str(searchString) + " occured " + str(targetCount) + " times." + "and the output has been saved to the file.")
    print("-"*10)
    
#Iterates array and displays each   
def displayArray(sortStatus,outputFile):
    outputFile = outputFile
    count = 0
    global gpaArray
    if sortStatus == True:
        makeHeader("Display all GPA's(sorted):")
        writeHeader("Display all GPA's(sorted):")
    else:
        makeHeader("Display all GPA's(unsorted):")
        writeHeader("Display all GPA's(unsorted):")
    for gpa in gpaArray:
        count += 1 
        outputFile.write("Gpa#" + str(count) + " is:" + str(gpaArray[count-1]) + "\n")
        print("Gpa#" + str(count) + " is:" + str(gpaArray[count-1]))
    print("The output has been prepared to the file. Please quit to save.")

#Sorts array
def sortArray(gpaArray,targetCount):
    #Bubble sort variables
    flag = 0
    swap = 0
    while flag == 0:
        flag = 1
        swap = 0
        while swap < (int(targetCount)-1):
            if gpaArray[swap] < gpaArray[swap + 1]:
                tempGPA = gpaArray[swap]
                gpaArray[swap] = gpaArray[swap + 1]
                gpaArray[swap + 1] = tempGPA
                flag = 0
            swap = swap + 1
    sortStatus = True
    print("-"*10)
    print("The GPA list has been sorted, please re-run 1 from the main menu to prepare the file for output.")
    print("-"*10)
    return sortStatus

#Outputs statistics at the end
def makeStats(targetCount,outputFile):
    global gpaArray
    length = len(gpaArray)
    average = round(sum(gpaArray)/len(gpaArray),2)
    tempArray = []
    writeHeader("The highest GPA in the list is: " + str(gpaArray[0]) + "\n")
    writeHeader("The lowest GPA in the list is: " + str(gpaArray[-1]) + "\n")
    writeHeader("The median GPA in the list is: " + str(gpaArray[length//2]) + "\n")
    writeHeader("The average GPA is: : " + str(average) + "\n")
    writeHeader("GPA's between 2.50 and 3.50:")

    for gpa in gpaArray:
        if gpa >= 2.50 and gpa <= 3.50:
            tempArray.append(gpa)

    for temp in tempArray:
        outputFile.write("GPA: " + str(temp) + "\n")

    writeHeader("Number of GPA's between 2.50 and 3.50: " + str(len(tempArray)))
        

    writeHeader("Programmed by: Timothy Weatherford, Executed by you! Thanks!" + "\n")
    

#Main Menu 
def mainMenu():
    global targetCount, sortStatus, outputFile
    makeHeader("Main Menu")
    choice = int(input("Please choose 1 to display and output all GPA entries to file, 2 to search GPA's, 3 to sort GPAs, or 4 to quit(writes file to disk):"))
    if choice == 1:
        displayArray(sortStatus,outputFile)
        mainMenu()
    elif choice == 2:
        searchArray(outputFile)
        mainMenu()
    elif choice == 3:
        sortStatus = sortArray(gpaArray,targetCount)
        mainMenu()
    elif choice == 4:
        #Sort if not sorted.
        if sortStatus == False:
            sortStatus = sortArray(gpaArray,targetCount)
        makeStats(targetCount,outputFile)            
        outputFile.close()
        pass
    else:
        print("Invalid Selection - Please choose again")
        mainMenu()


#GPA ARRAY INTIALIZATION - This handles startup more or less. 
makeHeader("Program Startup - GPA Entry")

targetCount = input("How many GPA's are in the input file?(default 25):")
if targetCount == "":
    targetCount = 25

while count < int(targetCount):
    count +=1
    gpa = float(file.readline().strip())
    appendData(gpa)

mainMenu()
        
    
