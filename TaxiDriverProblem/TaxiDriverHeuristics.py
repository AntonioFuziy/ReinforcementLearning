import time

import gym
import numpy as np
from SearchAlgorithms import AEstrela
from Graph import State

class TaxiDriverHeuristics(State):
  def __init__(self, operator, taxi_position, got_passenger, passenger_position, goal_location, obstacles):
    self.operator = operator
    self.taxi_position = taxi_position
    self.got_passenger = got_passenger
    self.passenger_position = passenger_position
    self.goal_location = goal_location
    self.obstacles = obstacles

  def env(self):
    return str(self.operator) + ";" + str(self.taxi_position) + ";" + str(self.got_passenger)

  def sucessors(self):
    sucessors = []
    
    if [self.taxi_position[0]+1, self.taxi_position[1]] not in self.obstacles:
      sucessors.append(TaxiDriverHeuristics("1", [self.taxi_position[0] - 1, self.taxi_position[1]], self.got_passenger, self.passenger_position, self.goal_location, self.obstacles))
    
    if [self.taxi_position[0]-1, self.taxi_position[1]] not in self.obstacles:
      sucessors.append(TaxiDriverHeuristics("0", [self.taxi_position[0] + 1, self.taxi_position[1]], self.got_passenger, self.passenger_position, self.goal_location, self.obstacles))
    
    if [self.taxi_position[0], self.taxi_position[1]+1] not in self.obstacles:
      sucessors.append(TaxiDriverHeuristics("2", [self.taxi_position[0], self.taxi_position[1] + 2], self.got_passenger, self.passenger_position, self.goal_location, self.obstacles))
    
    if [self.taxi_position[0], self.taxi_position[1]-1] not in self.obstacles:
      sucessors.append(TaxiDriverHeuristics("3", [self.taxi_position[0], self.taxi_position[1] - 2], self.got_passenger, self.passenger_position, self.goal_location, self.obstacles))
    
    if self.can_get_passenger():
      sucessors.append(TaxiDriverHeuristics("4", self.taxi_position, True, self.passenger_position, self.goal_location, self.obstacles))

    return sucessors

  def is_goal(self):
    if (self.taxi_position == self.goal_location) and self.got_passenger:
      return True
    return False

  def cost(self):
    return 1

  def h(self):
    if self.got_passenger:
      return abs(self.taxi_position[0]-self.goal_location[0]) + abs(self.taxi_position[1]-self.goal_location[1])

    return abs(self.taxi_position[0]-self.passenger_position[0]) + abs(self.taxi_position[1]-self.passenger_position[1])

  def can_get_passenger(self):
    if (self.taxi_position == self.passenger_position) and (not self.got_passenger):
      return True
    return False

  def description(self):
    return "Taxi Driver Problem"

  def print(self):
    return self.operator

# def main():
#   print("Taxi Driver Problem")
#   goal_location = (9,5)
#   start_position = (1,0)
#   passenger_position = (3,3)
#   obstacles = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [1, 0], [1, 4], [1, 10], [2, 0], [2, 4], [2, 10], [3, 0], [3, 10], [4, 0], [4, 2], [4, 6], [4, 10], [5, 0], [5, 2], [5, 6], [5, 10], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [6, 10]]  
#   state = TaxiDriverHeuristics(operator="", taxi_position=start_position, got_passenger=False, passenger_position=passenger_position, goal_location=goal_location, start_position=start_position, obstacles=obstacles, size_x=12, size_y=8)
#   algorithm = AEstrela()
#   start = time.time()
#   result = algorithm.search(state)
#   end = time.time()
#   if result:
#     print("Achou!")
#     print(result.show_path())
#     print('Duration in seconds = ' + str(end-start))
#   else:
#     print("Não achou solucao")

# if __name__ == '__main__':
#   main()