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
		
		self.render_first = True
		self.edge_score = 1
		self.corner_score = 1
		self.render_pause_time = 0.01
		self.max_score = 5000.
		self.score = self.get_cube_score()
		
	
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
		self.score = self.get_cube_score()
		# print("CUBE ROTATED: ", command, self.score)
		return
	
	def render(self):
		if self.render_first:
			plt.ion()
			plt.show()
			self.render_first = False
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
		plt.pause(self.render_pause_time)
		return
	
	def set_render_time(self, time):
		self.render_pause_time = time
	
	def rotate_edge(self, locs, counter_clock=True):
		data = []
		for loc in locs:
			data += [self.cube[loc[0], loc[1], loc[2]]]
		ccint = 2 * int(counter_clock) - 1
		for i, loc in enumerate(locs):
			self.cube[loc[0], loc[1], loc[2]] = data[(i + 2 * ccint) % 8]
		return
	
	def get_face_colors(self, axis="x", position=0):
		color_indexes = {"x2": 0,
		                 "x0": 1,
		                 "y2": 2,
		                 "y0": 3,
		                 "z2": 4,
		                 "z0": 5}
		if axis == "x":
			cubies = self.cube[position, :, :]
		elif axis == "y":
			cubies = self.cube[:, position, :]
		else:
			cubies = self.cube[:, :, position]
		
		color_code = {'g': 0, 'b': 1,
		              'white': 2, 'yellow': 3,
		              'orange': 4, 'r': 5}
		_colors = [self.cubies[cubie].global_colors[color_indexes[axis + str(position)]] for cubie in
		           cubies.reshape((-1))]
		colors = [color_code[cccode] for cccode in _colors]
		
		return colors
	
	def get_state(self):
		f = self.get_face_colors(axis="y", position=0)
		b = self.get_face_colors(axis="y", position=2)
		l = self.get_face_colors(axis="x", position=0)
		r = self.get_face_colors(axis="x", position=2)
		u = self.get_face_colors(axis="z", position=2)
		d = self.get_face_colors(axis="z", position=0)
		return np.array(f + b + r + l + u + d)
	
	def set_weights_edge_corner(self, edge, corner):
		self.edge_score = 2 * edge / (edge + corner)
		self.corner_score = 2 * corner / (edge + corner)
		return
	
	def get_cube_score(self):
		score = 0.
		for val in range(27):
			i = val % 3
			j = (val // 3) % 3
			k = (val // 9)
			# print([i,j,k], self.get_cubie_score(coords=[i, j, k]))
			score += self.get_cubie_score(coords=[i, j, k])
		if score == 20.:
			score = self.max_score
		return score
	
	def get_cubie_score(self, coords):
		
		if sum(np.array(coords) == 1) == 0:
			# Corner Cubie
			return int(self.is_cubie_correct(coords)) * self.corner_score
		
		elif sum(np.array(coords) == 1) == 1:
			# Edge Cubie
			return int(self.is_cubie_correct(coords)) * self.edge_score
		
		elif sum(np.array(coords) == 1) == 2:
			# Face Cubie
			return 0.
		else:
			# Center Cubie
			return 0.
	
	def get_cubie(self, coords):
		return self.cubies[self.cube[coords[2], coords[1], coords[2]]]
	
	def get_visible_colors(self, coords):
		invisible = np.array(coords) == 1
		color_coords = (1 - np.array(coords) // 2) + np.array([0, 2, 4])
		colors = []
		for iv, color in zip(invisible, [self.get_cubie(coords).global_colors[i] for i in color_coords]):
			if iv:
				colors += [None]
			else:
				colors += [color]
		return colors
	
	def is_cubie_correct(self, coords):
		face_colors = []
		for i, coord in enumerate(coords):
			face_coords = [1, 1, 1]
			if coord == 1:
				face_colors += [None]
			else:
				face_coords[i] = coord
				face_colors += [color for color in self.get_visible_colors(face_coords) if color is not None]
		# print("FACES: ", face_colors)
		# print("CUBIE: ", self.get_visible_colors(coords))
		
		return face_colors == self.get_visible_colors(coords)
	
	def print_correct_cubies(self):
		for val in range(27):
			i = val % 3
			j = (val // 3) % 3
			k = (val // 9)
			if sum(np.array([i, j, k]) == 1) < 2:
				if self.is_cubie_correct([i, j, k]):
					print([i, j, k])
		return
	
	def reset(self):
		n = 3
		self.size = n
		self.cubies = [Cubie([0, 0, 0]) for _ in range(n ** 3)]
		self.cube = np.zeros((n, n, n), dtype=int)
		for i in range(n):
			for j in range(n):
				for k in range(n):
					self.cube[i, j, k] = i + j * n + k * (n ** 2)
		self.score = self.get_cube_score()
		return
	
	def scramble(self):
		self.reset()
		cmds_length = np.random.randint(50, 100, 1)[0]
		base_cmds = ["l", "r", "u", "d", "f", "b"]
		cmds = []
		cmd_idxs = np.random.uniform(0, 6, cmds_length).astype(np.int)
		cc_idxs = np.random.uniform(0, 2, cmds_length).astype(np.int)
		for cmd_idx, cc_idx in zip(cmd_idxs, cc_idxs):
			cmd = base_cmds[cmd_idx]
			if cc_idx == 1:
				cmd += "'"
			self.rotate_face(command=cmd)
			cmds += [cmd]
		return cmds
	
	def is_solved(self):
		return self.score == self.max_score
