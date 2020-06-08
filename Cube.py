import numpy as np
import matplotlib.pyplot as plt
from MiniCube import MiniCube
from mpl_toolkits.mplot3d import Axes3D


def copyCubies(a, b):
	# a = b
	for _a, _b in zip(list(a), list(b)):
		_a.position = _b.position
		_a.global_colors = _b.global_colors
	return


def copyCubies2D(a, b):
	for _a, _b in zip(list(a), list(b)):
		copyCubies(_a, _b)
	return


def rotate_face_cubies(face, axis='X', counterClockWise=True):
	cubies = np.reshape(face, (-1))
	for cubie in cubies:
		# print(cubie.position)
		cubie.rotate(axis, counterClockWise)


class Cube(object):
	
	def __init__(self, size):
		super(Cube, self).__init__()
		self.size = size
		self.cubies = np.empty((3, 3, 3), dtype=object)
		for i in range(3):
			for j in range(3):
				for k in range(3):
					self.cubies[i, j, k] = MiniCube([i, j, k])
	
	def rotate_face(self, cmd="f"):
		ccwise = (cmd.endswith("'") & ((cmd[0] == "f") | (cmd[0] == "r") | (cmd[0] == "u")))
		ccwise = ccwise | ((len(cmd) == 1) & ((cmd == "b") | (cmd == "l") | (cmd == "d")))
		# print(ccwise, cmd)
		ccint = 2 * int(ccwise) - 1  # type: int
		
		pre_positions = self.cubies_positions()
		x = None
		if cmd[0] == "f":
			face_array = self.cubies[:, :, 2]
			# self.cubies[:, :, 2] = self.rotate_2d_array(face_array, ccint)
			copyCubies2D(self.cubies[:, :, 2], self.rotate_2d_array(face_array, ccint))
			rotate_face_cubies(self.cubies[:, :, 2], 'Z', ccwise)
		
		elif cmd[0] == "b":
			face_array = self.cubies[:, :, 0]
			# self.cubies[:, :, 0] = self.rotate_2d_array(face_array, ccint)
			copyCubies2D(self.cubies[:, :, 0], self.rotate_2d_array(face_array, ccint))
			rotate_face_cubies(self.cubies[:, :, 0], 'Z', ccwise)
		
		elif cmd[0] == "r":
			face_array = self.cubies[2, :, :]
			# self.cubies[2, :, :] = self.rotate_2d_array(face_array, ccint)
			copyCubies2D(self.cubies[2, :, :], self.rotate_2d_array(face_array, ccint))
			rotate_face_cubies(self.cubies[2, :, :], 'X', ccwise)
		
		elif cmd[0] == "l":
			face_array = self.cubies[0, :, :]
			# self.cubies[0, :, :] = self.rotate_2d_array(face_array, ccint)
			copyCubies2D(self.cubies[0, :, :], self.rotate_2d_array(face_array, ccint))
			rotate_face_cubies(self.cubies[0, :, :], 'X', ccwise)
		
		elif cmd[0] == "u":
			face_array = self.cubies[:, 2, :]
			# self.cubies[:, 2, :] = self.rotate_2d_array(face_array, ccint)
			copyCubies2D(self.cubies[:, 2, :], self.rotate_2d_array(face_array, ccint))
			rotate_face_cubies(self.cubies[:, 2, :], 'Y', ccwise)
		
		else:
			face_array = self.cubies[:, 0, :]
			# self.cubies[:, 0, :] = self.rotate_2d_array(face_array, ccint)
			copyCubies2D(self.cubies[:, 0, :], self.rotate_2d_array(face_array, ccint))
			rotate_face_cubies(self.cubies[:, 0, :], 'Y', ccwise)
		
		post_positions = self.cubies_positions()
		for pre, post in zip(pre_positions, post_positions):
			if pre!=post:
				print(pre, post)
		self.reset_positions()
		return x
	
	def render(self):
		fig = plt.figure(figsize=(10, 10))
		plt.title("Rubiks Cube")
		ax = fig.add_subplot(111, projection='3d')
		X = np.array([0, 1, 0, 1]).reshape((2, 2))-0.5
		Y = np.array([0, 0, 1, 1]).reshape((2, 2))-0.5
		Z = np.array([0.]*4).reshape((2,2))
		
		cubies = np.reshape(self.cubies, (-1))
		# print(len(cubies))
		for cubie in cubies:
			ax.plot_surface(Z+cubie.position[0]+0.5, X+cubie.position[1], Y+cubie.position[2], color=cubie.global_colors[0])  #  +X
			ax.plot_surface(Z+cubie.position[0]-0.5, X+cubie.position[1], Y+cubie.position[2], color=cubie.global_colors[1])  #  -X
			ax.plot_surface(X+cubie.position[0], Z+cubie.position[1]+0.5, Y+cubie.position[2], color=cubie.global_colors[2])  #  +Y
			ax.plot_surface(X+cubie.position[0], Z+cubie.position[1]-0.5, Y+cubie.position[2], color=cubie.global_colors[3])  #  -Y
			ax.plot_surface(X+cubie.position[0], Y+cubie.position[1], Z+cubie.position[2]+0.5, color=cubie.global_colors[4])  #  +Z
			ax.plot_surface(X+cubie.position[0], Y+cubie.position[1], Z+cubie.position[2]-0.5, color=cubie.global_colors[5])  #  -Z
		
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Z')
		plt.show()
		return
	
	def rotate_2d_array(self, face_array, ccint):
		print(ccint)
		cubies = [MiniCube([0, 0, 0]) for _ in range(self.size*self.size)]
		newcubes = np.array(cubies)
		newcubes = np.resize(newcubes, (self.size, self.size))
		
		# newcubes[::-1 * ccint, 2] = face_array[0, :]
		# newcubes[2, ::1 * ccint] = face_array[:, 2]
		# newcubes[::-1 * ccint, 0] = face_array[2, :]
		# newcubes[0, ::1 * ccint] = face_array[:, 0]
		# newcubes[1:2, 1] = face_array[1:2, 1]
		
		if ccint>0:
			copyCubies(newcubes[::-1, 0], face_array[0, :])
			copyCubies(newcubes[::-1, 2], face_array[2, :])
			copyCubies(newcubes[2, :], face_array[:, 0])
			copyCubies(newcubes[0, :], face_array[:, 2])
			copyCubies(newcubes[1:2, 1], face_array[1:2, 1])
		else:
			copyCubies(newcubes[:, 2], face_array[0, :])
			copyCubies(newcubes[:, 0], face_array[2, :])
			copyCubies(newcubes[0, ::-1], face_array[:, 0])
			copyCubies(newcubes[2, ::-1], face_array[:, 2])
			copyCubies(newcubes[1:2, 1], face_array[1:2, 1])
			
		# copyCubies(newcubes[::-ccint, 2], face_array[0, :])
		# copyCubies(newcubes[2, ::ccint], face_array[:, 2])
		# copyCubies(newcubes[::-ccint, 0], face_array[2, :])
		# copyCubies(newcubes[0, ::ccint], face_array[:, 0])
		# copyCubies(newcubes[1:2, 1], face_array[1:2, 1])
		# print(newcubes)
		return newcubes
	
	def reset(self):
		self.reset_positions()
		for cubie in np.reshape(self.cubies, (-1)):
			cubie.reset_colors()
		return
	
	def cubies_positions(self, display=False):
		cubies = np.reshape(self.cubies, (-1))
		positions = [cubie.position for cubie in cubies]
		if display:
			for i, cubie in enumerate(cubies):
				print(i, cubie.position)
		return positions
	
	def reset_positions(self):
		for i in range(3):
			for j in range(3):
				for k in range(3):
					self.cubies[i, j, k].position = [i, j, k]
		return
