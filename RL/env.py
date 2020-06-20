from Rubix.cube import Cube


class Env(object):
	def __init__(self, penalty=0.1):
		self.cube = Cube()
		self.actions_so_far = []
		self.rewards_so_far = []
		self.action_space = ["f", "b", "u", "d", "r", "l",
		                     "f'", "b'", "u'", "d'", "r'", "l'"]
		self.penalty = penalty
		_ = self.cube.scramble()
	
	def reset(self):
		self.cube.reset()
		_ = self.cube.scramble()
		self.actions_so_far = []
		self.rewards_so_far = []
	
	def get_state(self):
		return self.cube.get_state()
	
	def step(self, action):
		state = self.cube.get_state()
		score = self.cube.score
		self.cube.rotate_face(self.action_space[action])
		self.actions_so_far += [self.action_space[action]]
		reward = self.cube.score - score - self.penalty
		self.rewards_so_far += [reward]
		return state, action, reward, self.cube.get_state()
