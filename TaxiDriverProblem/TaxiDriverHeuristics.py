import time
from SearchAlgorithms import AEstrela
from Graph import State

class TaxiDriver(State):
  def __init__(self, operator, taxi_position, got_passenger, passenger_position, goal_location, start_position, obstacles, size_x, size_y):
    self.operator = operator
    self.taxi_position = taxi_position
    self.got_passenger = got_passenger
    self.passenger_position = passenger_position
    self.goal_location = goal_location
    self.start_position = start_position
    self.obstacles = obstacles
    self.size_x = size_x
    self.size_y = size_y

  def env(self):
    return ";" + str(self.operator) + ";" + str(self.taxi_position) + ";" + str(self.got_passenger) + ";" + str(self.passenger_position)

  def sucessors(self):
    sucessors = []

    up = (self.taxi_position[0] - 1, self.taxi_position[1])
    down = (self.taxi_position[0] + 1, self.taxi_position[1])
    left = (self.taxi_position[0], self.taxi_position[1] - 1)
    right = (self.taxi_position[0], self.taxi_position[1] + 1)
    
    if self.can_move_taxi(up) and (up[0] >= 0):
      sucessors.append(TaxiDriver("UP", up, self.got_passenger, self.passenger_position, self.goal_location, self.start_position, self.obstacles, self.size_x, self.size_y))
    if self.can_move_taxi(down) and (down[0] < self.size_y):
      sucessors.append(TaxiDriver("DOWN", down, self.got_passenger, self.passenger_position, self.goal_location, self.start_position, self.obstacles, self.size_x, self.size_y))
    if self.can_move_taxi(right) and (right[1] < self.size_x):
      sucessors.append(TaxiDriver("RIGHT", right, self.got_passenger, self.passenger_position, self.goal_location, self.start_position, self.obstacles, self.size_x, self.size_y))
    if self.can_move_taxi(left) and (left[1] >= 0):
      sucessors.append(TaxiDriver("LEFT", left, self.got_passenger, self.passenger_position, self.goal_location, self.start_position, self.obstacles, self.size_x, self.size_y))
    
    if self.can_get_passenger():
      sucessors.append(TaxiDriver("GET PASSENGER", self.taxi_position, True, self.passenger_position, self.goal_location, self.start_position, self.obstacles, self.size_x, self.size_y))

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

  def can_move_taxi(self, next_position):
    for obstacle in self.obstacles:
      if next_position == obstacle:
        return False
    return True

  def description(self):
    return "Taxi Driver Problem"

  def print(self):
    return self.operator


def main():
  print("Taxi Driver Problem")
  goal_location = (9,5)
  start_position = (0,0)
  passenger_position = (3,3)
  obstacles = [(1,0),(1,1),(1,3),(1,4)]
  state = TaxiDriver(operator="", taxi_position=start_position, got_passenger=False, passenger_position=passenger_position, goal_location=goal_location, start_position=start_position, obstacles=obstacles, size_x=10, size_y=10)
  algorithm = AEstrela()
  start = time.time()
  result = algorithm.search(state)
  end = time.time()
  if result:
    print("Achou!")
    print(result.show_path())
    print('Duration in seconds = ' + str(end-start))
  else:
    print("Não achou solucao")

if __name__ == '__main__':
  main()