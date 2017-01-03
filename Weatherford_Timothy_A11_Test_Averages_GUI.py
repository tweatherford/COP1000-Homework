'''
Assignment 11: Test averages revisited
Programmed by: Timothy Weatherford
Makes use of TKinter
'''
#Imports the TKinter Library
import tkinter

#Creates class
class testAvg:
    #Constructor method
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Average Calculator")

        #Create the frames.
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.test4_frame = tkinter.Frame(self.main_window)
        self.test5_frame = tkinter.Frame(self.main_window)
        self.test6_frame = tkinter.Frame(self.main_window)
        self.test7_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.letterGrade_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        #Widgets for test 1
        self.test1_label = tkinter.Label(self.test1_frame, text="Enter the scores for test 1:")
        self.test1_entry = tkinter.Entry(self.test1_frame, width = 10)
        self.test1_label.pack(side = "left")
        self.test1_entry.pack(side = "left")

        #Widgets for test 2
        self.test2_label = tkinter.Label(self.test2_frame, text="Enter the scores for test 2:")
        self.test2_entry = tkinter.Entry(self.test2_frame, width = 10)
        self.test2_label.pack(side = "left")
        self.test2_entry.pack(side = "left")

        #Widgets for test 3
        self.test3_label = tkinter.Label(self.test3_frame, text="Enter the scores for test 3:")
        self.test3_entry = tkinter.Entry(self.test3_frame, width = 10)
        self.test3_label.pack(side = "left")
        self.test3_entry.pack(side = "left")

        #Widgets for test 4
        self.test4_label = tkinter.Label(self.test4_frame, text="Enter the scores for test 4:")
        self.test4_entry = tkinter.Entry(self.test4_frame, width = 10)
        self.test4_label.pack(side = "left")
        self.test4_entry.pack(side = "left")

        #Widgets for test 5
        self.test5_label = tkinter.Label(self.test5_frame, text="Enter the scores for test 5:")
        self.test5_entry = tkinter.Entry(self.test5_frame, width = 10)
        self.test5_label.pack(side = "left")
        self.test5_entry.pack(side = "left")

        #Widgets for test 6
        self.test6_label = tkinter.Label(self.test6_frame, text="Enter the scores for test 6:")
        self.test6_entry = tkinter.Entry(self.test6_frame, width = 10)
        self.test6_label.pack(side = "left")
        self.test6_entry.pack(side = "left")

        #Widgets for test 7
        self.test7_label = tkinter.Label(self.test7_frame, text="Enter the scores for test 7:")
        self.test7_entry = tkinter.Entry(self.test7_frame, width = 10)
        self.test7_label.pack(side = "left")
        self.test7_entry.pack(side = "left")

        #Test Average Widgets
        self.results_label = tkinter.Label(self.avg_frame, text = "Average: ")
        self.avg = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.avg_frame, textvariable= self.avg)
        self.results_label.pack(side = "left")
        self.avg_label.pack(side = "left")

        #Letter Grade Widgets
        self.grade_label = tkinter.Label(self.letterGrade_frame, text = "Letter Grade:")
        self.grade = tkinter.StringVar()
        self.gradeResults_label = tkinter.Label(self.letterGrade_frame, textvariable= self.grade)
        self.grade_label.pack(side = "left")
        self.gradeResults_label.pack(side = "left")
        

        #Creates buttons
        self.calc_button = tkinter.Button(self.button_frame, text = "Average", command=self.calc_avg)
        self.grade_button = tkinter.Button(self.button_frame, text = "Letter Grade", command=self.calc_grade)
        self.quit_button = tkinter.Button(self.button_frame, text = "Quit", command = self.main_window.destroy)
        self.calc_button.pack(side = "left")
        self.grade_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        

        #Pack the frames
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.test4_frame.pack()
        self.test5_frame.pack()
        self.test6_frame.pack()
        self.test7_frame.pack()
        self.letterGrade_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        #Starts main loop
        tkinter.mainloop()

    def calc_avg(self):
        #Get the test scores as variables
        self.test1= float(self.test1_entry.get())
        self.test2= float(self.test2_entry.get())
        self.test3= float(self.test3_entry.get())
        self.test4= float(self.test4_entry.get())
        self.test5= float(self.test5_entry.get())
        self.test6= float(self.test6_entry.get())
        self.test7= float(self.test7_entry.get())

        #Calculate Average
        self.average = (self.test1 + self.test2 + self.test3 + self.test4 + self.test5 + self.test6 + self.test7)/7.00

        #Updates label
        self.avg.set(self.average)

    def calc_grade(self):
##        #Get the test scores as variables
##        self.test1= float(self.test1_entry.get())
##        self.test2= float(self.test2_entry.get())
##        self.test3= float(self.test3_entry.get())
##        self.test4= float(self.test4_entry.get())
##        self.test5= float(self.test5_entry.get())
##        self.test6= float(self.test6_entry.get())
##        self.test7= float(self.test7_entry.get())
##
##        self.average = (self.test1 + self.test2 + self.test3 + self.test4 + self.test5 + self.test6 + self.test7)/

        if self.average < 60:
            self.grade.set("F")
        elif self.average >= 60 and self.average < 70:
            self.grade.set("D")
        elif self.average >= 70 and self.average < 80:
            self.grade.set("C")
        elif self.average >= 80 and self.average < 90 :
            self.grade.set("B")
        else:
            self.grade.set("A")
            
            

'''
Main Program Call
'''
testAverage = testAvg()
        
