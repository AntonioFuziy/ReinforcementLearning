
import gym
import numpy as np
from TaxiDriverHeuristics import TaxiDriverHeuristics
from SearchAlgorithms import AEstrela

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
    print(start_position)
    passenger_position = self.possible_destinations[self.positions[2]]
    obstacles = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [1, 0], [1, 4], [1, 10], [2, 0], [2, 4], [2, 10], [3, 0], [3, 10], [4, 0], [4, 2], [4, 6], [4, 10], [5, 0], [5, 2], [5, 6], [5, 10], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [6, 10]]
    state = TaxiDriverHeuristics(operator="", taxi_position=start_position, got_passenger=False, passenger_position=passenger_position, goal_location=goal_location, obstacles=obstacles)
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