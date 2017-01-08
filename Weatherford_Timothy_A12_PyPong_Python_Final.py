'''
Assignment 12 - Comprehensive Final
Programed by: Timothy Weatherford
Pong Game - Simple pong game with TKinter and canvas to draw game assets.
'''

#Imports
import tkinter
from tkinter import *


#Defines our pong game class - input is a TKinter frame object.
class Pong(Frame):
    ##Variables##
    player1 = 0
    player2 = 0
    #Initial ball position - overriden after a score
    ballX=50
    ballY=50
    ball = 0
    paddle1 = 0
    paddle2 = 0
    paddle1X = 2
    paddle1Y = 2
    paddle2X = 0
    paddle2Y = 2
    canvas = 0
    #Initial ball speed. Increase to make the game faster, and also, change negatives to change which player servers.
    ballDX = 2
    ballDY = -2
    #Initial Window Height and Width
    winHEIGHT = 600;
    winWIDTH = 800;
    #Change this to make keys more sensitive
    paddleSpeed = 25
    #Initial Score
    player1Points = 0
    player2Points = 0
    #Placeholder
    textLabel = 0

    #Displays tutorial instructions to the users    
    def introMsg(self):
       tkinter.messagebox.showinfo("Pong Instructions", "Player 1's paddle tracks the mouse.\n w: Player 1 Paddle Up \n s:  Player 1 Paddle Down \n o: Player 2 Paddle Up \n l:  Player 2 Paddle Down. \n Shift + Q to quit and output final score to file.")

    #Constructor Method
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.introMsg()
        self.pongUI()
        self.outputFile = open("finalScore.txt","w")
        
    #Kevboard Input Handler
    def key(self, event):
        global player1,player2
        print("Key Pressed:", repr(event.char))
        if event.char == 'w':
            if self.canvas.coords(self.paddle1)[1]>=0:
                self.canvas.move(self.paddle1,0,-self.paddleSpeed)
        if event.char == 's':
            if self.canvas.coords(self.paddle1)[3]<=self.winHEIGHT:
                self.canvas.move(self.paddle1,0,self.paddleSpeed)
        if event.char == 'o':
            if self.canvas.coords(self.paddle2)[1]>=0:
                self.canvas.move(self.paddle2,0,-self.paddleSpeed)
        if event.char == 'l':
            if self.canvas.coords(self.paddle2)[3]<=self.winHEIGHT:
                self.canvas.move(self.paddle2,0,self.paddleSpeed)
        if event.char == 'Q':
            self.outputTextFile()
            self.parent.destroy()

    #Handles mouse click
    def mouseHandler(self, event):
        self.focus_set()
        print("Clicked at coordinate:", event.x, event.y)

    #Handles Movement
    def motion(self, event):
        coords1 = self.canvas.coords(self.paddle1)
        height1 = coords1[3]-coords1[1]
        coords1[1] = event.y
        coords1[3] = event.y+height1
        self.canvas.coords(self.paddle1,coords1[0],coords1[1],coords1[2],coords1[3])

    #Creates text labels
    def createLabels(self):
        self.pongLabel = self.canvas.create_text(self.winWIDTH/2,10,text="COP1000 PyPong - by Tim Weatherford")
        self.scoreLabel = self.canvas.create_text(self.winWIDTH/2,25,text="Score:")
        self.updateScores()

    #Used for updating scores
    def deleteScores(self):
        self.canvas.delete(self.textLabel)        

    #Updates score   
    def updateScores(self):
        self.deleteScores()
        self.textLabel = self.canvas.create_text(self.winWIDTH/2,40, text="Player1 - " + str(self.player1Points)+" | Player 2 - " + str(self.player2Points))

    #Used to center a ball after a point is scored
    def centerBall(self):
        self.canvas.coords(self.ball,self.winWIDTH/2,self.winHEIGHT/2,self.winWIDTH/2+10,self.winHEIGHT/2+10)
        

    #Creates the TKinter UI  
    def pongUI(self):
        self.paddle2X = self.parent.winfo_screenwidth() - 15     
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)
        self.winHEIGHT = self.parent.winfo_screenheight()
        self.winWIDTH = self.parent.winfo_screenwidth()
        self.ball = self.canvas.create_oval(0+self.ballX, 0+self.ballY, 10+self.ballX, 10+self.ballY, outline="black", 
            fill="blue", width=1)
        self.paddle1 = self.canvas.create_rectangle(0+self.paddle1X, 0+self.paddle1Y, 10+self.paddle1X, 50+self.paddle1Y, outline="black", fill="yellow")
        self.paddle2 = self.canvas.create_rectangle(0+self.paddle2X, 0+self.paddle2Y, 10+self.paddle2X, 50+self.paddle2Y, outline="black", fill="yellow")
        self.createLabels()
        self.parent.bind("<Key>", self.key)
        self.parent.bind("<Button-1>", self.mouseHandler)
        self.parent.bind("<Motion>", self.motion)
        self.canvas.pack(fill=BOTH, expand=1)
        self.after(200, self.mvmtHandler)
        

    #Handles collision and window size for game logic
    def collisionHandler(self,coords1,coords2):
        height1 = coords1[3]-coords1[1]
        width1 = coords1[2]-coords1[0]
        height2 = coords2[3]-coords2[1]
        width2 = coords2[2]-coords2[0]
        return not (coords1[0] + width1 < coords2[0] or coords1[1] + height1 < coords2[1] or coords1[0] > coords2[0] + width2 or coords1[1] > coords2[1] + height2)

    #Defines the movement of the ball and increments score if the ball touches the edge.
    def mvmtHandler(self):
        self.canvas.move(self.ball,self.ballDX, self.ballDY)
        if self.canvas.coords(self.ball)[1] <= 0:
            self.ballDY = -self.ballDY
        if self.canvas.coords(self.ball)[3] >= self.winHEIGHT:
            self.ballDY = -self.ballDY
        if self.collisionHandler(self.canvas.coords(self.ball),self.canvas.coords(self.paddle1)) or self.collisionHandler(self.canvas.coords(self.ball),self.canvas.coords(self.paddle2)):
            self.ballDX = -self.ballDX
        if self.canvas.coords(self.ball)[0] <= 0:
            self.ballDX = -self.ballDX
            self.player2Points+=1
            self.canvas.delete(self.textLabel)
            self.updateScores()
            self.centerBall()
        if self.canvas.coords(self.ball)[2] >= self.winWIDTH:
            self.ballDX = -self.ballDX
            self.player1Points+=1
            self.updateScores()
            self.centerBall()
        self.after(10, self.mvmtHandler)

    #Makes header for output file
    def makeHeader(self,text="COP1000 PyPong Final Scores"):
        self.outputFile.write("=-"*30 + "\n")
        self.outputFile.write(text + "\n")
        self.outputFile.write("=-"*30 + "\n")

    #Makes a divider (between the score and credits).
    def makeDivider(self):
        self.outputFile.write("-"*60 + "\n")

    #Credits the programmer, professor, and school
    def giveCredit(self):
        self.makeHeader("Programmed by: Timothy Weatherford \nDSC COP100 - Intro to Programming | Professor: Bettye Parham")

    #Thanks the user for playing.
    def giveThanks(self):
        self.makeHeader("Thanks for playing PyPong! Play again soon!")

    #Gives credit and thanks to output file. 
    def cleanUp(self):
        self.makeDivider()
        self.giveCredit()
        self.giveThanks()
        self.outputFile.close()

    #Decides winner for output file.
    def decideWinner(self):
        if self.player1Points > self.player2Points:
            self.outputFile.write("Winner is Player 1!!! Congratulations Player 1!!!\n")
        elif self.player1Points < self.player2Points:
            self.outputFile.write("Winner is Player 2!!! Congratulations Player 2!!!\n")
        else:
            self.outputFile.write("The game was a draw! Good game to both players!\n")

    #Outputs the score to file.
    def outputScore(self):
        self.makeDivider()
        self.outputFile.write("Player 1's Score: " + str(self.player1Points) + " |  Player 2's Score: " + str(self.player2Points) + "\n")
        self.makeDivider()

    #Handles Output of score
    def outputTextFile(self):
        self.makeHeader()
        self.outputScore()
        self.decideWinner()
        self.cleanUp()

                        
#Begins our pong game loop. Shift + Q to break
def main():  
    root = tkinter.Tk()
    ex = Pong(root)
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()  

#Calls main
main()
