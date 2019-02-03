import Global
import my_math
from matplotlib import pyplot as plt

def graph_tangent_lines(self):
	#iterate through and graph the tangent lines with the xValue in the list
	for i in self.newtonValues:
		plt.plot( Global.x_range, self.math.tan(i) )
		plt.pause(0.3)


# Graphs equation user entered
def graphEquation(self, button):

	self.is_new_equation()
	plt.close("all")
	self.setAxes()
	plt.plot( Global.x_range, self.math.y_value(Global.x_range) )

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

