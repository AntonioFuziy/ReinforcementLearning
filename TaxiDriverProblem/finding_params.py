import gym
import numpy as np

env = gym.make("Taxi-v3").env
state = env.reset()
env.render()

# taxi_row, taxi_col, pass_idx, dest_idx = env.decode(state)
# print(taxi_row, taxi_col, pass_idx, dest_idx)

# for i in range(1, len(env.desc)-1):
#   for j in range(1, len(env.desc[i])-1):
#     # if env.desc[i] == b'|':
#     print(env.desc[i][j])
#     print(f"x: {i-1}, y: {j-1}")
#   print("")

def makeMap(desc):
  city = []
  coords = {}

  for idx_row, row in enumerate(desc):
    new_row = []
    coords = {}
      
    if idx_row in [0, (len(desc)-1)]:
      continue
    
    for idx_col, item in enumerate(row):
        
      if idx_col in [0, len(row)-1]:
        continue
        
      new_row.append(item.decode("utf-8"))
      
    city.append(new_row)

  for idx_row, row in enumerate(city):
    for idx_col, item in enumerate(row):
      if item.isalpha():
        coords[item] = (idx_row, int(idx_col/2))

  return city, coords
city, coords = makeMap(env.desc)
print(coords)
print(city)