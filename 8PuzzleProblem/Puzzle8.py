from SearchAlgorithms import AEstrela
from Graph import State
import time

goal_state = [[1,2,3],
              [8,0,4],
              [7,6,5]]

first_test_board = [[8,1,3],
                    [0,7,2],
                    [6,5,4]]

class Puzzle8(State):
  def __init__(self, size, board, operator):
    self.size = size
    self.board = board
    self.operator = operator

  def env(self):
    return ";" + str(self.operator)
  
  def sucessors(self):
    sucessores = []
    x, y = self.find_empty_position()
    if x > 0:
      #right
      temp = self.board.copy()
      temp[y][x] = temp[y][x-1]
      temp[y][x-1] = 0
      print("right")
      sucessores.append(Puzzle8(self.size, temp, "right"))
    if x < self.size - 1:
      #left
      temp = self.board.copy()
      temp[y][x] = temp[y][x+1]
      temp[y][x+1] = 0
      print("left")
      sucessores.append(Puzzle8(self.size, temp, "left"))
    if y > 0:
      #down
      temp = self.board.copy()
      temp[y][x] = temp[y-1][x]
      temp[y-1][x] = 0
      print("down")
      sucessores.append(Puzzle8(self.size, temp, "down"))
    if y < self.size - 1:
      #up
      temp = self.board.copy()
      temp[y][x] = temp[y+1][x]
      temp[y+1][x] = 0
      print("up")
      sucessores.append(Puzzle8(self.size, temp, "up"))
    for i in range(len(self.board[0])):
      print(self.board[i])
    print("")
    return sucessores
  
  def find_empty_position(self):
    for i in range(0, len(self.board[0])):
      for j in range(0, len(self.board[0])):
        if self.board[i][j] == 0:
          # print(f"Zero x: {i} y: {j}")
          return i, j

  def calculate_manhattan_distance(self):
    distance = 0
    for i in range(0, len(self.board[0])):
      for j in range(0, len(self.board[0])):
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
    if self.board == goal_state:#self.board[0][0] == 1 and self.board[0][1] == 2 and self.board[0][2] == 3 and self.board[1][2] == 4 and self.board == [2][2] == 5 and self.board[2][1] == 6 and self.board[2][0] == 7 and self.board[0][1] == 8 and self.board[1][1] == 0:
      return True
    return False
  
  def description(self):
    return "8 Puzzle Problem"
  
  def cost(self):
    return 1

  def print(self):
    return self.board
  
  def h(self):
    return self.calculate_manhattan_distance()

  def generateBoard(self):
    self.board = first_test_board
    #printing matrix
    for i in self.board:
      print(i)

def main():
  print('8 Puzzle Problem')
  state = Puzzle8(size=3, board=None, operator=None)
  state.generateBoard()
  algorithm = AEstrela()
  print("Initial state with h = "+str(state.h()))
  start = time.time()
  result = algorithm.search(state)
  end = time.time()
  if result != None:
    print('Achou!')
    print(result.env())
    print('Final state with h = '+str(result.h()))
    print('Duration in seconds = '+str(end-start))
  else:
    print('Nao achou solucao')

if __name__ == '__main__':
  main()