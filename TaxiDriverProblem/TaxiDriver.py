
import gym
import numpy as np
from TaxiDriverHeuristics import TaxiDriverHeuristics
from SearchAlgorithms import AEstrela
from TaxiDriverOtimization import TaxiDriverOtimization

class TaxiDriver():
  def __init__(self, current_state, positions):
    self.current_state = current_state
    self.positions = list(positions)

    self.possible_destinations = {
      0: [1,1],
      1: [1,9],
      2: [5,1],
      3: [5,7]
    }
    
  def solve(self):
    goal_location = self.possible_destinations[self.positions[3]]
    start_position = [self.positions[0]+1 , self.positions[1]*2+1]
    passenger_position = self.possible_destinations[self.positions[2]]
    state = TaxiDriverOtimization(start_position, passenger_position, False, '', goal_location)
    algorithm = AEstrela()
    result = algorithm.search(state)
    return result

  def path(self):
    instructions = self.solve().show_path().replace(" ", "").replace(";", " ").split()
    for i in range(0, len(instructions)):
      instructions[i] = int(instructions[i])
    instructions.append(5)
    print(instructions)
    return instructions

def main():
  env = gym.make("Taxi-v3").env
  state = env.reset()
  # new_map = env.desc
  result = TaxiDriver(env.desc, env.decode(state))
  print(result.path())

if __name__ == '__main__':
  main()