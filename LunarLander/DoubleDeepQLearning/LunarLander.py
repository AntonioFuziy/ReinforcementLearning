import gym
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
from DoubleDeepQLearning import DoubleDQN

env = gym.make('LunarLander-v2')
np.random.seed(0)

print('State space: ', env.observation_space)
print('Action space: ', env.action_space)

gamma = 0.99 
epsilon = 1.0
epsilon_min = 0.01
epsilon_dec = 0.99
episodes = 350
batch_size = 64
memory = deque(maxlen=500000) 

DQN = DoubleDQN(env, gamma, epsilon, epsilon_min, epsilon_dec, episodes, batch_size, memory)
rewards = DQN.train()

import matplotlib.pyplot as plt
plt.plot(rewards)
plt.xlabel('Episodes')
plt.ylabel('# Rewards')
plt.title('# Rewards vs Episodes')
plt.savefig("results/lunar_lander_DoubleDeepQLearning.jpg")     
plt.close()
