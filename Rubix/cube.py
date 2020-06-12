import numpy as np
import matplotlib.pyplot as plt
from .cubie import Cubie


class Cube(object):
	"""
	+X Right
	-X Left
	+Y Top
	-Y Bottom
	+Z Front
	-Z Back
	"""
	
	def __init__(self):
		n = 3
		self.size = n
		self.cubies = [Cubie([0, 0, 0]) for _ in range(n ** 3)]
		self.cube = np.zeros((n, n, n), dtype=int)
		for i in range(n):
			for j in range(n):
				for k in range(n):
					self.cube[i, j, k] = i + j * n + k * (n ** 2)
		self.cube_fig = plt.figure(figsize=(10, 10))
		self.cube_ax = self.cube_fig.add_subplot(111, projection='3d')
		plt.ion()
		plt.show()
		
		
	def rotate_layer(self, position=0, axis='z', counter_clock=True):
		axis = axis.lower()
		if axis == 'x':
			locs = [[position, 0, 2], [position, 1, 2], [position, 2, 2],
			        [position, 2, 1], [position, 2, 0], [position, 1, 0],
			        [position, 0, 0], [position, 0, 1]]
			self.rotate_edge(locs, counter_clock)
			for cubie in [self.cubies[idx] for idx in list(self.cube[position, :, :].reshape((-1)))]:
				cubie.rotate(axis, counter_clock)
		
		elif axis == 'y':
			locs = [[0, position, 0], [1, position, 0], [2, position, 0],
			        [2, position, 1], [2, position, 2], [1, position, 2],
			        [0, position, 2], [0, position, 1]]
			self.rotate_edge(locs, counter_clock)
			for cubie in [self.cubies[idx] for idx in list(self.cube[:, position, :].reshape((-1)))]:
				cubie.rotate(axis, counter_clock)
		else:
			locs = [[0, 2, position], [1, 2, position], [2, 2, position],
			        [2, 1, position], [2, 0, position], [1, 0, position],
			        [0, 0, position], [0, 1, position]]
			self.rotate_edge(locs, counter_clock)
			for cubie in [self.cubies[idx] for idx in list(self.cube[:, :, position].reshape((-1)))]:
				cubie.rotate(axis, counter_clock)
		return
	
	def rotate_face(self, command="f"):
		command = command.lower()
		ccwise = int(command.endswith("'"))
		cmds_decoder = {"f": "y00",
		                "b": "y21",
		                "r": "x21",
		                "l": "x00",
		                "u": "z21",
		                "d": "z00"}
		if command[0] in cmds_decoder.keys():
			cmd_decoded = cmds_decoder[command[0]]
			ccwise += int(cmd_decoded[-1])
			ccwise %= 2
			self.rotate_layer(axis=cmd_decoded[0], position=int(cmd_decoded[1]), counter_clock=bool(ccwise))
		return
	
	def render(self):
		ax = self.cube_ax
		X = np.array([0, 1, 0, 1]).reshape((2, 2)) - 0.5
		Y = np.array([0, 0, 1, 1]).reshape((2, 2)) - 0.5
		Z = np.array([0.] * 4).reshape((2, 2))
		
		for i in range(self.size):
			for j in range(self.size):
				for k in range(self.size):
					idx = self.cube[i, j, k]
					cubie = self.cubies[idx]
					ax.plot_surface(Z + i + 0.5, X + j, Y + k,
					                color=cubie.global_colors[0])  # +X
					ax.plot_surface(Z + i - 0.5, X + j, Y + k,
					                color=cubie.global_colors[1])  # -X
					ax.plot_surface(X + i, Z + j + 0.5, Y + k,
					                color=cubie.global_colors[2])  # +Y
					ax.plot_surface(X + i, Z + j - 0.5, Y + k,
					                color=cubie.global_colors[3])  # -Y
					ax.plot_surface(X + i, Y + j, Z + k + 0.5,
					                color=cubie.global_colors[4])  # +Z
					ax.plot_surface(X + i, Y + j, Z + k - 0.5,
					                color=cubie.global_colors[5])  # -Z
		
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Z')
		plt.draw()
		plt.pause(2)
		# print("here")
		# plt.ion()
		# plt.show(ax)
		return
	
	def rotate_edge(self, locs, counter_clock=True):
		data = []
		for loc in locs:
			data += [self.cube[loc[0], loc[1], loc[2]]]
		ccint = 2 * int(counter_clock) - 1
		for i, loc in enumerate(locs):
			self.cube[loc[0], loc[1], loc[2]] = data[(i + 2 * ccint) % 8]
		return



