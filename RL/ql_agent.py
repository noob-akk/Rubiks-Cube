import numpy as np
from keras.models import Sequential, save_model, load_model
from keras.layers import Dense
import tensorflow as tf

gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.5)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))


def greedy_action(values):
	# print("greedy action taken")
	return np.argmax(values)


def random_action():
	# print("random action taken")
	return np.random.randint(0, 12, 1)[0]


class QLAgent(object):
	def __init__(self):
		self.n_actions = 12
		self.state_size = 54
		self.qnn = None
		self.load()
	
	def q_val_model(self):
		model = Sequential()
		model.add(Dense(self.state_size * 3 // 2, input_shape=(self.state_size,), activation='relu'))
		model.add(Dense(self.state_size * 3, activation='relu'))
		model.add(Dense(self.state_size * 3 // 2, activation='relu'))
		model.add(Dense(self.n_actions, activation='linear'))
		model.compile("adam", loss="mae")
		model.summary()
		return model
	
	def save(self):
		save_model(self.qnn, "./models/q_learn_model.hdf5")
		return
	
	def load(self):
		try:
			self.qnn = load_model("./models/q_learn_model.hdf5")
		except:
			self.qnn = self.q_val_model()
		return
	
	def egreedy_action(self, state, epsilon=0.5):
		coin = np.random.uniform(0, 1, 1)[0]
		values = self.get_action_values(state)
		# print(values.shape)
		if coin < epsilon:
			return values, random_action()
		else:
			return values, greedy_action(values)
	
	def get_action_values(self, state):
		values = self.qnn.predict(state.reshape((1, -1)))[0]
		return values
	
	def train(self, X, Y):
		self.qnn.fit(X, Y, shuffle=True, verbose=0)
		self.save()
		return
