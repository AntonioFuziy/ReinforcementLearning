from SearchAlgorithms import AEstrela
from Graph import State
import time
import copy

goal_state = [[1,2,3],
              [8,0,4],
              [7,6,5]]

first_test_board = [[5,4,0],[6,1,8],[7,3,2]] 

# tabuleiro_facil = [[8,1,3],[0,7,2],[6,5,4]]
# tabuleiro_dificil = [[7,8,6],[2,3,5],[1,4,0]]
# tabuleiro_dificil = [[7,8,6],[2,3,5],[0,1,4]]
# tabuleiro_dificil = [[8,3,6],[7,5,4],[2,1,0]]
# tabuleiro_impossivel = [[3,4,8],[1,2,5],[7,0,6]]
# tabuleiro_impossivel = [[3,4,8],[1,2,5],[7,0,6]]
# tabuleiro_impossivel = [[5,4,0],[6,1,8],[7,3,2]] 

class Puzzle8(State):
  def __init__(self, size, board, operator):
    self.size = size
    self.board = board
    self.operator = operator
  
  def sucessors(self):
    sucessores = []
    x, y = self.find_empty_position()
    if x > 0:
      #up
      temp1 = copy.deepcopy(self.board)
      temp1[x][y] = temp1[x-1][y]
      temp1[x-1][y] = 0
      sucessores.append(Puzzle8(self.size, temp1, "up"))
    if x < self.size - 1:
      #down
      temp2 = copy.deepcopy(self.board)
      temp2[x][y] = temp2[x+1][y]
      temp2[x+1][y] = 0
      sucessores.append(Puzzle8(self.size, temp2, "down"))
    if y > 0:
      #left
      temp3 = copy.deepcopy(self.board)
      temp3[x][y] = temp3[x][y-1]
      temp3[x][y-1] = 0
      sucessores.append(Puzzle8(self.size, temp3, "left"))
    if y < self.size - 1:
      #right
      temp4 = copy.deepcopy(self.board)
      temp4[x][y] = temp4[x][y+1]
      temp4[x][y+1] = 0
      sucessores.append(Puzzle8(self.size, temp4, "right"))

    return sucessores
  
  def find_empty_position(self):
    for i in range(0, self.size):
      for j in range(0, self.size):
        if self.board[i][j] == 0:
          return i, j

  def calculate_manhattan_distance(self):
    distance = 0
    for i in range(0, self.size):
      for j in range(0, self.size):
        x_goal, y_goal = self.return_goal_position(self.board[i][j]) 
        distance += abs(i-x_goal) + abs(j-y_goal)
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

  def check_solvable(self):
    expected_positions = {
      1: 0, 2: 1, 3: 2,
      8: 3, 0: 4, 4: 5,
      7: 6, 6: 7, 5: 8
    }

    temp_array = []
    for i in range(0, self.size):
      for j in range(0, self.size):
        temp_array.append(self.board[i][j])
    
    num_inversions = 0

    for i in range(0, 9):
      for j in range((i+1), 9):
        if temp_array[i] != 0 and temp_array[j] != 0 and expected_positions[temp_array[i]] > expected_positions[temp_array[j]]:
          num_inversions += 1
    return (num_inversions % 2 == 0)

def main():
  print('8 Puzzle Problem')
  board = first_test_board
  state = Puzzle8(size=3, board=board, operator="")
  if state.check_solvable():
    print("Solvable")
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
  else:
    print('Solucao Impossivel')
if __name__ == '__main__':
  main()