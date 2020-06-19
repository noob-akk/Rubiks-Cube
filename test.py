from Rubix.cube import Cube

myCube = Cube()
myCube.set_render_time(1)

cmds = ['b', 'b', 'l', "u'", 'b', "f'", "b'", 'u', "d'", "d'",
        'f', 'b', 'l', "u'", "l'", 'u', 'f', 'f', 'u', "d'"]

print(myCube.get_cube_score())
for cmd in cmds:
	myCube.rotate_face(cmd)
	print(myCube.get_cube_score())

# myCube.render()
#
# for cmd in cmds[::-1]:
# 	if cmd.endswith("'"):
# 		cmd = cmd[:1]
# 	else:
# 		cmd += "'"
# 	myCube.rotate_face(cmd)
# 	print(myCube.get_cube_score())
# 	myCube.render()

