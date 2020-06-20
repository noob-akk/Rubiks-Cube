import numpy as np
import os
from matplotlib import pyplot as plt
import keras
from keras.models import Sequential, save_model, load_model
from keras.layers import Dense


def greedy_action(values):
	return np.argmax(values)


def random_action():
	return np.random.randint(0, 12, 1)[0]


class QLAgent(object):
	def __init__(self):
		self.n_actions = 12
		self.state_size = 54
		self.qnn = self.q_val_model()
	
	def q_val_model(self):
		model = Sequential()
		model.add(Dense(self.state_size, activation='relu'))
		model.add(Dense(self.state_size * 3 // 2, activation='relu'))
		model.add(Dense(self.state_size * 3, activation='relu'))
		model.add(Dense(self.state_size * 3 // 2, activation='relu'))
		model.add(Dense(self.n_actions, activation='linear'))
		return model
	
	def save(self):
		save_model(self.qnn, "./models/q_learn_model.hdf5")
		return
	
	def load(self):
		self.qnn = load_model("./q_learn_model.hdf5")
	
	def egreedy_action(self, state, epsilon=0.5):
		coin = np.random.uniform(0, 1, 1)[0]
		if coin < epsilon:
			return random_action()
		else:
			values = self.qnn.predict(state)
			return greedy_action(values)
	
	def fit_model(self, X, Y):
		self.qnn.fit(X, Y, shuffle=True)
		return
