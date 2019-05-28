import cmath
import random
from Tkinter import *
root = Tk()

global points
global answerProblem
global grade
global gradeText
global x
global y
global answer
grade = 1
x = 4
y = 4
answer = 8
points = 0

def start():
    grade = (gradeText.get(1.0, END))
    labelStart = Label(root, text = 'Welcome to Math Points!')
    labelStart.grid(row = 2, column = 0, columnspan = 2)
    labelInstructions = Label(root, text = 'Answer all of the questions correctly to win! Pay close attention. The more questionsd correct, the harder the problems.')
    labelInstructions.grid(row = 3, column = 0, columnspan = 2)
    playButton = Button(root, text = 'Play!', command = problemPicker)
    playButton.grid(row = 4, column = 0, columnspan = 2)
    root.mainloop()

def makeProblemAdd():
    x = random.randint(1,15)
    y = random.randint(1,15)
    x = x * grade
    y = y * grade
    answer = x + y
    labelProblem = Label(root, text = (str(x) +str(' + ') +str(y)))
    labelProblem.grid(row = 5, column = 0)
    answerProblem = Text(width = 10, height = 1)
    answerProblem.grid(row = 5, column = 1)
    checkAnswer = Button(root, text = 'Check', command = checkProblem)
    
def makeProblemSubtract():
    x = random.randint(1,15)
    y = random.randint(1,15)
    x = x * grade
    y = y * grade
    answer = x - y
    labelProblem = Label(root, text = (str(x) +str(' - ') +str(y)))
    labelProblem.grid(row = 5, column = 0)
    answerProblem = Text(width = 10, height = 1)
    answerProblem.grid(row = 5, column = 1)
    checkAnswer = Button(root, text = 'Check', command = checkProblem)
    
def makeProblemMultiply():
    x = random.randint(1,15)
    y = random.randint(1,15)
    x = x * grade
    y = y * grade
    answer = x * y
    labelProblem = Label(root, text = (str(x) +str(' x ') +str(y)))
    labelProblem.grid(row = 5, column = 0)
    answerProblem = Text(width = 10, height = 1)
    answerProblem.grid(row = 5, column = 1)
    checkAnswer = Button(root, text = 'Check', command = checkProblem)
    
def makeProblemDivide():
    x = random.randint(1,15)
    y = random.randint(1,15)
    x = x * grade
    y = y * grade
    answer = x / y
    labelProblem = Label(root, text = (str(x) +str(' / ') +str(y)))
    labelProblem.grid(row = 5, column = 0)
    answerProblem = Text(width = 10, height = 1)
    answerProblem.grid(row = 5, column = 1)
    checkAnswer = Button(root, text = 'Check', command = checkProblem)
    
def checkProblem():
    if answer is (answerProblem.get):
        labelCorrectness = Label(root, text = 'Correct!')
        labelCorrectness.grid(row = 6, column = 0, columnspan = 2)
        nextProblem = Button(root, text = 'Next Prblem', command = problemPicker)
    else:
        labelCorrectness = Label(root, text = 'Incorrect, try again.')
        labelCorrectness.grid(row = 6, column = 0, columnspan = 2)
        
def problemPicker():
    if points >=4:
        ###Here

def debug():
    print grade

labelGrade = Label(root, text = 'Please input grade (1-4): ')
labelGrade.grid(row = 0, column = 0)
gradeText = Text(width = 10, height = 1)
gradeText.grid(row = 0, column = 1)
ContinueButton = Button(root, text = 'Continue', command=start)
ContinueButton.grid(row = 1, column = 0, columnspan = 2)

root.mainloop()
