from Rubix import Cube
import time
myCube = Cube()
myCube.set_render_time(2)
cmd = "x"
while cmd:
	myCube.rotate_face(cmd)
	if cmd[-1] is not 's':
		# myCube.print_correct_cubies()
		myCube.render()
		
	print("SCORE: ", myCube.get_cube_score())
	cmd = input("Enter the command: ")

print("Exited the simulation")