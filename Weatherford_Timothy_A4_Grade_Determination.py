##-----------------------------------------------------------
##Programmed by: Tim Weatherford
##Assignment 4 - Displays the average of x number of tests along with a letter grade.
##Created 11/11/16 - v1.0
##-----------------------------------------------------------

letterGrade = "Unknown Grade"

#Prints the introduction - just for presentation.
def displayIntro(title):
    print("=-"*30)
    print(title)
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

#Logic to determine letter grade
def letterGrade(score):
    if score <= 59.99:
        letterGrade = "F"
    elif score >= 60 and score < 66.99:
        letterGrade = "D"
    elif score >= 67 and score < 69.99:
        letterGrade = "D+"
    elif score >= 70 and score < 76.99:
        letterGrade = "C"
    elif score >= 77 and score < 79.99:
        letterGrade = "C+"
    elif score >= 80 and score < 86.99:
        letterGrade = "B"
    elif score >= 87 and score < 89.99:
        letterGrade = "B+"
    elif score >= 90 and score < 96.99:
        letterGrade = "A"
    else:
        letterGrade = "A+"
    return letterGrade
        

#This method accepts our data as input and prepares the final output.
def displayReport(student,qty,tests,testSum,testAvg):
    count = 0
    title = "Grade Report for " + student
    displayIntro(title)
    print("Student:" +student)
    for test in tests:
        count += 1
        print("Score for Test#"+ str(count) + ":" + str(test))
    print("Qty of Tests Scored:" + str(count))
    print("Average Test Score:" + str(format(testAvg, ".2f")))
    print("Letter Grade:" + letterGrade)
    print("Total Test Points:" + str(testSum))
    print("=-"*30)
    print("End " + student + "'s Grade Report")



##End Helper Methods##

#Presentation
displayIntro("Student Grade Reporting System")
#Program Main Loop - getters and setters.          
student = getStudent()
qty = getQty()
tests = getTests()
testSum = getSum(tests)
testAvg = testSum/qty
letterGrade = letterGrade(testAvg)

#Empty Lines - for presentation. Seperates user input from the output report.
print("")
print("-"*60)
print("")

#Output - Presents data to the user.
displayReport(student,qty,tests,testSum,testAvg)

