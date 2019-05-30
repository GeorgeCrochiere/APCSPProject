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
global checkingProblem
global xUse
global yUse
global toCheckAnswer
global answerRefrence
global checkingAnswer
grade = 1
x = 4
y = 4
answer = 8
points = 0
xUse = 8
yUse = 8

def start():
    grade = (gradeText.get(1.0, END))
    labelStart = Label(root, text = 'Welcome to Math Points!')
    labelStart.grid(row = 2, column = 0, columnspan = 2)
    labelInstructions = Label(root, text = 'Answer all of the questions correctly to win! Pay close attention. The more questions correct, the harder the problems.')
    labelInstructions.grid(row = 3, column = 0, columnspan = 2)
    playButton = Button(root, text = 'Play!', command = problemPicker)
    playButton.grid(row = 4, column = 0, columnspan = 2)
    root.mainloop()

def makeProblemAdd():
    grade = int(gradeText.get(1.0, END))
    x = random.randint(1,15)
    y = random.randint(1,15)
    xUse = (x * grade)
    yUse = (y * grade)
    answer = xUse + yUse
    answerRefrence.insert(END, answer)
    labelProblem = Label(root, text = (str(xUse) +str(' + ') +str(yUse)))
    labelProblem.grid(row = 5, column = 0)
    answerProblem = Text(width = 10, height = 1)
    answerProblem.grid(row = 5, column = 1)
    checkAnswer = Button(root, text = 'Check', command = onClick)
    checkAnswer.grid(row = 6, column = 0, columnspan = 2)
    
def makeProblemSubtract():
    grade = int(gradeText.get(1.0, END))
    x = random.randint(1,15)
    y = random.randint(1,15)
    xUse = (x * grade)
    yUse = (y * grade)
    answer = xUse - yUse
    answerRefrence.insert(END, answer)
    labelProblem = Label(root, text = (str(xUse) +str(' - ') +str(yUse)))
    labelProblem.grid(row = 5, column = 0)
    answerProblem = Text(width = 10, height = 1)
    answerProblem.grid(row = 5, column = 1)
    checkAnswer = Button(root, text = 'Check', command = onClick)
    checkAnswer.grid(row = 6, column = 0, columnspan = 2)
    
def makeProblemMultiply():
    grade = int(gradeText.get(1.0, END))
    x = random.randint(1,15)
    y = random.randint(1,15)
    xUse = (x * grade)
    yUse = (y * grade)
    answer = xUse * yUse
    answerRefrence.insert(END, answer)
    labelProblem = Label(root, text = (str(xUse) +str(' x ') +str(yUse)))
    labelProblem.grid(row = 5, column = 0)
    answerProblem = Text(width = 10, height = 1)
    answerProblem.grid(row = 5, column = 1)
    checkAnswer = Button(root, text = 'Check', command = onClick)
    checkAnswer.grid(row = 6, column = 0, columnspan = 2)
    
def makeProblemDivide():
    grade = int(gradeText.get(1.0, END))
    x = random.randint(1,15)
    y = random.randint(1,15)
    xUse = (x * grade)
    yUse = (y * grade)
    answer = xUse / yUse
    answerRefrence.insert(END, answer)
    labelProblem = Label(root, text = (str(xUse) +str(' / ') +str(yUse)))
    labelProblem.grid(row = 5, column = 0)
    answerProblem = Text(width = 10, height = 1)
    answerProblem.grid(row = 5, column = 1)
    checkAnswer = Button(root, text = 'Check', command = onClick)
    checkAnswer.grid(row = 6, column = 0, columnspan = 2)

def onClick():
    checkProblem((answerRefrence.get(1.0,END)),(answerProblem.get(1.0,END)))

def checkProblem(checkingAnswer, checkingProblem):
    print checkingAnswer
    print checkingProblem
    if checkingAnswer == checkingProblem:
        print ('test1')
        answerRefrence.delete(1.0,END)
        answerProblem.delete(1.0,END)
        points += 1
        labelCorrectness = Label(root, text = 'Correct!')
        labelCorrectness.grid(row = 7, column = 0, columnspan = 2)
        nextProblem = Button(root, text = 'Next Prblem', command = problemPicker)
    else:
        print ('test2')
        labelCorrectness = Label(root, text = 'Incorrect, try again.')
        labelCorrectness.grid(row = 7, column = 0, columnspan = 2)
        
def problemPicker():
    if points >= 16:
        print ('this is all good')
    else:
        if points >= 12:
            makeProblemDivide()
        else:
            if points >=8:
                makeProblemMultiply()
            else:
                if points >=4:
                    makeProblemSubtract()
                else:
                    makeProblemAdd()

def debug():
    print grade

answerRefrence = Text(width = 10, height = 1)
answerProblem = Text(width = 10, height = 1)

def temp():
    return answerProblem.get(1.0,END)

labelGrade = Label(root, text = 'Please input grade (1-4): ')
labelGrade.grid(row = 0, column = 0)
gradeText = Text(width = 10, height = 1)
gradeText.grid(row = 0, column = 1)
ContinueButton = Button(root, text = 'Continue', command=start)
ContinueButton.grid(row = 1, column = 0, columnspan = 2)

root.mainloop()
