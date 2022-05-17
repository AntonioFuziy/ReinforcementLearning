import gym
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
from keras import Sequential
from keras.layers import Dense
from keras.activations import relu, linear
from tensorflow.keras.optimizers import Adam
from DeepQLearning import DeepQLearning

env = gym.make('LunarLander-v2')
env.seed(0)
np.random.seed(0)

# Actions:
# 0: Do nothing
# 1: Fire left engine
# 2: Fire down engine
# 3: Fire right engine

print('State space: ', env.observation_space)
print('Action space: ', env.action_space)

# para usar os ativadores de keras.activations é necessário usar o Sequential do keras também, 
# não importar o do tensorflow
model = Sequential()
model.add(Dense(512, activation=relu, input_dim=env.observation_space.shape[0]))
model.add(Dense(256, activation=relu))
model.add(Dense(env.action_space.n, activation=linear))
model.summary()
model.compile(loss='mse', optimizer=Adam(learning_rate=0.001))

gamma = 0.99 # 0.99 > 0.9
epsilon = 1.0
epsilon_min = 0.01
epsilon_dec = 0.99
episodes = 500
batch_size = 64
memory = deque(maxlen=500000) # deque performa melhor que lista, O(1) vs O(n)

DQN = DeepQLearning(env, gamma, epsilon, epsilon_min, epsilon_dec, episodes, batch_size, memory, model)
rewards = DQN.train()

import matplotlib.pyplot as plt
plt.plot(rewards)
plt.xlabel('Episodes')
plt.ylabel('# Rewards')
plt.title('# Rewards vs Episodes')
plt.savefig("results/lunar_lander_v1.jpg")     
plt.close()

