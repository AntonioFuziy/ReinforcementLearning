import time
from SearchAlgorithms import AEstrela
from Graph import State

goal_location = (10,5)
start_position = (0,0)
passenger_position = (3,1)
obstacles = []

class TaxiDriver(State):
  def __init__(self, op, taxi_postition, got_passenger, passenger_destination, size_x, size_y):
    self.operator = op
    self.taxi_postition = taxi_postition
    self.got_passenger = got_passenger
    self.passenger_destination = passenger_destination
    self.size_x = size_x
    self.size_y = size_y

  def env(self):
    return ";"+ str(self.operator)

  def sucessors(self):
    sucessors = []
    return sucessors

  def is_goal(self):
    if (self.taxi_postition == self.passenger_destination) and self.got_passenger:
      return True
    return False

  def cost(self):
    return 1

  def h(self):
    pass

  def move_taxi(self):
    pass

  def description(self):
    return "Taxi Driver Problem"

  def print(self):
    return self.operator


def main():
  print("Taxi Driver Problem")
  state = TaxiDriver(op=None, taxi_postition=start_position, got_passenger=False, passenger_destination=goal_location, size_x=11, size_y=7)
  algorithm = AEstrela()
  print("Initial state with h = " + str(state.h()))
  start = time.time()
  result = algorithm.search(state)
  end = time.time()
  if result:
    print("Achou!")
    print(result.env())
    print('Final state with h = ' + str(result.h()))
    print('Duration in seconds = ' + str(end-start))
  else:
    print("Não achou solucao")

if __name__ == '__main__':
  main()