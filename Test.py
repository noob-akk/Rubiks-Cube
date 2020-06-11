from Cubie import Cubie
from Cube import Cube

myCube3 = Cube(3)
cmds = "f,u"

for cmd in cmds.split(','):
	myCube3.rotate_face(cmd=cmd)

myCube3.render()