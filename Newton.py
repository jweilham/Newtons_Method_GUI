from tkinter import *
from numpy import linspace
from matplotlib import pyplot as plt
import webbrowser


# Sets x to every number from (-10 to 10) for graphing functions
x = linspace(-10, 10, 2000)

# Inherit from Tkinter to make basic GUI
class Newton_GUI(Tk):

    def __init__(self):
        Tk.__init__(self)
    
        self.title("Newton's Method")
        self.addTitle("Newton's Method") 
        self.addGUI()
        

    # Function for finding the value of the derivative of a function at any given x point
    def derive(self, x):

        # Set h to a value really close to 0 to simulate the limit as h goes to 0
        h=0.00000000000001

        # Use derivative identity
        derivative = (self.formula(x + h) - self.formula(x)) / h
        
        return derivative


    # Graphs tangent lines by using Newton's method
    def graphTan(self):
        
        self.graphEquation(0)
        
        #calls formula to set entries of empty values = 0
        self.formula(0)
        
        k = 0
        # Check to see if the root guess is a number and label it valid
        try:
            k = float(self.guess.get())
            self.guessLabel["text"] = ""

        # If it isn't a number, then delete what's inside it and label it invalid
        except ValueError:
            self.guess.delete(0, 'end')
            self.guessLabel["text"] = "invalid"
            return
        
        # Gets our array of 
        xValues = self.newton(float((self.guess.get())))

        # If 0, then newton method failed, so do not graph
        if (xValues == 0):
            return



        #iterate through and graph the tangent lines with the xValue in the list
        z = 0
        for i in xValues:
            plt.plot(x, self.tan(i))
            plt.pause(0.3)
            z+=1

    
        
    # Executes Newton's Method
    # Returns an array of values for Newton's method calculations
    # Starts computation with initial x value of the user's guess of the root
            
    def newton(self, current_x):

        if(float(self.fourth.get()) and float(self.third.get()) and float(self.second.get()) and float(self.first.get()) and float(self.constant.get()) == 0):
            return 0

        accuracy = self.getAccuracy();
        xValues = []
        answer = False
        iterations = 0

        while (answer == False):
        
            x1 = current_x
            
            # If derivative is 0, tangent line will never hit x axis, no solution
            try:

                # update our current_x according to Newton's method formula
                current_x = (current_x - (self.formula(current_x)/(self.derive(current_x))))
                
            except ZeroDivisionError:
                self.rootLabel["text"] = "No root"
                return 0
            
            xValues.insert(iterations, current_x) 
            iterations+=1

            # After 100 iterations, it's an infinite loop with no answer/root
            if(iterations>100):
                self.rootLabel["text"] = "No root"
                return 0
    
            # If we get the same value for our answer as the last iteration,
            # Then Newton's Method has been satisfied and we have our answer
            if (accuracy%(current_x) == accuracy%(x1)):
                answer = True
                self.rootLabel["text"] = accuracy % current_x
                return xValues


    # Finds the equation of the tangent line to the curve at any given x point      
    def tan(self, a):
        
        m = self.derive(a)
        y = self.formula(a)

        #point slope formula, a represents the x value at any given point, and I added the y to this side from the original point slope form
        #(y - y1) = m*(x-x1)
        c = ((m*x) + (m*(-a)) + (y))
        return (c)


    # Returns y-value at the current x for the formula entered
    def formula(self, x):

        self.formulaValidation()

        four = float(self.fourth.get())
        three = float(self.third.get())
        two = float(self.second.get())
        one = float(self.first.get())
        constant = float(self.constant.get())
                      
        #takes the numbers entered and runs them through the function by entering the value of x
        four = four*x**4
        three = three*x**3
        two = two*x**2
        one = one*x

        #add them all together to get the y value at each x value
        c = (four + three + two + one + constant)

        #return the y value
        return (c)

    
    # Prints out work needed to find answer using Newton's Method by hand
    def showWork(self):
        
        #calls formula to set entries of empty values = 0
        self.formulaValidation()

        try:
            work = self.newton(float(self.guess.get()))
        except ValueError:
            print("No root value error")
            return

        if (work == 0):
            print("No root work = 0")
            return

        print("\n\n")
        print("x0 = ", work[0])

        count = 0
        for i in work:
            print("x",count+1, " = ", "x", count, " - ( f(", work[count],") / f'(", work[count], ") ) = ", work[count]) 
            count+=1

            
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


    # Graphs equation user entered
    def graphEquation(self, button):
        
        plt.close("all")
        self.setAxes()
        plt.plot(x,self.formula(x))
        if(button):
            plt.show()

    #functinon for setting axes of the graph about to be displayed
    def setAxes(self):

        #defines axes as the axes of the graph
        axes = plt.gca()

        #makes vertical and horizontal lines so the user has a better understanding of where the x and y axes are
        plt.axhline(y=0, xmin=-5000, xmax=5000, linewidth=2, color = 'k')
        plt.axvline(x=0, ymin=-5000, ymax = 5000, linewidth=2, color='k')

        #sets the limits of the graph for -20,20 in the x and y direction
        axes.set_xlim([-20,20])
        axes.set_ylim([-20, 20])


    
    # If formula input is invalid, or empty, delete and replace it with a default 0
    def formulaValidation(self):

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
        
        self.solveNewton = Button(self, text = "Solve with Newton's Method", command = self.graphTan).grid(row=8, column = 0)
        self.graphFunction = Button(self, text = "Graph Function", command= lambda: self.graphEquation(1) ).grid(row=3, column = 0)
        Label(self, text = "").grid(row=7, column =0)
        Label(self, text = "Root =").grid(row = 9, column = 0)
        
        #creates label for root and a fake entry box (gridding a label) for showing the root
        self.rootLabel = Label(self, anchor = "w", relief = "ridge")
        self.rootLabel.grid(row=9, column = 1, sticky = "we")
        
        self.showWork = Button(self, text = "Show Work", command = self.showWork).grid(row=10, column = 0)
        self.link = Button(self, text = "Explanation of Newton's Method", command = self.exampleLink).grid(row=11, column = 0)

    
#defines the main function to be run
def main():
  gui = Newton_GUI()#creates a new Tk class named app
  gui.mainloop()#run the app as a mainloop so it keeps running after calculations have been done

if __name__ == "__main__":#if the name of the class is main, run the main function
  main()
