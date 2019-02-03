import Global
import my_graph

class Newton_Math:

	def __init__(self):
		self.equation = []

	# Function for finding the value of the derivative of a function at any given x point
	def derive(self, x):

		# Set h to a value really close to 0 to simulate the limit as h goes to 0
		h=0.00000000000001

		# Use derivative identity
		derivative = (self.formula(x + h) - self.formula(x)) / h

		return derivative


	# Returns y-value at the current x for the formula entered
	def formula(self, x):

		#takes the numbers entered and runs them through the function by entering the value of x
		four = self.equation[0]*x**4
		three = self.equation[1]*x**3
		two = self.equation[2]*x**2
		one = self.equation[3]*x
		constant = self.equation[4]

		#add them all together to get the y value at each x value
		c = (four + three + two + one + constant)

	   # print(c)
		#return the y value
		return (c)


	# Finds the equation of the tangent line to the curve at any given x point
	def tan(self, x):
		print("xvalues: ", x)
		m = self.derive(x)
		print("m: ", m)
		y = self.formula(x)
		print("y: ", y)

		#point slope formula, a represents the x value at any given point, and I added the y to this side from the original point slope form
		#(y - y1) = m*(x-x1)
		c = ((m*Global.x_range) + (m*(-x)) + (y))
		print(c)
		return (c)

	def setEquation(self, e):
		self.equation = e

	def getEquation(self):
		return self.equation

