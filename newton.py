from tkinter import *
import webbrowser
import gui
import my_math
import my_graph
import matplotlib


# Inherit from Tkinter to make basic GUI
class Newton_GUI(Tk):
    
    # import methods
    from gui import exampleLink, addGUI, addTitle, formulaValidation, getAccuracy
    from gui import validate_guess, is_new_equation
    from my_graph import graph_tangent_lines, graphEquation, setAxes

    def __init__(self):
        Tk.__init__(self)
        
        # Window title
        self.title("Newton's Method")

        # GUI title
        self.addTitle("Newton's Method")
        self.addGUI()
        
        # Member variables
        self.math = my_math.Newton_Math()
        self.newtonValues = []
        # set initial guess to garbage value user wont enter
        self.currentGuess = -99994999


    # Graphs tangent lines by using Newton's method
    def solve_with_newton(self):

        self.graphEquation(0)
        self.formulaValidation()
        
        valid, guess_is_same, guess = self.validate_guess()

        if(not valid):
            return

        # If guess is the same, then re-use our data from Newton method
        elif(guess_is_same):
            self.graph_tangent_lines()
            return

        # Guess is valid, but is not the same
        else:

            del self.newtonValues[:]            
            self.newton(guess)

            # If newton succeeded
            if (self.newtonValues):
                self.graph_tangent_lines()

                
    # Executes Newton's Method
    # Returns an array of values for Newton's method calculations
    # Starts computation with initial x value of the user's guess of the root
    # Returns 0 if failed, 1 if succeeded     
    def newton(self, current_x):

        self.root = False
        
        if(float(self.fourth.get()) and float(self.third.get()) and float(self.second.get()) and float(self.first.get()) and float(self.constant.get()) == 0):
            return 0

        accuracy = self.getAccuracy()
        iterations = 0
        while (self.root == False):
        
            x1 = current_x

            # If derivative is 0, tangent line will never hit x axis, no solution
            try:
                # update our current_x according to Newton's method formula
                current_x = (current_x - (self.math.formula(current_x)/(self.math.derive(current_x))))
                
            except ZeroDivisionError:
                self.rootLabel["text"] = "No root"
                del self.newtonValues[:]
                return 0
            
            self.newtonValues.insert(iterations, current_x) 
            iterations+=1

            # After 100 iterations, it's an infinite loop with no answer/root
            if(iterations>100):
                print("iterations!")
                self.rootLabel["text"] = "No root"
                del self.newtonValues[:]
                return 0
    
            # If we get the same value for our answer as the last iteration,
            # Then Newton's Method has been satisfied and we have our answer
            if (accuracy%(current_x) == accuracy%(x1)):
                print(iterations)
                self.root = True
                self.rootLabel["text"] = accuracy % current_x
                return 1


    # Prints out work needed to find answer using Newton's Method by hand
    def showWork(self):
        
        #If there is a new equation
        if(self.is_new_equation()):
            
            valid, guess_is_same, guess = self.validate_guess()

            if(valid):
                
                del self.newtonValues[:]
                
                if(self.newton(guess)):
                    self.print_work()
                    
            else:
                return
            
        # Not a new equation
        else:
            valid, guess_is_same, guess = self.validate_guess()
            # if it's the same guess as last time
            if(guess_is_same):
                plt.close("all")
                self.print_work()
                
            else:
                del self.newtonValues[:]
                if(self.newton(guess)):
                    self.print_work()


    # Prints values stored by newton()
    def print_work(self):
            
            print("\n\n")
            print("x0 = ", self.newtonValues[0])

            count = 0
            for i in self.newtonValues:
                print("x",count+1, " = ", "x", count, " - ( f(", self.newtonValues[count],") / f'(", self.newtonValues[count], ") ) = ", self.newtonValues[count]) 
                count+=1
