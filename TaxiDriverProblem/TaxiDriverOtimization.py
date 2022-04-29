from Graph import State
from SearchAlgorithms import AEstrela

class TaxiDriverOtimization(State):
  def __init__(self, taxi_position, passenger_position, got_passenger, operator, goal_location):
    self.taxi_position = taxi_position
    self.got_passenger = got_passenger
    self.passenger_position = passenger_position
    self.goal_location = goal_location
    self.operator = operator
    self.obstacles = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [1, 0], [1, 4], [1, 10], [2, 0], [2, 4], [2, 10], [3, 0], [3, 10], [4, 0], [4, 2], [4, 6], [4, 10], [5, 0], [5, 2], [5, 6], [5, 10], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [6, 9], [6, 10]]

  def env(self):
    return str(self.operator) + ";" + str(self.taxi_position) + ";" + str(self.got_passenger)

  def is_goal(self):
    if self.taxi_position == self.goal_location and self.got_passenger:
      return True
    return False

  def cost(self):
    return 1
  
  def description(self):
    return "Taxi Driver Problem"

  def print(self):
    return self.operator

  def sucessors(self):
    sucessors = []

    if [self.taxi_position[0]+1, self.taxi_position[1]] not in self.obstacles:
      sucessors.append(TaxiDriverOtimization([self.taxi_position[0]+1, self.taxi_position[1]], self.passenger_position, self.got_passenger, "0", self.goal_location))

    if [self.taxi_position[0]-1, self.taxi_position[1]] not in self.obstacles:
      sucessors.append(TaxiDriverOtimization([self.taxi_position[0]-1, self.taxi_position[1]], self.passenger_position, self.got_passenger, "1", self.goal_location))
    
    if [self.taxi_position[0], self.taxi_position[1]+1] not in self.obstacles:
      sucessors.append(TaxiDriverOtimization([self.taxi_position[0], self.taxi_position[1]+2], self.passenger_position, self.got_passenger, "2", self.goal_location))

    if [self.taxi_position[0], self.taxi_position[1]-1] not in self.obstacles:
      sucessors.append(TaxiDriverOtimization([self.taxi_position[0], self.taxi_position[1]-2], self.passenger_position, self.got_passenger, "3", self.goal_location))
    
    if self.can_get_passenger():
      sucessors.append(TaxiDriverOtimization(self.taxi_position, self.passenger_position, True, "4", self.goal_location))
    
    return sucessors
  
  def can_get_passenger(self):
    return self.taxi_position == self.passenger_position
    
  def h(self):
    if self.got_passenger:
      return abs(self.taxi_position[0]-self.goal_location[0]) + abs(self.taxi_position[1]-self.goal_location[1])

    return abs(self.taxi_position[0]-self.passenger_position[0]) + abs(self.taxi_position[1]-self.passenger_position[1])