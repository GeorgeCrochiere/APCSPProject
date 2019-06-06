import cmath
import random
from Tkinter import *
root = Tk()
root.title("Math Points")

global points
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
global answerProblem
global solution
global labelCorrectness
global labelCorrectnessVar
global pointsVar
#global nextProblem
labelCorrectnessVar = StringVar()
pointsVar = StringVar()
grade = 1
x = 4
y = 4
answer = 8
points = 0
xUse = 8
yUse = 8
solution = 2

def start():
    grade = (gradeText.get())
    global points
    points = 0
    pointsVar.set(str(points))
    answerRefrence.delete(0,99)
    answerProblem.delete(0,99)
    answerProblem.config(state = 'normal')
    gradeText.config(state = 'disabled')
    
    problemPicker()

def makeProblemAdd():
    grade = int(gradeText.get())
    x = random.randint(1,15)
    y = random.randint(1,15)
    xUse = (x * grade)
    yUse = (y * grade)
    answer = xUse + yUse
    answerRefrence.insert(END, answer)
    labelProblem = Label(root, text = (('   ') + str(xUse) +str(' + ') +str(yUse) + ('   ')))
    labelProblem.grid(row = 6, column = 0)
    checkAnswer = Button(root, text = 'Check', command = onClick)
    checkAnswer.grid(row = 7, column = 0, columnspan = 2)
    
def makeProblemSubtract():
    grade = int(gradeText.get())
    x = random.randint(10,15)
    y = random.randint(1,9)
    xUse = (x * grade)
    yUse = (y * grade)
    answer = xUse - yUse
    answerRefrence.insert(END, answer)
    labelProblem = Label(root, text = (('   ') + str(xUse) +str(' - ') +str(yUse) +('   ')))
    labelProblem.grid(row = 6, column = 0)
    checkAnswer = Button(root, text = 'Check', command = onClick)
    checkAnswer.grid(row = 7, column = 0, columnspan = 2)
    
def makeProblemMultiply():
    grade = int(gradeText.get())
    x = random.randint(1,2)
    y = random.randint(1,10)
    xUse = (x * grade)
    yUse = (y * grade)
    answer = xUse * yUse
    answerRefrence.insert(END, answer)
    labelProblem = Label(root, text = (('   ') + str(xUse) +str(' x ') +str(yUse) + ('   ')))
    labelProblem.grid(row = 6, column = 0)
    checkAnswer = Button(root, text = 'Check', command = onClick)
    checkAnswer.grid(row = 7, column = 0, columnspan = 2)
    
def makeProblemDivide():
    grade = int(gradeText.get())
    x = random.randint(1,16)
    y = random.randint(1,3)
    xUse = (x * grade)
    randomChoice = random.randint(1,2)
    if randomChoice == 1:
        yUse = y
    if randomChoice == 2:
        yUse = (y * grade)
    answer = round((xUse / float(yUse)), 3)
    answerRefrence.insert(END, answer)
    labelProblem = Label(root, text = (('   ') + str(xUse) +str(' / ') +str(yUse) + ('   ')))
    labelProblem.grid(row = 6, column = 0)
    checkAnswer = Button(root, text = 'Check', command = onClick)
    checkAnswer.grid(row = 7, column = 0, columnspan = 2)

def onClick():
    solution = (answerProblem.get())
    checkProblem((answerRefrence.get()),solution)

def checkProblem(checkingAnswer, checkingProblem):
    print checkingAnswer
    print checkingProblem
    if checkingAnswer == checkingProblem:
        print ('test1')
        answerRefrence.delete(0,99)
        answerProblem.delete(0,99)
        global points
        points += 1
        pointsVar.set(str(points))
        labelCorrectnessVar.set('Correct!')
        labelCorrectness.grid(row = 8, column = 0, columnspan = 2)
        #nextProblem = Button(root, text = 'Next Problem', command = problemPicker, state=NORMAL)
        #nextProblem.grid(row = 8, column = 0, columnspan = 2)
        #nextProblem.config(state=NORMAL)
        problemPicker()
    else:
        print ('test2')
        labelCorrectnessVar.set('Incorrect, try again.')
        labelCorrectness.grid(row = 9, column = 0, columnspan = 2)
        #nextProblem.config(state=DISABLED)
        
def problemPicker():
    #nextProblem.config(state=DISABLED)
    if points >= 16:
        print ('this is all good')
        congrats()
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

def congrats():
    congratsWindow = Toplevel()
    congratsWindow.title('You Win!')
    congratsLabel = Label(congratsWindow, text ='Congragulations!', fg = 'red')
    congratsLabel2 = Label(congratsWindow, text = 'You completed all 16 problems!', fg = 'red')
    congratsLabel.grid(row = 0, column = 0)
    congratsLabel2.grid(row = 1, column = 0)
    canvas = Canvas(congratsWindow, height=600, width=600, relief=RAISED, bg='azure')
    canvas.grid(row = 2, column = 0)
    canvas.create_polygon(0, 0, 600, 0, 300, 400, fill = 'blue', outline = 'blue')
    canvas.create_polygon(100, 0, 500, 0, 300, 266.667, fill = 'azure', outline = 'azure')
    canvas.create_oval(375, 325, 225, 475, fill = 'gold', outline = 'gold')
    canvas.create_oval(350, 350, 250, 450, fill = 'gold', outline = 'goldenrod')

def debug():
    print (answerProblem.get(1.0, END))

answerRefrence = Entry(width = 10)
answerProblem = Entry(width = 10, state = 'disabled')
answerProblem.grid(row = 6, column = 1)

labelStart = Label(root, text = 'Welcome to Math Points!', fg = 'red')
labelStart.grid(row = 0, column = 0, columnspan = 2)
labelInstructions = Label(root, text = 'Answer all 16 questions correctly to win! Pay close attention. The more questions correct, the harder the problems.')
labelInstructions2 = Label(root, text = 'For all division problems, round to the thousandths place. If it is a whole number, end it with ".0". \n Leave EVERYTHING as whole numbers. \n The ENTER key will not work. Click the appropiate buttons.')
labelInstructions3 = Label(root, text = 'This is intended for those is late elementary school (4th grade) up to those in middle school (7-8th grade) with the intent to help sharpen mental math skills.')
labelInstructions.grid(row = 1, column = 0, columnspan = 2)
labelInstructions2.grid(row = 2, column = 0, columnspan = 2)
labelInstructions3.grid(row = 3, column = 0, columnspan = 2)
labelGrade = Label(root, text = 'Please input difficulty (1-4): ')
labelGrade.grid(row = 4, column = 0)
gradeText = Entry(width = 10)
gradeText.grid(row = 4, column = 1)
playButton = Button(root, text = 'Play!', command = start)
playButton.grid(row = 5, column = 0, columnspan = 2)
labelCorrectness = Label(root, textvariable = labelCorrectnessVar)
pointsLabel = Label(root, textvariable = pointsVar)
pointsLabel.grid(row = 11, column = 0, columnspan = 2)
#nextProblem = Button(root, text = 'Next Problem', command = problemPicker, state=DISABLED)

root.mainloop()
