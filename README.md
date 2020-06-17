# Rubiks-Cube
The goal of the project is to figure out a reward system to solve the cube in RL. 
So, not much time has been spent in modelling and rendering of the cube. 
For the same reason, the available commands are kept minimal.
 
### Rubik's cube model
* A simple 3D array is used. 
* Rotations are semi-hard coded.
* Currently lower case commands are implemented as the goal of the
project is not to build a simulator.
    * Allowed commands are `["f", "b", "u", "d", "l", "r"]` and their clockwise counterparts
    * `command="f"` would mean rotating front face counter-clockwise
    * `command="b'"` would mean rotating back face clockwise
* Rendering is done in matplotlib. 
* Interaction window is limited to 2 seconds after entering the command 
and after the plot freezes. As long as your mouse is not released the plot doesn't freeze.
* Score is number of edge and corner cubes at teh right position. So max score is 20.
* Edge and corner cubies' score can be changed by `set_weights_edge_corner(self, edge, corner)`
