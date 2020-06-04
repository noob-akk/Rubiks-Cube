import numpy as np
import os
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class MiniCube(object):
	def __init__(self, position):
		# 0 +X, 1 -X
		# 2 +Y, 3 -Y
		# 4 +Z, 5 -Z
		self.global_colors = ['g', 'b', 'white', 'yellow', 'orange', 'r']

		#global position of center
		self.position = [None]*3
		for i,p in enumerate(position):
			self.position[i] = p

		# #X->X' angle in ccwise direction
		# self.orientation = [0]*3


	def rotate(self, axis='X', counterclockwise=True):
		'''
		changes colors of all its faces acc to the roattion
		'''
		ncolors = [None]*6
		for i in range(6):
			ncolors[i] = self.global_colors[i]

		if axis=='X':
			if counterclockwise:
				ncolors[2] = self.global_colors[5]
				ncolors[3] = self.global_colors[4]
				ncolors[4] = self.global_colors[2]
				ncolors[5] = self.global_colors[3]
			else:
				ncolors[2] = self.global_colors[4]
				ncolors[3] = self.global_colors[5]
				ncolors[4] = self.global_colors[3]
				ncolors[5] = self.global_colors[2]
		elif axis=='Y':
			if counterclockwise:
				ncolors[0] = self.global_colors[4]
				ncolors[1] = self.global_colors[5]
				ncolors[4] = self.global_colors[1]
				ncolors[5] = self.global_colors[0]
			else:
				ncolors[0] = self.global_colors[5]
				ncolors[1] = self.global_colors[4]
				ncolors[4] = self.global_colors[0]
				ncolors[5] = self.global_colors[1]
		else:
			if counterclockwise:
				ncolors[0] = self.global_colors[3]
				ncolors[1] = self.global_colors[2]
				ncolors[2] = self.global_colors[0]
				ncolors[3] = self.global_colors[1]
			else:
				ncolors[0] = self.global_colors[2]
				ncolors[1] = self.global_colors[3]
				ncolors[2] = self.global_colors[1]
				ncolors[3] = self.global_colors[0]

		# flag = 2*int(counterclockwise)-1
		# coords = {'X':0, 'Y':1, 'Z':2}
		# for ax in range(3):
		# 	self.orientation[ax] += (flag*90+360)
		# self.orientation[coords[axis]] -= flag*90
		# for ax in range(3):
			# self.orientation[ax] %= 360

		for i in range(6):
			self.global_colors[i] = ncolors[i]

		return

	def get_colors(self):
		'''
		Return colors of the minicube w.r.t the global axes
		'''
		return self.global_colors


	def render(self, title="Title"):
		axes = [2,1,4,0,3,5]
		print(" %s \n%s%s%s\n %s \n %s \n"%(self.global_colors[axes[0]], 
			self.global_colors[axes[1]], 
			self.global_colors[axes[2]], 
			self.global_colors[axes[3]], 
			self.global_colors[axes[4]], 
			self.global_colors[axes[5]]))
		points = np.array([[-1, -1, -1],
                      [1, -1, -1 ],
                      [1, 1, -1],
                      [-1, 1, -1],
                      [-1, -1, 1],
                      [1, -1, 1 ],
                      [1, 1, 1],
                      [-1, 1, 1]])

		fig = plt.figure()
		plt.title(title)
		ax = fig.add_subplot(111, projection='3d')
		r = [-1,1]
		X, Y = np.meshgrid(r, r)
		one = np.ones(4).reshape(2, 2)
		ax.plot_surface(X,Y, one, color=self.global_colors[0])
		ax.plot_surface(X,Y,-one, color=self.global_colors[1])
		ax.plot_surface(X,-one,Y, color=self.global_colors[3])
		ax.plot_surface(X, one,Y, color=self.global_colors[2])
		ax.plot_surface( one,X,Y, color=self.global_colors[4])
		ax.plot_surface(-one,X,Y, color=self.global_colors[5])
		# ax.scatter3D(points[:, 0], points[:, 1], points[:, 2])
		ax.set_xlabel('Z')
		ax.set_ylabel('Y')
		ax.set_zlabel('X')
		plt.show()
		return

	def reset_colors(self):
		self.global_colors = ['g', 'b', 'white', 'yellow', 'orange', 'r']
		return


minicube = MiniCube([0,0,0])
minicube.render("Original")

axes = ['X', 'Y', 'Z']
for i in range(6):
	title = ""
	axis = axes[i//2]
	ccwise = i%2
	minicube.reset_colors()
	print(axis, "Fresh")
	if ccwise:
		title = "%d: %s %s"%(i, axis, "counterclockwise")
	else:
		title = "%d: %s %s"%(i, axis, "clockwise")
	minicube.rotate(axis, counterclockwise=ccwise)
	minicube.render(title)


# class Cube(object):
# 	"""docstring for Cube"""
# 	def __init__(self, size):
# 		super(Cube, self).__init__()
# 		self.size = size
# 		self.

# 	def 
		