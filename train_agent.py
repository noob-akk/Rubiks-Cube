from RL import QLAgent, Env
import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt

# plt.figure()
# plt.ion()
# plt.show()
env = Env()
agent = QLAgent()
action_space = ["f", "b", "u", "d",
                "r", "l", "f'", "b'",
                "u'", "d'", "r'", "l'"]

eps_start = 0.99
eps_decay = 0.999
f = open("log.csv", "w+")
mean_rewards = []
for episode in tqdm(range(int(1e4))):
	states = []
	q_values = []
	actions = []
	rewards = []
	gamma = 1.
	epsilon = eps_start * (eps_decay ** episode)
	state = env.get_state()
	for i in range(100):
		pre_values, action = agent.egreedy_action(state, epsilon=epsilon)
		_, _, reward, next_state, done = env.step(action)
		pre_values[action] = reward + gamma * max(agent.get_action_values(next_state))
		states += [state]
		q_values += [pre_values]
		actions += [action]
		state = next_state
		rewards += [reward]
		if done:
			print("SOLVED !!!!")
			break
	# print(action, action_space[action], reward)
	# print("%d,%.4f,%.3f"%(episode+1, epsilon, np.mean(rewards)))
	f.write("%d,%.4f,%.3f\n" % (episode + 1, epsilon, np.mean(rewards)))
	mean_rewards += [np.mean(rewards)]
	agent.train(np.array(states), np.array(q_values))
	env.reset()
	if (episode+1) % 200 == 0:
		plt.figure()
		plt.plot(mean_rewards)
		plt.savefig("mean_rewards.png")
f.close()
