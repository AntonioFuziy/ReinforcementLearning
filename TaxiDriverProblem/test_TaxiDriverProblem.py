from datetime import datetime
from SearchAlgorithms import AEstrela
from TaxiDriverProblem import TaxiDriver

def test1():
  goal_location = (9,5)
  start_position = (0,0)
  passenger_position = (3,3)
  obstacles = []
  state = TaxiDriver(operator="", taxi_position=start_position, got_passenger=False, passenger_position=passenger_position, goal_location=goal_location, start_position=start_position, obstacles=obstacles, size_x=10, size_y=10)
  algorithm = AEstrela()
  inicio = datetime.now()
  result = algorithm.search(state)
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste 1")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.state.is_goal() == True
  
def test2():
  goal_location = (9,5)
  start_position = (0,0)
  passenger_position = (3,3)
  obstacles = [(1,0),(1,1),(1,3),(1,4)]
  state = TaxiDriver(operator="", taxi_position=start_position, got_passenger=False, passenger_position=passenger_position, goal_location=goal_location, start_position=start_position, obstacles=obstacles, size_x=10, size_y=10)
  algorithm = AEstrela()
  inicio = datetime.now()
  result = algorithm.search(state)
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste 2")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.state.is_goal() == True
  
def test3():
  goal_location = (9,5)
  start_position = (0,0)
  passenger_position = (3,3)
  obstacles = [(1,0),(1,1),(1,3),(1,4),(1,5),(1,6),(1,7)]
  state = TaxiDriver(operator="", taxi_position=start_position, got_passenger=False, passenger_position=passenger_position, goal_location=goal_location, start_position=start_position, obstacles=obstacles, size_x=10, size_y=10)
  algorithm = AEstrela()
  inicio = datetime.now()
  result = algorithm.search(state)
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste 3")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.state.is_goal() == True
  
def test4():
  goal_location = (9,5)
  start_position = (0,0)
  passenger_position = (3,3)
  obstacles = [(0,0),(1,0),(2,0),(3,0),(4,0)]
  state = TaxiDriver(operator="", taxi_position=start_position, got_passenger=False, passenger_position=passenger_position, goal_location=goal_location, start_position=start_position, obstacles=obstacles, size_x=10, size_y=10)
  algorithm = AEstrela()
  inicio = datetime.now()
  result = algorithm.search(state)
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste 4")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.state.is_goal() == True
  
def test5():
  goal_location = (9,5)
  start_position = (0,0)
  passenger_position = (3,3)
  obstacles = [(1,1),(2,2),(2,3),(2,4)]
  state = TaxiDriver(operator="", taxi_position=start_position, got_passenger=False, passenger_position=passenger_position, goal_location=goal_location, start_position=start_position, obstacles=obstacles, size_x=10, size_y=10)
  algorithm = AEstrela()
  inicio = datetime.now()
  result = algorithm.search(state)
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste 5")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.state.is_goal() == True