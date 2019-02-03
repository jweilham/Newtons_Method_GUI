from tkinter import *

# Returns true if user has entered a new equation
# Stores new equation into our current equation as well
def is_new_equation(self):

	self.equationValidation()
	
	four = float(self.fourth.get())
	three = float(self.third.get())
	two = float(self.second.get())
	one = float(self.first.get())
	constant = float(self.constant.get())

	newEquation = [four, three, two, one, constant]

	if(newEquation == self.math.equation):
		return False
    # There is a new equation
	else:
		del self.newtonValues[:]
		del self.math.equation[:]
		self.math.equation= newEquation
		return True

# validates user guess
# checks for if guess is the same to avoid running the Newton method multiple times
# returns tuple of (bool valid, bool same, float guess)
def validate_guess(self):

	try:
		same = False
		
		guess = float(self.guess.get())
		
		if(guess == self.currentGuess):
			same = True
		else:
			self.currentGuess = guess
		
		self.guessLabel["text"] = ""
		return (True, same, guess)

	# If it isn't a number, then delete what's inside it and label it invalid
	except ValueError:
		self.guess.delete(0, 'end')
		self.guessLabel["text"] = "invalid"
		return (False, -1, same)

# Grabs user inputted accuracy in decimals, defaults to 7
def getAccuracy(self):

		#adds together strings to set the accuracy
		acc1 ='%.'
		acc2 =  'f'
		
		#try to see if the accuracy entered is a number, if it is then make acc equal to the string of it
		try:
			k = int(self.acc.get())
			acc = str(k)
		except ValueError:
			self.acc.delete(0, 'end')
			self.acc.insert(0, 7)
			acc = '7'
		if(int(self.acc.get()) > 15):
			acc = '7'
		
		accuracy = acc1 + acc + acc2

		return accuracy



# If equation input is invalid, or empty, delete and replace it with a default 0
def equationValidation(self):

	try:
		four = float(self.fourth.get())
	except ValueError:
		self.fourth.delete(0, 'end')
		self.fourth.insert(0, 0)

	try:
		three = float(self.third.get())
	except ValueError:
		self.third.delete(0, 'end')
		self.third.insert(0, 0)
		
	try:
		two = float(self.second.get())
	except ValueError:
		self.second.delete(0, 'end')
		self.second.insert(0, 0)

	try:
		one = float(self.first.get())
	except ValueError:
		self.first.delete(0, 'end')
		self.first.insert(0, 0)
		
	try:
		constant = float(self.constant.get())
	except:
		self.constant.delete(0, 'end')
		self.constant.insert(0, 0)


def addTitle(self, title):
	Label(self, text = title, fg = "blue", font = ("Times", 25)).grid(columnspan=20)


def exampleLink(self):
	webbrowser.open('http://tutorial.math.lamar.edu/Classes/CalcI/NewtonsMethod.aspx')



#Function that adds entries and labels and everything on the GUI for it to work   
def addGUI(self):

	Label(self, text = "").grid(row = 1, column = 0)
	Label(self, text = "Enter Function:").grid(row=2, column = 0)

	Label(self, text = "x^4", justify = LEFT).grid(row = 2, column = 2)
	self.fourth = Entry(self, justify = RIGHT, width = 5)
	self.fourth.grid(row = 2, column = 1)

	
	Label(self, text = "x^3").grid(row=2, column = 4)
	self.third = Entry(self, justify = RIGHT, width = 5)
	self.third.grid(row = 2, column = 3)

	Label(self, text = "x^2").grid(row=2, column = 6)
	self.second = Entry(self, justify = RIGHT, width = 5)
	self.second.grid(row = 2, column = 5)

	Label(self, text = "x").grid(row=2, column = 8)
	self.first = Entry(self, justify = RIGHT, width = 5)
	self.first.grid(row = 2, column = 7)

	Label(self, text = "Constant").grid(row=2, column = 10)
	self.constant = Entry(self, justify = RIGHT, width = 5)
	self.constant.grid(row = 2, column = 9)

	Label(self, text = "").grid(row=4, column =0)

	Label(self, text = "Accuracy (decimal places)").grid(row=6, column = 0)
	self.acc = Entry(self, justify = LEFT, width = 5)
	self.acc.grid(row = 6, column = 1)

	Label(self, text = "Guess for the root").grid(row = 5, column = 0)
	self.guess = Entry(self, justify = LEFT, width = 5)
	self.guess.grid(row=5, column = 1)
	
	self.guessLabel = Label(self, anchor = "w", relief = "flat")
	self.guessLabel.grid(row=5, column = 2, sticky = "we")
	
	self.solveNewton = Button(self, text = "Solve with Newton's Method", command = self.solve_with_newton).grid(row=8, column = 0)
	self.graphFunction = Button(self, text = "Graph Function", command= lambda: self.graphEquation(1) ).grid(row=3, column = 0)
	Label(self, text = "").grid(row=7, column =0)
	Label(self, text = "Root =").grid(row = 9, column = 0)
	
	#creates label for root and a fake entry box (gridding a label) for showing the root
	self.rootLabel = Label(self, anchor = "w", relief = "ridge")
	self.rootLabel.grid(row=9, column = 1, sticky = "we")
	
	self.showWork = Button(self, text = "Show Work", command = self.showWork).grid(row=10, column = 0)
	self.link = Button(self, text = "Explanation of Newton's Method", command = self.exampleLink).grid(row=11, column = 0)

