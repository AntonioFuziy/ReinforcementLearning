import numpy as np
import random
from keras.activations import relu, linear
from tensorflow.keras.optimizers import Adam
from keras import Sequential
from keras.layers import Dense
import keras

class DoubleDQN:
  def __init__(self, env, gamma, epsilon, epsilon_min, epsilon_dec, episodes, batch_size, memory, step):
    self.env = env
    self.gamma = gamma
    self.epsilon = epsilon
    self.epsilon_min = epsilon_min
    self.epsilon_dec = epsilon_dec
    self.episodes = episodes
    self.batch_size = batch_size
    self.memory = memory
    self.step = step
    self.primary_network = self.build_network()
    self.target_network = keras.models.clone_model(self.primary_network)
    self.target_network.set_weights(self.primary_network.get_weights())

  def select_action(self, state):
    if np.random.rand() < self.epsilon:
      return random.randrange(self.env.action_space.n)
    action = self.target_network.predict(state, verbose=0)
    return np.argmax(action[0])

  def experience(self, state, action, reward, next_state, terminal):
    self.memory.append((state, action, reward, next_state, terminal))

  def experience_replay(self):
    if len(self.memory) > self.batch_size:
      batch = random.sample(self.memory, self.batch_size)
      states = np.array([i[0] for i in batch])
      actions = np.array([i[1] for i in batch])
      rewards = np.array([i[2] for i in batch])
      next_states = np.array([i[3] for i in batch])
      terminals = np.array([i[4] for i in batch])
      
      states = np.squeeze(states)
      next_states = np.squeeze(next_states)

      targets = rewards + self.gamma * (np.amax(self.primary_network.predict_on_batch(next_states), axis=1)) * (1 - terminals)
      targets_full = self.primary_network.predict_on_batch(states)

      indexes = np.array([i for i in range(self.batch_size)])
      targets_full[[indexes], [actions]] = targets

      self.primary_network.fit(states, targets_full, epochs=1, verbose=0)
      if self.epsilon > self.epsilon_min:
        self.epsilon *= self.epsilon_dec
    
    return
  
  def build_network(self):
    network = Sequential()
    network.add(Dense(512, activation=relu, input_dim=self.env.observation_space.shape[0]))
    network.add(Dense(256, activation=relu))
    network.add(Dense(self.env.action_space.n, activation=linear))
    network.compile(loss='mse', optimizer=Adam(learning_rate=0.001))
    return network

  def train(self):
    rewards = []
    for i in range(self.episodes+1):
      state = self.env.reset()
      state = np.reshape(state, (1, 8))
      score = 0
      max_steps = 3000
      for _ in range(max_steps):
        action = self.select_action(state)
        # self.env.render()
        next_state, reward, terminal, _ = self.env.step(action)
        score += reward
        next_state = np.reshape(next_state, (1, 8))
        self.experience(state, action, reward, next_state, terminal)
        state = next_state
        self.experience_replay()
        if terminal:
          print(f'Episódio: {i+1}/{self.episodes}. Score: {score}')
          break
      
      rewards.append(score)

      if i % self.step == 0 and i > 0:
        print("Updating target network...")
        self.target_network.set_weights(self.primary_network.get_weights())  

    self.target_network.save(f'data/double_DQN_{self.step}_model_lunar_land')
    return rewards
