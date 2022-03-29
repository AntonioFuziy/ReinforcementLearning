from SearchAlgorithms import AEstrela
from Graph import State
import time
import copy

goal_state = [[1,2,3],
              [8,0,4],
              [7,6,5]]

first_test_board = [[8,1,3],[0,7,2],[6,5,4]]

class Puzzle8(State):
  def __init__(self, size, board, operator):
    self.size = size
    self.board = board
    self.operator = operator
  
  def sucessors(self):
    sucessores = []
    x, y = self.find_empty_position()
    if x > 0:
      #right
      temp1 = copy.deepcopy(self.board)
      temp1[x][y] = temp1[x-1][y]
      temp1[x-1][y] = 0
      sucessores.append(Puzzle8(self.size, temp1, "up"))
    if x < self.size - 1:
      #left
      temp2 = copy.deepcopy(self.board)
      temp2[x][y] = temp2[x+1][y]
      temp2[x+1][y] = 0
      sucessores.append(Puzzle8(self.size, temp2, "down"))
    if y > 0:
      #down
      temp3 = copy.deepcopy(self.board)
      temp3[x][y] = temp3[x][y-1]
      temp3[x][y-1] = 0
      sucessores.append(Puzzle8(self.size, temp3, "left"))
    if y < self.size - 1:
      #up
      temp4 = copy.deepcopy(self.board)
      temp4[x][y] = temp4[x][y+1]
      temp4[x][y+1] = 0
      sucessores.append(Puzzle8(self.size, temp4, "right"))
    for i in range(self.size):
      print(self.board[i])
    print("")
    return sucessores
  
  def find_empty_position(self):
    for i in range(0, self.size):
      for j in range(0, self.size):
        if self.board[i][j] == 0:
          # print(f"Zero x: {i} y: {j}")
          return i, j

  def calculate_manhattan_distance(self):
    distance = 0
    for i in range(0, self.size):
      for j in range(0, self.size):
        x_goal, y_goal = self.return_goal_position(self.board[i][j]) 
        distance += abs(i-x_goal) + abs(j-y_goal)
    print("Distance: ", distance)
    return distance
  
  def return_goal_position(self, number):
    if number == 0:
      return 1, 1
    elif number == 1:
      return 0, 0
    elif number == 2:
      return 0, 1
    elif number == 3:
      return 0, 2
    elif number == 4:
      return 1, 2
    elif number == 5:
      return 2, 2
    elif number == 6:
      return 2, 1
    elif number == 7:
      return 2, 0
    elif number == 8:
      return 1, 0
    else:
      raise Exception("Matriz errada")
                    
  def is_goal(self):
    if self.board == goal_state:
      return True
    return False
  
  def description(self):
    return "8 Puzzle Problem"
  
  def cost(self):
    return 1

  def print(self):
    return self.board

  def env(self):
    return str(self.board)
  
  def h(self):
    return self.calculate_manhattan_distance()

def main():
  print('8 Puzzle Problem')
  board = first_test_board
  state = Puzzle8(size=3, board=board, operator="")
  # state.generateBoard()
  algorithm = AEstrela()
  print("Initial state with h = "+str(state.h()))
  start = time.time()
  result = algorithm.search(state)
  end = time.time()
  if result != None:
    print('Achou!')
    print(result.show_path())
    print('Final state with h = '+str(result.h()))
    print('Duration in seconds = '+str(end-start))
  else:
    print('Nao achou solucao')

if __name__ == '__main__':
  main()