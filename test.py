from Rubix.cube import Cube

myCube = Cube()
cmd = "x"
while cmd:
	myCube.rotate_face(cmd)
	myCube.render()
	cmd = input("Enter the command: ")

print("Exiting the Rubik's cube simulation")