import numpy as np
import matplotlib.pyplot as plt
from MiniCube import MiniCube


def copyCubies(a, b):
	for _a, _b in zip(list(a), list(b)):
		_a.position = _b.position
		_a.global_colors = _b.global_colors
	return


def rotate_face_cubies(face, axis='X', counterClockWise=True):
	cubies = np.reshape(face, (-1))
	for cubie in cubies:
		print(cubie.position)
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
	
	def face_rotate(self, face="f"):
		ccwise = (face.endswith("'") & ((face[0] == "f") | (face[0] == "r") | (face[0] == "u")))
		ccwise = ccwise | ((len(face) == 1) & ((face == "b") | (face == "l") | (face == "d")))
		print(ccwise, )
		ccint = 2 * int(ccwise) - 1
		
		x = None
		if face[0] == "f":
			face_array = self.cubies[:, :, 2]
			self.cubies[:, :, 2] = self.rotate_2d_array(face_array, ccint)
			rotate_face_cubies(self.cubies[:, :, 2], 'Z', ccwise)
		
		elif face[0] == "b":
			face_array = self.cubies[:, :, 0]
			x = self.rotate_2d_array(face_array, ccint)
			self.cubies[:, :, 0] = self.rotate_2d_array(face_array, ccint)
			rotate_face_cubies(self.cubies[:, :, 0], 'Z', ccwise)
		
		elif face[0] == "r":
			face_array = self.cubies[2, :, :]
			self.cubies[2, :, :] = self.rotate_2d_array(face_array, ccint)
			rotate_face_cubies(self.cubies[2, :, :], 'X', ccwise)
		
		elif face[0] == "l":
			face_array = self.cubies[0, :, :]
			self.cubies[0, :, :] = self.rotate_2d_array(face_array, ccint)
			rotate_face_cubies(self.cubies[0, :, :], 'X', ccwise)
		
		elif face[0] == "u":
			face_array = self.cubies[:, 2, :]
			self.cubies[:, 2, :] = self.rotate_2d_array(face_array, ccint)
			rotate_face_cubies(self.cubies[:, 2, :], 'Y', ccwise)
		
		else:
			face_array = self.cubies[:, 0, :]
			self.cubies[:, 0, :] = self.rotate_2d_array(face_array, ccint)
			rotate_face_cubies(self.cubies[:, 0, :], 'Y', ccwise)
		
		for i in range(3):
			for j in range(3):
				for k in range(3):
					self.cubies[i, j, k].position = [i, j, k]
		return x
	
	def render(self):
		fig = plt.figure(figsize=(10, 10))
		plt.title("Rubiks Cube")
		ax = fig.add_subplot(111, projection='3d')
		X = np.array([0,1,0,1]).reshape((2,2))-0.5
		Y = np.array([0,0,1,1]).reshape((2,2))-0.5
		Z = np.array([0.]*4).reshape((2,2))
		
		cubies = np.reshape(self.cubies, (-1))
		print(len(cubies))
		for cubie in cubies:
			ax.plot_surface(Z+cubie.position[0]+0.5, X+cubie.position[1], Y+cubie.position[2], color=cubie.global_colors[0]) # +X
			ax.plot_surface(Z+cubie.position[0]-0.5, X+cubie.position[1], Y+cubie.position[2], color=cubie.global_colors[1]) # -X
			ax.plot_surface(X+cubie.position[0], Z+cubie.position[1]+0.5, Y+cubie.position[2], color=cubie.global_colors[2]) # +Y
			ax.plot_surface(X+cubie.position[0], Z+cubie.position[1]-0.5, Y+cubie.position[2], color=cubie.global_colors[3]) # -Y
			ax.plot_surface(X+cubie.position[0], Y+cubie.position[1], Z+cubie.position[2]+0.5, color=cubie.global_colors[4]) # +Z
			ax.plot_surface(X+cubie.position[0], Y+cubie.position[1], Z+cubie.position[2]-0.5, color=cubie.global_colors[5]) # -Z
		
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Z')
		plt.show()
		return
	
	def rotate_2d_array(self, face_array, ccint):
		cubies = [MiniCube([0, 0, 0]) for _ in range(self.size*self.size)]
		newcubes = np.array(cubies)
		newcubes = np.resize(newcubes, (self.size, self.size))
		
		copyCubies(newcubes[::-1 * ccint, 2], face_array[0, :])
		copyCubies(newcubes[2, ::1 * ccint], face_array[:, 2])
		copyCubies(newcubes[::-1 * ccint, 0], face_array[2, :])
		copyCubies(newcubes[0, ::1 * ccint], face_array[:, 0])
		copyCubies(newcubes[1:2, 1], face_array[1:2, 1])
		# print(newcubes)
		return newcubes
