##-----------------------------------------------------------
##Programmed by: Tim Weatherford
##Assignment 2 - Displays the average of x number of tests.
##Created 10/29/16 - v1.0
##-----------------------------------------------------------


#Prints the introduction - just for presentation.
print("Student Grade Report System")
print("=-"*30)

##Begin Helper Methods##

#This method gets the desired student from the user.
def getStudent():
    student = str(input("Enter the student's name:"))
    return student

#This method gets the desired quantity of tests to score from the user.
def getQty():
    qty = int(input("Enter the number of tests to input for this student:"))
    return qty

#This method gets the test scores from the user.
def getTests():
    count = 0
    tests = []
    while count!= qty:
       count = count + 1
       score = int(input('Enter the score for test#{0}:'.format(count)))
       tests.insert(count - 1, score)
    return tests

#This method adds the total points of all tests.
def getSum(tests):
    testSum = 0
    for test in tests:
        testSum = testSum + test
    return testSum

#This method accepts our data as input and prepares the final output.
def displayReport(student,qty,tests,testSum,testAvg):
    count = 0
    print("Grade Report for " + student)
    print("=-"*30)
    print("Student:" +student)
    for test in tests:
        count = count + 1 
        print("Score for Test#"+ str(count) + ":" + str(test))
    print("Qty of Tests Scored:" + str(count))
    print("Average Test Score:" + str(testAvg))
    print("Total Test Points:" + str(testSum))
    print("=-"*30)
    print("End " + student + "'s Grade Report")

##End Helper Methods##

#Program Main Loop - getters and setters.          
student = getStudent()
qty = getQty()
tests = getTests()
testSum = getSum(tests)
testAvg = testSum/qty

#Empty Lines - for presentation. Seperates user input from the output report.
print("")
print("-"*60)
print("")

#Output - Presents data to the user.
displayReport(student,qty,tests,testSum,testAvg)

