import numpy as np
import matplotlib.pyplot as plt

class MiniCube(object):
	
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
		ncolors = [None] * 6
		for i in range(6):
			ncolors[i] = self.global_colors[i]
		
		if axis == 'X':
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
		elif axis == 'Y':
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
		"""
		Return colors of the minicube w.r.t the global axes
		"""
		return self.global_colors
	
	def render(self, title="Title"):
		axes = [2, 1, 4, 0, 3, 5]
		print(" %s \n%s%s%s\n %s \n %s \n" % (self.global_colors[axes[0]][0],
		                                      self.global_colors[axes[1]][0],
		                                      self.global_colors[axes[2]][0],
		                                      self.global_colors[axes[3]][0],
		                                      self.global_colors[axes[4]][0],
		                                      self.global_colors[axes[5]][0]))
		fig = plt.figure(figsize=(10, 10))
		plt.title("Rubiks Cube")
		ax = fig.add_subplot(111, projection='3d')
		X = np.array([0, 1, 0, 1]).reshape((2, 2)) - 0.5
		Y = np.array([0, 0, 1, 1]).reshape((2, 2)) - 0.5
		Z = np.array([0.] * 4).reshape((2, 2))
		
		ax.plot_surface(Z + self.position[0] + 0.5, X + self.position[1], Y + self.position[2],
		                color=self.global_colors[0], alpha=1)  # +X
		ax.plot_surface(Z + self.position[0] - 0.5, X + self.position[1], Y + self.position[2],
		                color=self.global_colors[1], alpha=1)  # -X
		ax.plot_surface(X + self.position[0], Z + self.position[1] + 0.5, Y + self.position[2],
		                color=self.global_colors[2], alpha=1)  # +Y
		ax.plot_surface(X + self.position[0], Z + self.position[1] - 0.5, Y + self.position[2],
		                color=self.global_colors[3], alpha=1)  # -Y
		ax.plot_surface(X + self.position[0], Y + self.position[1], Z + self.position[2] + 0.5,
		                color=self.global_colors[4], alpha=1)  # +Z
		ax.plot_surface(X + self.position[0], Y + self.position[1], Z + self.position[2] - 0.5,
		                color=self.global_colors[5], alpha=1)  # -Z
		return
	
	def reset_colors(self):
		self.global_colors = ['g', 'b', 'white', 'yellow', 'orange', 'r']
		return
