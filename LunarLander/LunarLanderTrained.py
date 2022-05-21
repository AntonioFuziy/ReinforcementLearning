from tensorflow import keras
import numpy as np
import gym

env = gym.make('LunarLander-v2').env
state = env.reset()
model = keras.models.load_model('data/model_lunar_land', compile=False)
done = False
rewards = 0
steps = 0

while not done and steps < 300:
    Q_values = model.predict(state[np.newaxis])
    action = np.argmax(Q_values[0])
    state, reward, done, info = env.step(action)
    rewards += reward
    env.render()
    steps += 1

print(f'Score = {rewards}')
input('press a key...')