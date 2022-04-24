import time
from SearchAlgorithms import AEstrela
from Graph import State
import gym

env = gym.make("Taxi-v3").env

positions = {
  0: 'R',
  1: 'G',
  2: 'Y',
  3: 'B',
  4: False,
}

class TaxiDriver(State):
  def __init__(self, taxi_map, operator, current_state):
    self.current_state = current_state
    self.taxi_row, self.taxi_col, self.pass_idx, self.dest_idx = self.current_state
    self.taxi_map = taxi_map
    self.operator = operator
    self.taxi_position = (self.taxi_row, self.taxi_col)

  def env(self):
    return ";" + str(self.operator) + ";" + str(self.taxi_position) + ";" + str(self.got_passenger) + ";" + str(self.passenger_position)

  def sucessors(self):
    sucessors = []

    up = (self.taxi_position[0] - 1, self.taxi_position[1])
    down = (self.taxi_position[0] + 1, self.taxi_position[1])
    left = (self.taxi_position[0], self.taxi_position[1] - 1)
    right = (self.taxi_position[0], self.taxi_position[1] + 1)
    
    if self.can_move_taxi(up, "up") and (up[0] >= 0):
      sucessors.append(TaxiDriver("UP", up))
    if self.can_move_taxi(down, "down") and (down[0] < len(self.map)-1):
      sucessors.append(TaxiDriver("DOWN", down))
    if self.can_move_taxi(right, "right") and (right[1] < len(self.map)-1):
      sucessors.append(TaxiDriver("RIGHT", right))
    if self.can_move_taxi(left, "left") and (left[1] >= 0):
      sucessors.append(TaxiDriver("LEFT", left))
    
    if self.can_get_passenger():
      sucessors.append(TaxiDriver("GET PASSENGER", self.taxi_position, True, self.passenger_position, self.goal_location, self.start_position, self.obstacles, self.size_x, self.size_y))
    
    return sucessors

  def is_goal(self):
    if self.dest_idx == self.pass_idx:
      return True
    return False

  def cost(self):
    return 1

  def h(self):
    if self.map[self.pass_idx] != None:
      return abs(self.taxi_position[0]-self.goal_location[0]) + abs(self.taxi_position[1]-self.goal_location[1])

    return abs(self.taxi_position[0]-self.passenger_position[0]) + abs(self.taxi_position[1]-self.passenger_position[1])

  def can_get_passenger(self):
    if (self.taxi_position == self.passenger_position) and (not self.got_passenger):
      return True
    return False

  def can_move_taxi(self, next_position, direction):
    if self.taxi_map[next_position[0]][next_position[1]] != '|' and (direction == "left" or direction == "right"):
      return False
    if self.taxi_map[next_position[0]][next_position[1]] != '-' and (direction == "up" or direction == "down"):
      return False
    return True

  def description(self):
    return "Taxi Driver Problem"

  def print(self):
    return self.operator

def main():
  print("Taxi Driver Problem")
  state = env.reset()
  env.render()
  taxi_row, taxi_col, pass_idx, dest_idx = env.decode(state)
  print(taxi_row, taxi_col, pass_idx, dest_idx)
  goal_location = (9,5)
  start_position = (taxi_row, taxi_col)
  passenger_position = (3,3)
  # obstacles = [(1,0),(1,1),(1,3),(1,4)]
  state = TaxiDriver(operator="", taxi_position=start_position, got_passenger=False, passenger_position=passenger_position, goal_location=goal_location, start_position=start_position, state=state)
  algorithm = AEstrela()
  start = time.time()
  result = algorithm.search(state)
  end = time.time()
  if result:
    print("Achou!")
    print(result.show_path())
    env.render()
    print('Duration in seconds = ' + str(end-start))
  else:
    print("Não achou solucao")

if __name__ == '__main__':
  main()