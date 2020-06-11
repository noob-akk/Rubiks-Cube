import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Cubie(object):
	
	def __init__(self, position):
		# 0 +X, 1 -X
		# 2 +Y, 3 -Y
		# 4 +Z, 5 -Z
		self.global_colors = ['g', 'b', 'white', 'yellow', 'orange', 'r']
		
		# global position of center
		self.position = [-10] * 3
		for i, p in enumerate(position):
			self.position[i] = p
	
	# #X->X' angle in ccwise direction
	# self.orientation = [0]*3
	
	def rotate(self, axis='X', counterClockWise=True):
		"""
		changes colors of all its faces acc to the roattion
		"""
		axis = axis.lower()
		ncolors = [None] * 6
		for i in range(6):
			ncolors[i] = self.global_colors[i]
		
		if axis == 'x':
			if counterClockWise:
				ncolors[2] = self.global_colors[5]
				ncolors[3] = self.global_colors[4]
				ncolors[4] = self.global_colors[2]
				ncolors[5] = self.global_colors[3]
			else:
				ncolors[2] = self.global_colors[4]
				ncolors[3] = self.global_colors[5]
				ncolors[4] = self.global_colors[3]
				ncolors[5] = self.global_colors[2]
		elif axis == 'y':
			if counterClockWise:
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
			if counterClockWise:
				ncolors[0] = self.global_colors[3]
				ncolors[1] = self.global_colors[2]
				ncolors[2] = self.global_colors[0]
				ncolors[3] = self.global_colors[1]
			else:
				ncolors[0] = self.global_colors[2]
				ncolors[1] = self.global_colors[3]
				ncolors[2] = self.global_colors[1]
				ncolors[3] = self.global_colors[0]
		
		for i in range(6):
			self.global_colors[i] = ncolors[i]
		
		return
	
	def get_colors(self):
		"""
		Return colors of the minicube w.r.t the global axes
		"""
		return self.global_colors
	
	def render(self, title="Cubie Render", display=False):
		axes = [2, 1, 4, 0, 3, 5]
		print(" %s \n%s%s%s\n %s \n %s \n" % (self.global_colors[axes[0]][0], self.global_colors[axes[1]][0], self.global_colors[axes[2]][0], self.global_colors[axes[3]][0], self.global_colors[axes[4]][0],  self.global_colors[axes[5]][0]))
		if display:
			fig = plt.figure(figsize=(3, 3))
			plt.title("Rubiks Cube")
			ax = fig.add_subplot(111, projection='3d')
			X = np.array([0, 1, 0, 1]).reshape((2, 2)) - 0.5
			Y = np.array([0, 0, 1, 1]).reshape((2, 2)) - 0.5
			Z = np.array([0.] * 4).reshape((2, 2))
			
			ax.plot_surface(Z + self.position[0] + 0.5, X + self.position[1], Y + self.position[2], color=self.global_colors[0], alpha=1)  # +X
			ax.plot_surface(Z + self.position[0] - 0.5, X + self.position[1], Y + self.position[2], color=self.global_colors[1], alpha=1)  # -X
			ax.plot_surface(X + self.position[0], Z + self.position[1] + 0.5, Y + self.position[2], color=self.global_colors[2], alpha=1)  # +Y
			ax.plot_surface(X + self.position[0], Z + self.position[1] - 0.5, Y + self.position[2], color=self.global_colors[3], alpha=1)  # -Y
			ax.plot_surface(X + self.position[0], Y + self.position[1], Z + self.position[2] + 0.5, color=self.global_colors[4], alpha=1)  # +Z
			ax.plot_surface(X + self.position[0], Y + self.position[1], Z + self.position[2] - 0.5, color=self.global_colors[5], alpha=1)  # -Z
			plt.show()
		return
	
	def reset_colors(self):
		self.global_colors = ['g', 'b', 'white', 'yellow', 'orange', 'r']
		return

#
# cubie = MiniCube([0, 0, 0])
# cubie.render()
# cubie.rotate()
# cubie.render()