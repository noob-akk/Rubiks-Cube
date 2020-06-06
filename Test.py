from MiniCube import MiniCube
from Cube import Cube

myCube3 = Cube(3)
cmds = "f,r,u,b',l',d'"

for cmd in cmds.split(','):
	myCube3.rotate_face(cmd=cmd)

myCube3.render()