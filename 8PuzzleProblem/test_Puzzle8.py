from datetime import datetime
from SearchAlgorithms import AEstrela
from Puzzle8 import Puzzle8

goal_state = str([[1,2,3],
              [8,0,4],
              [7,6,5]])

def test1():
  board = [[8,1,3],[0,7,2],[6,5,4]]
  state = Puzzle8(3, board, "")
  algorithm = AEstrela()
  inicio = datetime.now()
  result = algorithm.search(state)
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste Fácil")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.state.env() == goal_state
  
def test2():
  board = [[7,8,6],[2,3,5],[1,4,0]] 
  state = Puzzle8(3, board, "")
  algorithm = AEstrela()
  inicio = datetime.now()
  result = algorithm.search(state)
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste Difícil")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.state.env() == goal_state
  
def test3():
  board = [[7,8,6],[2,3,5],[0,1,4]] 
  state = Puzzle8(3, board, "")
  algorithm = AEstrela()
  inicio = datetime.now()
  result = algorithm.search(state)
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste Difícil")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.state.env() == goal_state
  
def test4():
  board = [[8,3,6],[7,5,4],[2,1,0]] 
  state = Puzzle8(3, board, "")
  algorithm = AEstrela()
  inicio = datetime.now()
  result = algorithm.search(state)
  fim = datetime.now()
  print("")
  print("=======================================")
  print("Teste Difícil")
  print(f"Tempo de resolucao: {fim-inicio}")
  assert result.state.env() == goal_state
  
def test5():
  board = [[3,4,8],[1,2,5],[7,0,6]] 
  state = Puzzle8(3, board, "")
  print("")
  print("=======================================")
  print("Teste Impossível")
  print("Impossivel de resolver")
  assert state.check_solvable() == False